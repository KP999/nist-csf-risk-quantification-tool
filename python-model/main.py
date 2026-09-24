from risk_model import df, average_reduction_by_control

# Print a summary of the risk data, including inherent risk, best control, and lowest residual risk for each risk.
def print_summary():
    print("=" * 50)
    print("NIST CSF RISK QUANTIFICATION TOOL")
    print("=" * 50)
    print()
    print("Risk Summary (Inherent Risk, Best Control, Residual Risk)")
    print("-" * 50)
    print(df[["name", "inherent_risk", "best_control", "lowest_residual_risk"]].to_string(index=False))

# Print average risk reduction by control. Sorted reductions gives back a dictionary and uses key=lambda item: item[1] to sort by the second item in the tuple (the percentage reduction).
# The reverse=True argument sorts in descending order, ranking from best to worst
# 
def print_average_reduction():
    print()
    print("Average Risk Reduction by Control (Across All Risks)")
    print("-" * 50)
    reductions = average_reduction_by_control()
    ranked = sorted(reductions.items(), key=lambda item: item[1], reverse=True)
    for control, pct in ranked:
        print(f"{control:<40}: {pct:.1%}")

# Generate a heatmap of the risk data. This function imports the visualize module, which builds and saves the heatmap as heatmap.png.
def generate_heatmap():
    print()
    print("Generating risk heat map...")
    import visualize  # running this module builds and saves heatmap.png
    print("Saved to heatmap.png")

if __name__ == "__main__":
    print_summary()
    print_average_reduction()
    generate_heatmap()