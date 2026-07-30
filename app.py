import json
import pandas as pd

from lead_scorer import score_lead

# -------------------------------
# Load Sample Leads
# -------------------------------

with open("sample_leads.json", "r") as file:
    leads = json.load(file)

results = []

print("=" * 70)
print("      AI Lead Qualification & Sales Assistant")
print("=" * 70)

# -------------------------------
# Score Each Lead
# -------------------------------

for lead in leads:

    score, action = score_lead(lead)

    print(f"\nLead Name : {lead['name']}")
    print(f"Company   : {lead['company']}")
    print(f"Message   : {lead['message']}")
    print(f"Score     : {score}/100")
    print(f"Next Step : {action}")

    results.append({
        "Name": lead["name"],
        "Company": lead["company"],
        "Score": score,
        "Recommended Action": action
    })

# -------------------------------
# Save Results
# -------------------------------

df = pd.DataFrame(results)

df.to_csv("results.csv", index=False)

print("\n" + "=" * 70)
print("Lead qualification completed successfully!")
print("Results saved in results.csv")
print("=" * 70)