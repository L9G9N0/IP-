.PHONY: help build test lint typecheck format clean verify-csv install-dev

PYTHON ?= python3
PIP ?= pip
PYTEST ?= pytest
RUFF ?= ruff
MYPY ?= mypy

help:
	@echo "CCU Evidence Engine - Developer Automation"
	@echo "=========================================="
	@echo "make build       - Deterministically rebuild all datasets and reports"
	@echo "make test        - Run automated pytest test suite"
	@echo "make verify-csv  - Check RFC 4180 column integrity across all CSVs"
	@echo "make lint        - Run ruff linter"
	@echo "make typecheck   - Run mypy static type checking"
	@echo "make format      - Auto-format code with ruff"
	@echo "make clean       - Remove cache directories, .pytest_cache, and artifacts"
	@echo "make install-dev - Install development dependencies"

install-dev:
	$(PIP) install -r requirements-dev.txt

build:
	@echo "==> [1/9] Building Master Literature Matrix..."
	@$(PYTHON) scripts/build_literature_matrix.py
	@echo "==> [2/9] Building Chemical Reaction Database..."
	@$(PYTHON) scripts/build_reaction_database.py
	@echo "==> [3/9] Building 13 Pathway Research Dossiers..."
	@$(PYTHON) scripts/build_pathway_reports.py
	@echo "==> [4/9] Building LCA & TEA Models..."
	@$(PYTHON) scripts/build_lca_tea.py
	@echo "==> [5/9] Building Cross-Pathway Tables & Figure Plans..."
	@$(PYTHON) scripts/build_tables_and_figures.py
	@echo "==> [6/9] Building Research Gaps & Novelty Analysis..."
	@$(PYTHON) scripts/build_research_gaps.py
	@echo "==> [7/9] Building Forensic Claim Register..."
	@$(PYTHON) scripts/build_claim_register.py
	@echo "==> [8/9] Building QC Registers & Consistency Audits..."
	@$(PYTHON) scripts/build_docs_and_qc.py
	@echo "==> [9/9] Compiling Full Revised Manuscript Draft..."
	@$(PYTHON) scripts/build_final_manuscript.py
	@echo "==> All datasets and dossiers regenerated successfully!"

test:
	@if command -v $(PYTEST) >/dev/null 2>&1; then \
		$(PYTEST) -v --durations=10; \
	else \
		$(PYTHON) -m unittest discover -s tests -v; \
	fi

verify-csv:
	@$(PYTHON) -m unittest tests.test_csv_integrity

lint:
	$(RUFF) check .

typecheck:
	$(MYPY) scripts/

format:
	$(RUFF) format .

clean:
	@echo "==> Cleaning caches and OS artifacts..."
	@rm -rf .pytest_cache .ruff_cache .mypy_cache build dist *.egg-info
	@find . -type d -name "__pycache__" -exec rm -rf {} +
	@find . -type f -name "*.pyc" -delete
	@find . -type f -name ".DS_Store" -delete
	@echo "==> Clean complete."
