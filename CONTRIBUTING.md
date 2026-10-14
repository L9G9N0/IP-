# Contributing Guidelines: Scientific & Code Collaboration

> **Document:** `CONTRIBUTING.md`  
> **Platform:** Evidence-Based CCU Research & Data Engine  
> **Status:** Canonical Contribution Standards  
> **Last Updated:** October 2026  

---

## 1. Welcome & Academic Contribution Philosophy

Thank you for your interest in contributing to the **Carbon Dioxide Utilisation (CCU) Evidence Engine & Review Platform** at IIIT-Delhi. 

This repository bridges cutting-edge catalytic chemistry with automated data engineering. Because all data directly feeds into peer-reviewed scientific publications, **we enforce strict standards of evidence, thermodynamic consistency, and data provenance**.

We welcome contributions from chemists, chemical engineers, computational researchers, and open-source scientific developers.

---

## 2. Core Contribution Principles

Before submitting any proposed changes, ensure your contributions adhere to our three non-negotiable principles:

1. **Strict DOI Traceability:** No performance number (conversion, selectivity, Faradaic efficiency, yield) can enter the datasets without an active, verified Digital Object Identifier (DOI) from a peer-reviewed journal.
2. **Thermodynamic Feasibility:** Reactions must balance stoichiometrically and obey thermodynamic state functions ($\Delta H^\circ$, $\Delta G^\circ$, $E^\circ$). Claims of spontaneous endothermic reactions or perpetual energy loops will be rejected.
3. **Metric Normalization:** When reporting electrocatalytic or photocatalytic benchmarks, you must decouple Faradaic efficiency from single-pass conversion and energy efficiency.

---

## 3. Contribution Pathways

### 3.1 Submitting New Literature Benchmarks
If you wish to add a landmark primary research paper published between 2020 and 2025:
1. Ensure the paper reports primary experimental or high-level DFT data (not second-hand review summaries).
2. Edit `scripts/build_literature_matrix.py`.
3. Add a new row adhering to the 32-column schema in `MASTER_LITERATURE_MATRIX.csv`.
4. Run `python3 scripts/build_literature_matrix.py` to regenerate the dataset.
5. In your Pull Request description, provide a PDF snippet or link to the specific page/figure where the metrics are reported.

### 3.2 Adding or Correcting Chemical Reactions
If you identify a missing reaction pathway or an error in thermodynamic parameters:
1. Verify the standard enthalpy ($\Delta H_{298\text{ K}}^\circ$) and Gibbs free energy ($\Delta G_{298\text{ K}}^\circ$) against NIST Chemistry WebBook or authoritative thermodynamic tables.
2. Edit `scripts/build_reaction_database.py`.
3. Run `python3 scripts/build_reaction_database.py`.

### 3.3 Correcting Documentation or Typos
Direct improvements to markdown dossiers (`research/pathways/*.md`, `research/lca_tea/*.md`, `docs/*.md`) or documentation files are welcome.

---

## 4. Development & Pull Request Workflow

### 4.1 Fork and Branch Setup
```bash
# Clone your fork
git clone https://github.com/<your-username>/IP-.git
cd IP-

# Create a dedicated feature branch
git checkout -b feature/add-tandem-dmc-benchmark
```

### 4.2 Making Changes & Regenerating Artifacts
Always edit the python generator scripts in `scripts/` rather than manually editing the generated CSV files. Run the appropriate script to update the target datasets:

```bash
python3 scripts/build_literature_matrix.py
python3 scripts/build_reaction_database.py
```

### 4.3 Automated Pre-PR Linting Checks
Execute the automated validation checks before committing:

```bash
# Check CSV validity
python3 -c "
import csv, glob
for path in glob.glob('research/**/*.csv', recursive=True):
    with open(path, 'r', encoding='utf-8') as f:
        reader = list(csv.reader(f))
        print(f'[OK] {path}: {len(reader)} rows')
"
```

### 4.4 Commit Message Conventions
We follow the [Conventional Commits](https://www.conventionalcommits.org/) specification:
- `feat:` Introduces a new dataset column, script feature, or pathway dossier.
- `fix:` Corrects a chemical formula, thermodynamic value, or citation typo.
- `docs:` Updates documentation, readmes, or publication plans.
- `chore:` Maintenance of `.gitignore`, licenses, or script formatting.

Example:
```bash
git commit -m "fix(chemistry): correct stoichiometric water coefficient in formic acid eCO2R"
```

---

## 5. Review & Acceptance Process

1. **Automated Validation:** The maintainers run the data consistency suite on incoming PRs.
2. **Scientific Peer Review:** Every PR is reviewed by at least one researcher at IIIT-Delhi for chemical accuracy and citation authenticity.
3. **Merge & Attribution:** Once approved, your changes will be merged into `main`, and your name will be acknowledged in the repository and subsequent journal publications.
