import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor

# Load original dataset
data = pd.read_csv("cbr_data.csv")

# Features
X = data[["Clay", "StoneDust", "OMC", "MDD", "PI"]]
y = data["CBR"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = XGBRegressor()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Plot Actual vs Predicted
plt.figure(figsize=(8,6))
plt.scatter(y_test, y_pred)

# Perfect line
max_val = max(y_test.max(), y_pred.max())

plt.plot([0, max_val], [0, max_val], linestyle='--')

# ✅ ADD HERE (IMPORTANT)
plt.xlim(0, max_val)
plt.ylim(0, max_val)

# Labels
plt.xlabel("Actual CBR", fontsize=21)
plt.ylabel("Predicted CBR", fontsize=21)
plt.title("Actual vs Predicted CBR", fontsize=21)

plt.grid(alpha=0.3)

plt.savefig("actual_vs_predicted.png", dpi=300, bbox_inches='tight')
plt.show()