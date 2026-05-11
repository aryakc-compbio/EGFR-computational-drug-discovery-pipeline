import pandas as pd
import os

# Load inhibitor dataset
df = pd.read_csv("data/egfr_inhibitors.csv")

# Create output directory
os.makedirs("sdf", exist_ok=True)

for idx, row in df.iterrows():

    name = row["name"]
    smiles = row["smiles"]

    # Clean safe filename
    name = (
        str(name)
        .replace(" ", "_")
        .replace("/", "_")
        .replace("\\", "_")
    )

    # Temporary SMILES file
    smi_file = f"sdf/{name}.smi"

    with open(smi_file, "w") as f:
        f.write(smiles)

    # Generate 3D SDF structure
    cmd = f'obabel {smi_file} -O sdf/{name}.sdf --gen3d'

    print(f"Generating {name}.sdf")

    os.system(cmd)

print("\nAll 3D ligand structures generated.")
