# Local Development & Build Environment Guide

> **Document:** `DEVELOPMENT.md`  
> **Platform:** Evidence-Based CCU Research & Data Engine  
> **Status:** Canonical Developer Guide  
> **Last Updated:** October 2026  

---

## 1. Prerequisites & System Requirements

The platform is designed to be completely portable, lightweight, and executable with zero external third-party Python package installations.

### Supported Operating Systems
- **macOS:** Ventura (13.x), Sonoma (14.x), Sequoia (15.x)
- **Linux:** Ubuntu 22.04/24.04 LTS, Debian 12, RHEL 9, Arch Linux
- **Windows:** Windows 10/11 via Windows Subsystem for Linux (WSL2 recommended) or native PowerShell

### Toolchain Dependencies
- **Python:** 3.11, 3.12, 3.13, or 3.14 (Tested on Python 3.14.0)
- **Git:** Version 2.40 or newer
- **Text Editor:** VS Code, Cursor, Vim, or Emacs with Markdown and CSV extensions

---

## 2. Local Setup & Repository Initialization

Clone the official GitHub repository and navigate to the project directory:

```bash
# Clone the repository
git clone https://github.com/L9G9N0/IP-.git

# Navigate into the project root
cd IP-
```

### Python Virtual Environment (Optional)
Because all generation scripts exclusively use the Python Standard Library (`os`, `csv`, `sys`, `re`, `glob`), a virtual environment is optional. However, if you plan to run exploratory Jupyter notebooks or Pandas analytics, create an isolated virtual environment:

```bash
# Create a virtual environment
python3 -m venv .venv

# Activate the virtual environment
# On macOS / Linux:
source .venv/bin/activate
# On Windows (PowerShell):
# .venv\Scripts\Activate.ps1

# Optional analytical dependencies
pip install --upgrade pip
pip install pandas matplotlib seaborn
```

---

## 3. Build Script Execution & Pipeline Commands

All data generation scripts reside in `scripts/`. You can execute individual scripts to regenerate specific files, or run the entire pipeline via a single command:

```bash
# --- INDIVIDUAL SCRIPT EXECUTIONS ---

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

# 8. Regenerate Risk Registers, Quality Control Audits & Revision Plan
python3 scripts/build_docs_and_qc.py
```

### Complete One-Liner Pipeline Execution
```bash
python3 -c "
import subprocess, sys
scripts = [
    'scripts/build_literature_matrix.py',
    'scripts/build_reaction_database.py',
    'scripts/build_pathway_reports.py',
    'scripts/build_lca_tea.py',
    'scripts/build_tables_and_figures.py',
    'scripts/build_research_gaps.py',
    'scripts/build_claim_register.py',
    'scripts/build_docs_and_qc.py'
]
for s in scripts:
    print(f'==> Executing {s}...')
    res = subprocess.run([sys.executable, s])
    if res.returncode != 0:
        sys.exit(f'Error running {s}')
print('==> Pipeline successfully regenerated!')
"
```

---

## 4. Coding Standards & Python 3.14 Considerations

When modifying scripts or contributing new data generators, observe the following rules:

### 4.1 Raw String Literals for Multiline Strings with LaTeX
Python 3.12+ and Python 3.14 issue `SyntaxWarning` or `SyntaxError` on unrecognized escape sequences such as `\t`, `\r`, `\D`, `\a` inside standard string literals. Because markdown dossiers frequently contain LaTeX equations (e.g., `\text{CO}_2`, `\Delta H^\circ`, `\rightleftharpoons`), **always use raw string literals (`r'''...'''`)**:

```python
# CORRECT: Raw string literal preserves LaTeX backslashes without warnings
content = r'''
$$2\text{CO}_2 + 12\text{H}^+ + 12e^- \rightarrow \text{C}_2\text{H}_4 + 4\text{H}_2\text{O}$$
\Delta H^\circ = -128.4\text{ kJ/mol}
'''

# INCORRECT: Standard string triggers SyntaxWarning in Python 3.14
content = '''
$$2\text{CO}_2 + 12\text{H}^+ + 12e^- \rightarrow \text{C}_2\text{H}_4 + 4\text{H}_2\text{O}$$
'''
```

### 4.2 RFC 4180 CSV Conformance
All CSV generation must use Python's built-in `csv.writer` module with standard quoting rules (`csv.QUOTE_MINIMAL` or `csv.QUOTE_ALL`) and UTF-8 encoding:

```python
import csv

with open('output.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(rows)
```

---

## 5. Automated Data Quality & Integrity Auditing

Before submitting pull requests or making updates, run the automated linting checks:

```bash
# 1. Verify that all CSV files are valid and readable
python3 -c "
import csv, glob
for path in sorted(glob.glob('research/**/*.csv', recursive=True)):
    with open(path, 'r', encoding='utf-8') as f:
        reader = list(csv.reader(f))
        col_count = len(reader[0])
        for idx, row in enumerate(reader[1:], start=2):
            assert len(row) == col_count, f'Column mismatch in {path} at line {idx}: expected {col_count}, got {len(row)}'
        print(f'[PASSED] {path}: {len(reader)-1} rows, {col_count} columns')
"

# 2. Check for unresolved TODO or placeholder tags
python3 -c "
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

## 6. How to Add New Literature & Reactions

### Adding a New Benchmark Paper
1. Open `scripts/build_literature_matrix.py`.
2. Locate the `rows` array.
3. Append a new 32-element list adhering strictly to the `headers` schema:
   - Provide an immutable `Paper_ID` (e.g., `METH-2024-SURNAME`).
   - Include an active, verified `DOI`.
   - Ensure all performance numbers (FE, conversion, yield) are verified directly against the published paper's main text or Supplementary Information.
4. Run `python3 scripts/build_literature_matrix.py`.

### Adding a New Chemical Reaction
1. Open `scripts/build_reaction_database.py`.
2. Locate the `reactions` array.
3. Append a new 25-element list with stoichiometric balance and calculated $\Delta H^\circ$, $\Delta G^\circ$, and $E^\circ$ from NIST or primary literature.
4. Run `python3 scripts/build_reaction_database.py`.

---

## 7. Git Workflow & Commit Hygiene

- **Branching:** Work on dedicated feature branches (e.g., `feature/add-formic-benchmarks`).
- **Commit Messages:** Follow Conventional Commits:
  - `feat: add 2024 solid-electrolyte benchmark to literature matrix`
  - `docs: update LCA grid threshold calculations in LCA_REVIEW.md`
  - `fix: correct typo in ammonium carbamate stoichiometric coefficients`
- **Clean Working Tree:** Never commit `.DS_Store`, OS cache files, or Python `__pycache__` directories.
