# Contributing Guidelines: Scientific & Code Collaboration

> **Document:** `CONTRIBUTING.md`  
> **Platform:** Evidence-Based CCU Research & Data Engine  
> **Status:** Canonical Contribution Standards  
> **Last Updated:** October 2026  

---

## Table of Contents

- [Welcome & Philosophy](#welcome--philosophy)
- [Code of Conduct](#code-of-conduct)
- [Non-Negotiable Contribution Rules](#non-negotiable-contribution-rules)
- [Contribution Pathways](#contribution-pathways)
  - [Submitting New Literature Benchmarks](#submitting-new-literature-benchmarks)
  - [Adding or Correcting Chemical Reactions](#adding-or-correcting-chemical-reactions)
  - [Improving Documentation & Dossiers](#improving-documentation--dossiers)
- [Local Development Workflow](#local-development-workflow)
  - [Environment Setup](#environment-setup)
  - [Running Build Scripts](#running-build-scripts)
  - [Automated Testing & Linting](#automated-testing--linting)
- [Git Commit & Pull Request Standards](#git-commit--pull-request-standards)
  - [Conventional Commits](#conventional-commits)
  - [Pull Request Checklist](#pull-request-checklist)
- [Peer Review & Acceptance Process](#peer-review--acceptance-process)

---

## Welcome & Philosophy

Thank you for your interest in contributing to the **Carbon Dioxide Utilisation (CCU) Evidence Engine & Research Platform** at Indraprastha Institute of Information Technology Delhi (IIIT-Delhi).

This repository bridges chemical engineering, reaction kinetics, and software engineering. Because data from this platform feeds directly into peer-reviewed scientific publications, **we enforce strict standards of evidence, thermodynamic consistency, data provenance, and software quality**.

---

## Code of Conduct

All contributors and maintainers are expected to adhere to the [Code of Conduct](CODE_OF_CONDUCT.md). We are committed to providing a welcoming, harassment-free environment for everyone.

---

## Non-Negotiable Contribution Rules

Before submitting any proposed modification, ensure your contribution satisfies these four requirements:

1. **Strict DOI Traceability:** No performance metric (conversion, Faradaic efficiency, selectivity, overpotential, current density) may enter datasets without an active, verified Digital Object Identifier (DOI) resolving to a peer-reviewed journal or recognized standard body.
2. **Thermodynamic Feasibility:** Reactions must balance stoichiometrically for mass and charge and obey thermodynamic state functions ($\Delta H^\circ$, $\Delta G^\circ$, $E^\circ$). Claims of spontaneous endothermic reactions or perpetual energy loops will be rejected immediately.
3. **Metric Normalization:** When reporting electrocatalytic or photocatalytic benchmarks, you must decouple Faradaic efficiency from single-pass conversion, carbonate crossover, and overall cell energy efficiency.
4. **RFC 4180 CSV Compliance:** All dataset edits must conform strictly to RFC 4180 rules (exact column counts per row, minimal quoting, UTF-8 encoding).

---

## Contribution Pathways

### Submitting New Literature Benchmarks
If you wish to add a landmark primary research paper published between 2020 and 2026:
1. Ensure the paper reports primary experimental or high-level DFT data (not second-hand review summaries).
2. Edit [`scripts/build_literature_matrix.py`](scripts/build_literature_matrix.py) to append a new record matching the 32-column schema.
3. Run `python3 scripts/build_literature_matrix.py` to regenerate [`research/literature/MASTER_LITERATURE_MATRIX.csv`](research/literature/MASTER_LITERATURE_MATRIX.csv).
4. In your Pull Request description, provide a page/figure reference from the primary paper where the values are documented.

### Adding or Correcting Chemical Reactions
If you identify a missing reaction pathway or an error in thermodynamic parameters:
1. Verify the standard enthalpy ($\Delta H_{298\text{ K}}^\circ$) and Gibbs free energy ($\Delta G_{298\text{ K}}^\circ$) against the NIST Chemistry WebBook.
2. Edit [`scripts/build_reaction_database.py`](scripts/build_reaction_database.py) to update or append the reaction definition.
3. Run `python3 scripts/build_reaction_database.py` to regenerate the database.
4. Run `pytest tests/test_reactions.py` to verify thermodynamic consistency.

### Improving Documentation & Dossiers
Direct improvements to pathway reports ([`research/pathways/*.md`](research/pathways/)), LCA/TEA assumptions ([`research/lca_tea/*.md`](research/lca_tea/)), or root documentation are welcome. Please ensure all Markdown follows GitHub Flavored Markdown (GFM) standards and maintains a clean heading hierarchy.

---

## Local Development Workflow

### Environment Setup
```bash
# Clone your fork
git clone https://github.com/<your-username>/IP-.git
cd IP-

# Set up an isolated virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install development dependencies
pip install -r requirements-dev.txt
```

### Running Build Scripts
Execute build operations using the provided [`Makefile`](Makefile):

```bash
# Rebuild all datasets and dossiers deterministically
make build

# Run the automated test suite
make test

# Run code style formatting and linting
make lint

# Run static type checking
make typecheck
```

### Automated Testing & Linting
Before opening a Pull Request, verify that all automated checks pass locally:

```bash
# Verify CSV schema integrity
pytest tests/test_csv_integrity.py

# Verify reaction thermodynamics
pytest tests/test_reactions.py

# Run ruff linter
ruff check .
```

---

## Git Commit & Pull Request Standards

### Conventional Commits
We adhere to the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) specification:
- `feat:` Introduces a new dataset column, script feature, or pathway dossier.
- `fix:` Corrects a chemical formula, thermodynamic value, or citation typo.
- `docs:` Updates documentation, readmes, or publication plans.
- `test:` Adds or updates automated tests.
- `refactor:` Code refactoring without behavioral changes.
- `chore:` Maintenance of configuration, dependencies, or licenses.

Example:
```bash
git commit -m "fix(chemistry): correct stoichiometric water coefficient in formic acid eCO2R"
```

### Pull Request Checklist
When submitting a Pull Request, confirm that:
- [ ] Changes were made to generator scripts in `scripts/`, and all artifacts were regenerated (`make build`).
- [ ] All automated tests pass (`make test`).
- [ ] Code conforms to style guidelines (`make lint`).
- [ ] New literature citations include verified DOIs.
- [ ] PR title follows Conventional Commits format.

---

## Peer Review & Acceptance Process

1. **Automated CI Checks:** Every incoming PR triggers GitHub Actions to run the full test suite across Python 3.11, 3.12, 3.13, and 3.14.
2. **Scientific Review:** At least one research team member from IIIT-Delhi reviews the PR for chemical validity, mass/charge balance, and citation fidelity.
3. **Merge & Attribution:** Once approved, your PR will be merged into `main`, and your contribution will be acknowledged in release notes and subsequent journal manuscripts.
