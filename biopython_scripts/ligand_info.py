from Bio.PDB import PDBParser

parser = PDBParser(QUIET=True)

structure = parser.get_structure(
    "EGFR",
    "../pdb_analysis/egfr_structure/1m17.pdb"
)

print("Ligands found:\n")

for model in structure:
    for chain in model:
        for residue in chain:
            if residue.id[0] != " " and residue.resname != "HOH":
                print(residue.resname)
