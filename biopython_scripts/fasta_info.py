from Bio import SeqIO

record = SeqIO.read(
    "../uniprot_analysis/egfr.fasta",
    "fasta"
)

print("Protein ID:", record.id)
print("Description:", record.description)
print("Sequence Length:", len(record.seq))

print("\nFirst 60 residues:")
print(record.seq[:60])

