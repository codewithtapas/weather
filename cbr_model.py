import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
from xgboost import XGBRegressor

# Load data
data = pd.read_csv("cbr_data.csv")
data = data.dropna()

# 🔥 Feature Engineering
data["Clay_StoneDust"] = data["Clay"] * data["StoneDust"]
data["OMC_MDD"] = data["OMC"] * data["MDD"]
data["PI_OMC"] = data["PI"] * data["OMC"]

# Features
X = data[[
    "Clay", "StoneDust", "OMC", "MDD", "PI",
    "Clay_StoneDust", "OMC_MDD", "PI_OMC"
]]
y = data["CBR"]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 🔥 Better Model
model = XGBRegressor(
    n_estimators=800,
    learning_rate=0.03,
    max_depth=8,
    subsample=0.9,
    colsample_bytree=0.9,
    gamma=0.1,
    reg_alpha=0.1,
    reg_lambda=1,
    random_state=42
)

# Train
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluation
r2 = r2_score(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print("R2 Score:", r2)
print("RMSE:", rmse)
importance = model.feature_importances_

feature_importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": importance
})

# ❌ Remove unwanted feature
feature_importance = feature_importance[feature_importance["Feature"] != "Clay_StoneDust"]

# ✅ Sort again after removal
feature_importance = feature_importance.sort_values(by="Importance", ascending=False)

plt.figure(figsize=(10,6))
plt.barh(feature_importance["Feature"], feature_importance["Importance"])
plt.gca().invert_yaxis()

for i, v in enumerate(feature_importance["Importance"]):
    plt.text(v + 0.001, i, f"{v:.3f}")

plt.title("Feature Importance for CBR Prediction (XGBoost)")
plt.xlabel("Importance Score")

plt.savefig("feature_importance.png", dpi=300, bbox_inches='tight')
plt.show()