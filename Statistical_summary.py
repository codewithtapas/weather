import pandas as pd
import matplotlib.pyplot as plt

# File name
file_name = "statistical_summary"

# Load dataset
df = pd.read_csv("cbr_data.csv")

# Create statistical summary
summary = pd.DataFrame({
    "Mean": df.mean(),
    "Median": df.median(),
    "Std Dev": df.std(),
    "Minimum": df.min(),
    "Maximum": df.max(),
    "Skewness": df.skew(),
    "Kurtosis": df.kurt()
}).round(3)

# Add "Parameter" column
summary.reset_index(inplace=True)
summary.rename(columns={"index": "Parameter"}, inplace=True)

# Save CSV
summary.to_csv(f"{file_name}.csv", index=False)

# ---- Create Image ----
fig, ax = plt.subplots(figsize=(10, 6))
ax.axis('off')

table = ax.table(
    cellText=summary.values,
    colLabels=summary.columns,
    loc='center'
)

table.auto_set_font_size(False)
table.set_fontsize(10)
table.auto_set_column_width(col=list(range(len(summary.columns))))

# Save image
plt.savefig(f"{file_name}.png", bbox_inches='tight', dpi=300)

plt.close()

print("✅ Files saved successfully with 'Parameter' column!")