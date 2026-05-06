import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from xgboost import XGBRegressor

# Load data
data = pd.read_csv("cbr_data.csv")

# Features
X = data[["Clay", "StoneDust", "OMC", "MDD", "PI"]]
y = data["CBR"]

# Train model
model = XGBRegressor()
model.fit(X, y)

# Predict
data["Predicted_CBR"] = model.predict(X)

# Plot graphs
features = ["Clay", "StoneDust", "OMC", "MDD", "PI"]

for feature in features:

    g = sns.jointplot(
        x=data[feature],
        y=data["Predicted_CBR"],
        kind="scatter",
        height=6,
        marginal_kws=dict(bins=15, fill=True)
    )

    # Labels
    g.set_axis_labels(feature, "Predicted CBR", fontsize=16)

    # Title FIX (use fig instead of plt)
    g.fig.suptitle(f"{feature} vs Predicted CBR", fontsize=18)

    # IMPORTANT: adjust layout (this fixes top cut issue)
    g.fig.subplots_adjust(top=0.92)

    # Tick size
    g.ax_joint.tick_params(labelsize=12)

    plt.show()