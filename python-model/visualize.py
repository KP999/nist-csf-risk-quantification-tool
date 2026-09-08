import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from risk_model import df

# This script visualizes the risk data in a heatmap format, showing the inherent risk scores based on severity and likelihood.

levels = ["LOW", "MEDIUM", "HIGH"]

# Pivot: rows = severity, columns = likelihood, values = inherent risk score
grid = df.pivot_table(
    index="severity", columns="likelihood", values="inherent_risk", aggfunc="first"
)
grid = grid.reindex(index=levels[::-1], columns=levels) # HIGH severity on top, LOW to HIGH likelihood left to right

# Seperates the names of the risks in each cell of the grid
name_grid = (
    df.groupby(["severity", "likelihood"])["name"]
    .apply(lambda names: "\n".join(names))
    .unstack()
    .reindex(index=levels[::-1], columns=levels)
)

plt.figure(figsize=(8, 6))
sns.heatmap(
    grid,
    annot=name_grid,
    fmt="",
    cmap="RdYlGn_r",
    linewidths=1,
    linecolor="white",
    cbar_kws={"label": "Inherent Risk Score"},
)
# Add labels and title
plt.title("Risk Heat Map (Likelihood x Severity)")
plt.xlabel("Likelihood")
plt.ylabel("Severity")
plt.tight_layout()
plt.savefig("heatmap.png", dpi=150)
plt.show()

print(grid)