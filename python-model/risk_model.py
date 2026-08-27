import pandas as pd
from risk_data import risks

df = pd.DataFrame(risks)

# Convert likelihood and severity to numerical scores
scale = {"LOW": 3, "MEDIUM": 6, "HIGH": 9}
df["likelihood_score"] = df["likelihood"].map(scale)
df["severity_score"] = df["severity"].map(scale)

# Calculate inherent risk score
df["inherent_risk"] = df["likelihood_score"] * df["severity_score"]

# Calculate residual risk after applying a given control
def residual_risk(row, control_name):
    reduction_likelihood, reduction_severity = row["reductions"][control_name]
    return row["inherent_risk"] * (1 - reduction_likelihood) * (1 - reduction_severity)

# Build one residual-risk column per control
control_names = list(df.loc[0, "reductions"].keys())
for control in control_names:
    column_name = "residual_" + control.lower().replace(" ", "_").replace("&", "and")
    df[column_name] = df.apply(lambda row: residual_risk(row, control), axis=1)

residual_columns = [c for c in df.columns if c.startswith("residual_")]

# Identify the best control for each risk based on the lowest residual risk
df["best_control"] = df[residual_columns].idxmin(axis=1)
df["lowest_residual_risk"] = df[residual_columns].min(axis=1)

# Map each residual column name back to its clean control name for display
column_to_control = {
    "residual_" + c.lower().replace(" ", "_").replace("&", "and"): c
    for c in control_names
}
df["best_control"] = df["best_control"].map(column_to_control)

if __name__ == "__main__":
    print(df[["name", "inherent_risk", "best_control", "lowest_residual_risk"]])
    print()
    for control in control_names:
        column_name = "residual_" + control.lower().replace(" ", "_").replace("&", "and")
        reduction_pct = (df["inherent_risk"] - df[column_name]) / df["inherent_risk"]
        print(f"{control}: {reduction_pct.mean():.1%}")