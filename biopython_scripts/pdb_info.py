from Bio.PDB import PDBParser

parser = PDBParser(QUIET=True)

structure = parser.get_structure(
    "EGFR",
    "../pdb_analysis/egfr_structure/1m17.pdb"
)

print("Structure ID:", structure.id)

model = structure[0]

print("\nChains:")
for chain in model:
    print(chain.id)

atom_count = 0

for atom in structure.get_atoms():
    atom_count += 1

print("\nTotal atoms:", atom_count)
