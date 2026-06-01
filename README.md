# EGFR Computational Drug Discovery Pipeline


Integrated computational biology and molecular modeling workflow for EGFR.

## Workflow Includes
- UniProt sequence analysis
- BLAST similarity search
- Multiple sequence alignment
- PDB structure analysis
- Ligand extraction
- ChEMBL bioactivity mining
- Molecular docking
- Molecular dynamics simulation
- Protein–ligand interaction analysis

## Tools
Python, Biopython, GROMACS, AutoDock Vina, PyMOL, Linux, gmx_MMPBSA tool

An end-to-end computational pipeline exploring EGFR (Epidermal Growth Factor Receptor) as a drug target, using gefitinib as the primary ligand. The pipeline covers target identification, sequence analysis, ligand mining, molecular docking, molecular dynamics simulation, and binding free energy estimation.

EGFR is a clinically validated oncology target — mutations in its kinase domain drive non-small cell lung cancer (NSCLC), and gefitinib is an FDA-approved first-generation EGFR inhibitor used in its treatment.

---

## Pipeline Overview

```
UniProt/PDB → BLAST → MSA (ClustalW) → ChEMBL mining → Docking (AutoDock Vina) → MD (GROMACS) → MM-GBSA
```

| Stage | Tool | Folder |
|---|---|---|
| Sequence retrieval and annotation | Biopython, UniProt | `uniprot_analysis/`, `biopython_scripts/` |
| Structure retrieval and analysis | PDB, Biopython | `pdb_analysis/egfr_structure/` |
| Homology search | BLAST | `blast_alignment/egfr_blast/` |
| Multiple sequence alignment | ClustalW | `msa_analysis/` |
| Bioactivity data mining | ChEMBL, RDKit | `chembl_analysis/` |
| Ligand preparation | Open Babel / manual | `ligand_preparation/gefitinib/` |
| Protein preparation | PyMOL | `protein_preparation/egfr_protein/` |
| Molecular docking | AutoDock Vina, PyMOL | `docking/gefitinib_docking/` |
| MD simulation | GROMACS | `md_simulation/egfr_gefitinib_md/` |
| Binding free energy | gmx_MMPBSA | `results/` |

---

## Key Results

### Protein Structure Assessment Before Docking

### Structure Selection

The EGFR kinase domain crystal structure (PDB ID: 1M17) was selected for molecular docking and molecular dynamics studies.

### Missing Residue Analysis

Prior to receptor preparation, the PDB structure was inspected for unresolved residues using the `REMARK 465` section of the PDB file.

The following missing residues were identified:

* Residues 666–671
* Residues 965–976
* Residues 996–998

### Binding Pocket Assessment

The co-crystallized inhibitor (AQ4, Erlotinib) was used to identify the ligand-binding pocket. Residues within 5 Å of the ligand were examined using PyMOL.

Key binding-site residues included:

* LEU694
* GLY695
* VAL702
* ALA719
* LYS721
* GLU738
* MET742
* LEU764
* ILE765
* THR766
* GLN767
* LEU768
* MET769
* PRO770
* PHE771
* GLY772
* CYS773
* LEU820
* THR830
* ASP831

### Decision on Structure Repair

Comparison of the missing residues with the ligand-binding pocket showed that all unresolved residues were located outside the active-site region and did not participate in ligand interactions.

Therefore, missing-residue reconstruction was not performed, as it was unlikely to influence docking accuracy or binding-site geometry. The experimentally resolved structure was used directly for receptor preparation and subsequent docking studies.

This assessment ensured that protein preparation decisions were based on structural and functional relevance rather than automatic residue reconstruction.


### Molecular Docking
Two clinically approved EGFR inhibitors were docked against the EGFR kinase domain crystal structure (PDB: 1IVO or equivalent):

| Ligand | Binding Affinity (kcal/mol) |
|---|---|
| Gefitinib | -8.3 |
| Erlotinib | -7.5 |

Gefitinib showed stronger predicted binding. Interaction analysis in BIOVIA Discovery Studio identified key contacts with **Val702, Lys721, Ala719, and Met769** — residues consistent with the known ATP-binding pocket of EGFR reported in the literature.

### Molecular Dynamics
- A 1 ns exploratory MD simulation of the EGFR-gefitinib complex was run in GROMACS to assess initial binding stability.
- Note: This is a short run intended for pipeline demonstration and preliminary stability assessment, not production-level sampling.

### MM-GBSA Binding Free Energy
- Estimated binding free energy for EGFR-gefitinib: **-20.34 kcal/mol** (gmx_MMPBSA)
- Negative value confirms thermodynamically favourable binding, consistent with the docking result.

---

## Tools and Environment

- **Python**: Biopython, RDKit, Pandas, Matplotlib
- **Docking**: AutoDock Vina, PyMOL
- **MD**: GROMACS, gmx_MMPBSA
- **Visualisation**: BIOVIA Discovery Studio, PyMOL
- **Databases**: UniProt, PDB, ChEMBL

---

## Folder Structure

```
EGFR-computational-drug-discovery-pipeline/
├── uniprot_analysis/          # Sequence retrieval and annotation
├── biopython_scripts/         # Biopython automation scripts
├── blast_alignment/egfr_blast/    # BLAST homology search outputs
├── msa_analysis/              # Multiple sequence alignment (ClustalW)
├── pdb_analysis/egfr_structure/   # PDB structure parsing and analysis
├── chembl_analysis/           # ChEMBL bioactivity mining and filtering
├── ligand_preparation/gefitinib/  # Ligand 3D prep and format conversion
├── protein_preparation/egfr_protein/  # Protein cleaning and prep for docking
├── docking/gefitinib_docking/ # AutoDock Vina config, outputs, interaction analysis
├── md_simulation/egfr_gefitinib_md/   # GROMACS topology, mdp files, trajectories
├── results/                   # MM-GBSA outputs and summary figures
└── docs/                      # Supporting notes and references
```

---

## Limitations and Notes

- MD simulation length is 1 ns, suitable for exploratory purposes only. Extended simulations would be required for convergence analysis and reliable free energy estimates.
- Erlotinib docking results are included for comparison; full interaction analysis for erlotinib will be added in a future update.
- This pipeline was built as a learning and practice project to integrate multiple computational drug discovery tools on a single validated target.

---

## References

- EGFR crystal structure: PDB
- Gefitinib, erlotinib bioactivity: ChEMBL
- gmx_MMPBSA: Valdés-Tresanco et al., *J. Chem. Theory Comput.*, 2021
