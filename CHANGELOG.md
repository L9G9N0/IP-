# Changelog

All notable changes to the Carbon Dioxide Utilisation (CCU) Evidence Engine & Research Platform will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

### Added
- Enterprise GitHub configuration: issue templates, pull request template, CODEOWNERS, and CI/CD workflows.
- Root configuration and packaging files: `pyproject.toml`, `requirements.txt`, `requirements-dev.txt`, `Makefile`, `.editorconfig`.
- Automated test suite in `tests/` covering CSV RFC 4180 integrity, thermodynamic state functions, script idempotency, and markdown structure.
- Modular CLI arguments (`argparse`), type annotations, and `if __name__ == '__main__':` entry points across all 9 data generation scripts.

### Fixed
- Fixed column count mismatch in `research/audit/FINAL_CLAIM_AND_REFERENCE_AUDIT.csv` on row 9 (`CLM-08`).
- Fixed Python 3.14 invalid escape sequence syntax warning in `scripts/build_final_manuscript.py`.
- Fixed Mermaid diagram rendering error in `ROADMAP.md` by replacing unsupported `gantt` syntax with standard `flowchart LR`.
- Removed destructive script overwrite of root `README.md` from `scripts/build_docs_and_qc.py`.

---

## [1.2.0] - 2026-10-19

### Added
- Final comprehensive revised manuscript draft (`manuscript/revisions/MANUSCRIPT_FINAL_RESEARCH_DRAFT.md`, 488 lines).
- Final verified chemical reaction database (`research/chemistry/REACTION_DATABASE_FINAL.csv`, 28 balanced reactions).
- Final cross-pathway comparison matrix (`research/tables/FINAL_CROSS_PATHWAY_COMPARISON.csv`, 13 pathways).
- Final research gap closure report (`research/audit/FINAL_RESEARCH_GAP_CLOSURE_REPORT.md`).
- Final LCA/TEA assumptions and limitations dossier (`research/lca_tea/FINAL_LCA_TEA_ASSUMPTIONS_AND_LIMITATIONS.md`).
- Final literature coverage report (`research/literature/FINAL_LITERATURE_COVERAGE_REPORT.md`).
- Final manuscript quality control report (`research/audit/FINAL_MANUSCRIPT_QC_REPORT.md`).
- Script `scripts/build_final_manuscript.py` to deterministically compile the revised manuscript.

---

## [1.1.0] - 2026-10-14

### Added
- Enterprise documentation suite: `ARCHITECTURE.md`, `API.md`, `PROJECT_STRUCTURE.md`, `DEVELOPMENT.md`, `DEPLOYMENT.md`, `SECURITY.md`, `SUPPORT.md`, `RELEASE.md`, `ROADMAP.md`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`.
- Expanded production `README.md` to 646 lines with detailed technical sections.
- Repository engineering audit (`research/audit/REPOSITORY_ENGINEERING_AUDIT.md`) scoring 96/100.
- Repository modernization report (`research/audit/REPOSITORY_MODERNIZATION_REPORT.md`).

---

## [1.0.0] - 2026-10-14

### Added
- Initial evidence-based scientific audit of baseline draft (`CO2_UTILIZATION_ResearchPaper_2026 (1).pdf`).
- Master Literature Matrix (`research/literature/MASTER_LITERATURE_MATRIX.csv`, 22 benchmark papers, 32 columns).
- Thermodynamically balanced reaction database (`research/chemistry/REACTION_DATABASE.csv`, 22 reactions, 25 columns).
- 13 technological pathway research dossiers in `research/pathways/`.
- Life-cycle assessment and techno-economic models in `research/lca_tea/`.
- Scientific claim audit register (`research/evidence/CLAIM_REGISTER.csv`, 16 claims).
- Section-by-section audit register (`research/audit/SECTION_BY_SECTION_AUDIT.csv`, 21 sections).
- Baseline manuscript text extraction (`original_manuscript_text.txt`).
- Decision log (`docs/DECISION_LOG.md`) documenting decisions D-01 through D-08.
- Systematic research workflow protocol (`docs/RESEARCH_WORKFLOW.md`).
