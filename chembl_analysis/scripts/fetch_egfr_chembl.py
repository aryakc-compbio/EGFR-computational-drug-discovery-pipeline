from chembl_webresource_client.new_client import new_client
import pandas as pd

# ChEMBL clients
target = new_client.target
activity = new_client.activity
molecule = new_client.molecule

# Search EGFR target
targets = target.search("EGFR")

egfr = None

for t in targets:
    if "Epidermal growth factor receptor" in str(t):
        egfr = t
        break

if egfr is None:
    raise ValueError("EGFR target not found")

print("Selected target:", egfr["target_chembl_id"])

target_id = egfr["target_chembl_id"]

# Fetch IC50 activity data
res = activity.filter(
    target_chembl_id=target_id,
    standard_type="IC50"
).only(
    "molecule_chembl_id",
    "canonical_smiles",
    "standard_value"
)

data = []

for r in res:

    if not r["canonical_smiles"]:
        continue

    if not r["standard_value"]:
        continue

    chembl_id = r["molecule_chembl_id"]

    # Fetch molecule metadata
    try:
        mol = molecule.get(chembl_id)
        name = mol.get("pref_name")

    except Exception:
        name = None

    # Fallback if no preferred name
    if not name:
        name = chembl_id

    # Clean filename-safe name
    name = (
        name.replace(" ", "_")
            .replace("/", "_")
            .replace("\\", "_")
    )

    data.append({
        "name": name,
        "chembl_id": chembl_id,
        "smiles": r["canonical_smiles"],
        "IC50_nM": r["standard_value"]
    })

# Create dataframe
df = pd.DataFrame(data)

# Clean IC50 values
df["IC50_nM"] = pd.to_numeric(df["IC50_nM"], errors="coerce")
df = df.dropna()

# Remove duplicates
df = df.drop_duplicates(subset=["chembl_id"])

# Sort by potency
df = df.sort_values("IC50_nM")

# Keep top 50 inhibitors
df = df.head(50)

# Save dataset
df.to_csv("data/egfr_inhibitors.csv", index=False)

print("\nTop inhibitors:")
print(df.head())

print("\nSaved dataset to:")
print("data/egfr_inhibitors.csv")
