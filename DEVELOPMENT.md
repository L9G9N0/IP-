# Local Development & Build Environment Guide

> **Document:** `DEVELOPMENT.md`  
> **Platform:** Evidence-Based CCU Research & Data Engine  
> **Status:** Canonical Developer Guide  
> **Last Updated:** October 2026  

---

## Table of Contents

- [Prerequisites & System Requirements](#prerequisites--system-requirements)
- [Local Setup & Repository Initialization](#local-setup--repository-initialization)
- [Makefile Automation & Standard Commands](#makefile-automation--standard-commands)
- [Build Script Execution & Pipeline Commands](#build-script-execution--pipeline-commands)
- [Coding Standards & Python 3.14 Considerations](#coding-standards--python-314-considerations)
  - [Raw String Literals for Multiline Strings with LaTeX](#raw-string-literals-for-multiline-strings-with-latex)
  - [RFC 4180 CSV Conformance](#rfc-4180-csv-conformance)
  - [Root-Relative Path Resolution](#root-relative-path-resolution)
- [Automated Data Quality & Integrity Auditing](#automated-data-quality--integrity-auditing)
- [How to Add New Literature & Reactions](#how-to-add-new-literature--reactions)
  - [Adding a New Benchmark Paper](#adding-a-new-benchmark-paper)
  - [Adding a New Chemical Reaction](#adding-a-new-chemical-reaction)
- [Git Workflow & Commit Hygiene](#git-workflow--commit-hygiene)

---

## Prerequisites & System Requirements

The platform is designed to be completely portable, lightweight, and executable with zero external third-party Python runtime installations.

### Supported Operating Systems
- **macOS:** Ventura (13.x), Sonoma (14.x), Sequoia (15.x)
- **Linux:** Ubuntu 22.04/24.04 LTS, Debian 12, RHEL 9, Arch Linux
- **Windows:** Windows 10/11 via WSL2 (recommended) or native PowerShell

### Toolchain Dependencies
- **Python:** 3.11, 3.12, 3.13, or 3.14
- **Git:** Version 2.40 or newer
- **Make:** GNU Make (optional, but recommended for single-command automation)

---

## Local Setup & Repository Initialization

Clone the official GitHub repository and navigate into the project root:

```bash
# Clone the repository
git clone https://github.com/L9G9N0/IP-.git
cd IP-

# Set up an isolated Python virtual environment (recommended for development)
python3 -m venv .venv

# Activate the virtual environment
# On macOS / Linux:
source .venv/bin/activate
# On Windows (PowerShell):
# .venv\Scripts\Activate.ps1

# Install development, testing, and linting tools
pip install -r requirements-dev.txt
```

---

## Makefile Automation & Standard Commands

The repository provides a standard [`Makefile`](Makefile) for standardizing daily developer workflows:

| Target | Description |
|---|---|
| `make build` | Deterministically executes the full data generation and synthesis pipeline |
| `make test` | Executes the complete `pytest` test suite with duration profiling |
| `make lint` | Runs `ruff` static code analysis and checks formatting |
| `make typecheck` | Runs `mypy` strict static type analysis on all scripts |
| `make format` | Automatically formats code using `ruff` |
| `make clean` | Removes Python caches (`__pycache__`), `.pytest_cache`, and OS artifacts |
| `make verify-csv` | Validates RFC 4180 column count integrity across all CSV databases |

---

## Build Script Execution & Pipeline Commands

All data generation scripts reside in `scripts/`. Scripts can be executed individually with standard CLI flags or executed in sequence:

```bash
# 1. Regenerate Master Literature Matrix (research/literature/MASTER_LITERATURE_MATRIX.csv)
python3 scripts/build_literature_matrix.py

# 2. Regenerate Chemical Reaction Database & Mechanistic Dossiers
python3 scripts/build_reaction_database.py

# 3. Regenerate all 13 Pathway Research Dossiers (research/pathways/*.md)
python3 scripts/build_pathway_reports.py

# 4. Regenerate Life-Cycle & Techno-Economic Models (research/lca_tea/)
python3 scripts/build_lca_tea.py

# 5. Regenerate Cross-Pathway Table & Figure Blueprints (research/tables/, research/figures/)
python3 scripts/build_tables_and_figures.py

# 6. Regenerate Research Gaps & Novelty Analysis (research/gaps/)
python3 scripts/build_research_gaps.py

# 7. Regenerate Claim Register (research/evidence/CLAIM_REGISTER.csv)
python3 scripts/build_claim_register.py

# 8. Regenerate Risk Registers & Consistency Audits
python3 scripts/build_docs_and_qc.py

# 9. Recompile Full Revised Manuscript Draft
python3 scripts/build_final_manuscript.py
```

### Single Command Full Rebuild
```bash
make build
```

---

## Coding Standards & Python 3.14 Considerations

When contributing new build modules or modifying existing generators, follow these rules:

### Raw String Literals for Multiline Strings with LaTeX
Python 3.12+ and Python 3.14 issue `SyntaxWarning` on unrecognized escape sequences such as `\t`, `\r`, `\D`, `\a`, `\*` inside standard string literals. Because markdown dossiers frequently contain LaTeX equations (e.g., `\text{CO}_2`, `\Delta H^\circ`, `\rightleftharpoons`), **always use raw string literals (`r'''...'''` or `r"""..."""`)**:

```python
# CORRECT: Raw string literal preserves LaTeX backslashes without warnings
content = r"""
$$2\text{CO}_2 + 12\text{H}^+ + 12e^- \rightarrow \text{C}_2\text{H}_4 + 4\text{H}_2\text{O}$$
\Delta H^\circ = -128.4\text{ kJ/mol}
"""

# INCORRECT: Standard string triggers SyntaxWarning in Python 3.14
content = """
$$2\text{CO}_2 + 12\text{H}^+ + 12e^- \rightarrow \text{C}_2\text{H}_4 + 4\text{H}_2\text{O}$$
"""
```

### RFC 4180 CSV Conformance
All CSV generation must use Python's built-in `csv.writer` module with standard quoting rules and UTF-8 encoding:

```python
import csv
from pathlib import Path

def write_csv(filepath: Path, headers: list[str], rows: list[list[str]]) -> None:
    filepath.parent.mkdir(parents=True, exist_ok=True)
    with open(filepath, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)
```

### Root-Relative Path Resolution
Never use raw relative paths like `open('research/data.csv')`. Always resolve paths relative to the repository root:

```python
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_FILE = REPO_ROOT / "research" / "literature" / "MASTER_LITERATURE_MATRIX.csv"
```

---

## Automated Data Quality & Integrity Auditing

Before opening pull requests, run the automated quality checks:

```bash
# 1. Run full test suite via pytest
pytest -v

# 2. Verify all CSV files match exact column counts
make verify-csv

# 3. Check for unresolved TODO or placeholder tags
python -c "
import glob
for path in glob.glob('research/**/*.md', recursive=True):
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
        if 'TODO' in text or 'TBD' in text or 'FIXME' in text:
            print(f'[FLAGGED] Placeholder found in {path}')
print('[PASSED] Placeholder scan completed.')
"
```

---

## How to Add New Literature & Reactions

### Adding a New Benchmark Paper
1. Open [`scripts/build_literature_matrix.py`](scripts/build_literature_matrix.py).
2. Locate the benchmark data array.
3. Append a new 32-element list adhering strictly to the `headers` schema:
   - Provide an immutable `Paper_ID` (e.g., `METH-2025-SURNAME`).
   - Include an active, verified `DOI`.
   - Ensure all performance numbers (FE, conversion, yield) are verified directly against the published paper's main text or Supplementary Information.
4. Run `python3 scripts/build_literature_matrix.py` to regenerate the database.
5. Verify integrity with `pytest tests/test_csv_integrity.py`.

### Adding a New Chemical Reaction
1. Open [`scripts/build_reaction_database.py`](scripts/build_reaction_database.py).
2. Locate the reactions array.
3. Append a new reaction record with stoichiometric balance and calculated $\Delta H^\circ$, $\Delta G^\circ$, and $E^\circ$ from NIST or primary literature.
4. Run `python3 scripts/build_reaction_database.py`.
5. Verify with `pytest tests/test_reactions.py`.

---

## Git Workflow & Commit Hygiene

- **Branching:** Work on dedicated feature branches (e.g., `feature/add-formic-benchmarks`).
- **Commit Messages:** Follow Conventional Commits:
  - `feat: add 2025 solid-electrolyte benchmark to literature matrix`
  - `docs: update LCA grid threshold calculations in LCA_REVIEW.md`
  - `fix: correct typo in ammonium carbamate stoichiometric coefficients`
- **Clean Working Tree:** Never commit `.DS_Store`, OS cache files, or Python `__pycache__` directories. Run `make clean` before committing.
