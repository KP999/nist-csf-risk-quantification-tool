# Cybersecurity Risk Assessment Tool

An Excel-based risk quantification model built on the NIST Cybersecurity Framework (CSF), designed to score inherent risk, model the effect of individual security controls, and identify which control most reduces each risk.

Built as a portfolio extension of risk quantification work I did during the EY Trajectory Program, where I built a similar tool applying NIST CSF controls (ID.RA, PR.AT, PR.DS) to assess phishing, data breach, and web application risks for a model financial institution.

## What it does

- Logs risk scenarios with a description, the CIA principle(s) they threaten (Confidentiality, Integrity, Availability), and a Likelihood / Severity rating (Low/Medium/High)
- Calculates an **Inherent Risk Value** (Likelihood × Severity) and classifies it into a Risk Level (Low/Medium/High/Critical) with threshold bands.
- Models up to six security controls per risk, each with an estimated percentage reduction to Likelihood and Severity
- Calculates **Residual Risk** for every control automatically: `Inherent Risk × (1 − Likelihood Reduction) × (1 − Severity Reduction)`
- Automatically flags the **best-performing control** for each risk (lowest residual risk) and what percentage of inherent risk it eliminates
- Visualizes residual risk across all controls in a comparison chart
- Recalculates live.

## Methodology

Likelihood and Severity are each scored on a qualitative scale (Low = 3, Medium = 6, High = 9), multiplied to produce a 9-point-to-81-point inherent risk score. This is a standard semi-quantitative approach consistent with NIST SP 800-30 and NIST CSF's risk assessment category (ID.RA). Risk level thresholds and control-effectiveness percentages are analyst judgment calls made for this model company; THEY ARE NOT SOURCED FROM A REAL BREACH DATASET AND ARE DOCUMENTED AS ASSUMPTIONS IN THE WORKBOOK ITSELF.
## Repo contents

- `Risk_Assessment_Tool_Old.xlsx` — the original prototype model (Introduction, Tutorial, and Risk Assessment Tool tabs)
- `Risk_Assessment_Tool.xlsx` — the full revamped model (Introduction, Tutorial, and Risk Assessment Tool tabs)
- `risk_model.py` — *(planned)* a Python/pandas rebuild of the same logic, for a code-based version of the same analysis
- `screenshots/` — *(planned)* a couple of screenshots of the register and chart, for anyone who doesn't want to download the file to see it

## Why I built this

The original risk scoring sheet I built during the EY Trajectory Program showed me how important risk scoring, assessment, and mitigation are to preventing security incidents. While the tool was successful, there were many limitations, such as no automatic "best control" identification, no risk level classification, no input validation, and overall lacking polish. So I rebuilt this project to close that gap. 
This tool is meant to demonstrate that I can take a framework like NIST CSF and turn it into something usable: not just naming risks and describing how they might affect a business, but scoring them, modeling which controls reduce them the most, and showing the reasoning behind every number. Redoing this project helps turn "this could be bad" into a number a business can actually act on, a core GRC/risk analyst responsibility.

## Limitations / next steps

- Ratings and control-effectiveness percentages are illustrative, not derived from real incident data
- Only six risk scenarios are modeled currently — a production version would cover a broader risk universe
- A Python version (pandas for the model, matplotlib for visualization) is in progress to show the same logic implemented in code
