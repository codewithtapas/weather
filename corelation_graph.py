import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv("cbr_data.csv")

# Select relevant columns
corr_data = data[["Clay", "StoneDust", "OMC", "MDD", "PI", "CBR"]]

# Compute correlation matrix
corr_matrix = corr_data.corr()

# Plot heatmap
plt.figure(figsize=(8,6))
sns.heatmap(
    corr_matrix,
    annot=True,
    cmap="coolwarm",
    fmt=".2f",
    linewidths=0.5
)

plt.title("Correlation Matrix", fontsize=18)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

plt.tight_layout()

# ✅ Save in same folder
plt.savefig("correlation_matrix.png", dpi=300, bbox_inches='tight')

plt.show()