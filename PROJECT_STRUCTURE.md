# Project Structure & File Manifest

> **Document:** `PROJECT_STRUCTURE.md`  
> **Repository:** `https://github.com/L9G9N0/IP-.git`  
> **Status:** Canonical Production Manifest  
> **Last Updated:** October 2026  

---

## Table of Contents

- [High-Level Directory Overview](#high-level-directory-overview)
- [Complete Repository Directory Tree](#complete-repository-directory-tree)
- [Root Governance & Configuration Manifest](#root-governance--configuration-manifest)
- [GitHub Enterprise Standards Manifest (`.github/`)](#github-enterprise-standards-manifest-github)
- [Algorithmic Script Layer Manifest (`scripts/`)](#algorithmic-script-layer-manifest-scripts)
- [Scientific Data Stores Manifest (`research/`)](#scientific-data-stores-manifest-research)
- [Manuscript & Academic Sources Manifest (`manuscript/`)](#manuscript--academic-sources-manifest-manuscript)
- [Automated Verification Suite Manifest (`tests/`)](#automated-verification-suite-manifest-tests)
- [Operational Records Manifest (`docs/`)](#operational-records-manifest-docs)

---

## High-Level Directory Overview

```text
IP-/
├── .github/                              # CI/CD workflows, issue templates, PR template, CODEOWNERS
├── .licenses/                            # Open-access and third-party licensing documentation
├── docs/                                 # Operational logs, decision records, research workflows
├── manuscript/                           # Baseline drafts, extracted figures, revision plan, revised draft
├── research/                             # 10 core scientific directories containing databases & dossiers
├── scripts/                              # 9 reproducible Python data generation scripts
└── tests/                                # Automated pytest test suite
```

---

## Complete Repository Directory Tree

```text
IP-/
├── .editorconfig                         # Cross-editor formatting rules (indent, charset, EOL)
├── .gitignore                            # Git untracked pattern definitions
├── .github/
│   ├── CODEOWNERS                        # Code ownership mapping
│   ├── dependabot.yml                    # Dependabot configuration for actions & pip
│   ├── discussions.md                    # GitHub Discussions configuration recommendations
│   ├── labels.yml                        # GitHub standardized labels taxonomy
│   ├── pull_request_template.md          # Comprehensive PR checklist and metadata template
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.yml                # Structured bug report form
│   │   ├── config.yml                    # Issue template chooser configuration
│   │   ├── feature_request.yml           # Feature proposal form
│   │   ├── question.yml                  # General inquiry form
│   │   └── scientific_claim_dispute.yml  # Formal empirical claim dispute form
│   └── workflows/
│       ├── ci.yml                        # Matrix CI (Python 3.11-3.13 on Linux, macOS, Windows)
│       ├── codeql.yml                    # CodeQL static application security testing
│       └── docs-lint.yml                 # Markdown linting & line-ending verification
├── .licenses/
│   └── literature_search_openalex_LICENSE.txt # OpenAlex API license note
├── API.md                                # Script execution CLI reference & CSV schema definitions
├── ARCHITECTURE.md                       # Five-tier technical architecture & mathematical models
├── CHANGELOG.md                          # Version release history following Keep a Changelog
├── CODE_OF_CONDUCT.md                    # Contributor Covenant v2.1 ethical standards
├── CONTRIBUTING.md                       # Comprehensive contributor workflows & RFC 4180 rules
├── DEPLOYMENT.md                         # Release, Zenodo DOI minting & ChemRxiv deposition procedures
├── DEVELOPMENT.md                        # Local developer setup, testing, and linting guide
├── LICENSE                               # Official MIT open-source license
├── Makefile                              # Make build, test, lint, format, and clean automation
├── PROJECT_STRUCTURE.md                  # This file; canonical repository file manifest
├── README.md                             # Flagship enterprise README portal
├── RELEASE.md                            # SemVer 2.0.0 versioning policy and release cadence
├── ROADMAP.md                            # Multi-phase research roadmap and publication milestones
├── SECURITY.md                           # Security policy, DOI immutability, and vulnerability SLA
├── SUPPORT.md                            # Support channels and institutional contacts
├── original_manuscript_text.txt          # Extracted raw text of the 26-page baseline manuscript
├── CO2_UTILIZATION_ResearchPaper_2026 (1).pdf # Original baseline research paper PDF
├── pyproject.toml                        # Modern Python project configuration (ruff, pytest, mypy)
├── requirements.txt                      # Production environment declarations (zero runtime dependencies)
├── requirements-dev.txt                  # Development dependencies (pytest, ruff, mypy)
├── docs/
│   ├── CHANGELOG.md                      # Synchronized copy of project changelog
│   ├── DECISION_LOG.md                   # Formal records for scientific decisions D-01 through D-08
│   └── RESEARCH_WORKFLOW.md              # Systematic PRISMA literature screening methodology
├── manuscript/
│   ├── original/
│   │   ├── original_manuscript.pdf       # 26-page unverified baseline PDF
│   │   └── figures/                      # 5 rasterized figures extracted from baseline paper
│   └── revisions/
│       ├── MANUSCRIPT_FINAL_RESEARCH_DRAFT.md # 488-line synthesized full review draft
│       └── REVISION_PLAN.md              # Reorganization blueprint across 13 pathways
├── research/
│   ├── audit/                            # Forensic audits, risk registers, and QC reports
│   │   ├── FINAL_CLAIM_AND_REFERENCE_AUDIT.csv # 22-claim comprehensive audit
│   │   ├── FINAL_MANUSCRIPT_QC_REPORT.md # Final quality control report
│   │   ├── FINAL_RESEARCH_GAP_CLOSURE_REPORT.md # Gap closure matrix
│   │   ├── FINAL_SCIENTIFIC_CONSISTENCY_AUDIT.md # Cross-document consistency verification
│   │   ├── INITIAL_RESEARCH_PROBLEMS.md  # 10 initial manuscript vulnerabilities
│   │   ├── ORIGINAL_MANUSCRIPT_ANALYSIS.md # Forensic analysis of baseline draft
│   │   ├── PUBLICATION_RISK_REGISTER.md  # Peer-review risk register
│   │   ├── REPOSITORY_ENGINEERING_AUDIT.md # 12-dimension technical software audit
│   │   ├── REPOSITORY_MODERNIZATION_REPORT.md # Platform modernization summary
│   │   └── SECTION_BY_SECTION_AUDIT.csv  # 21-section disposition matrix
│   ├── chemistry/                        # Chemical reaction databases & mechanisms
│   │   ├── NEW_REACTION_CANDIDATES.md    # 13 high-potential candidate reactions
│   │   ├── NEW_REACTIONS_VERIFIED.md     # In-depth mechanistic analysis of new candidates
│   │   ├── REACTION_DATABASE.csv         # Baseline 22-reaction database
│   │   ├── REACTION_DATABASE_FINAL.csv   # Comprehensive 28-reaction verified database
│   │   └── REACTION_MECHANISM_ANALYSIS.md# Surface catalyst kinetics & mechanisms
│   ├── evidence/                         # Evidence registers and normalization rules
│   │   ├── CLAIM_REGISTER.csv            # 16 audited baseline claims
│   │   ├── EVIDENCE_COVERAGE_REPORT.md   # Evidentiary coverage report
│   │   └── METRIC_NORMALIZATION.md       # Governing equations (FE, SPC, EE, STY)
│   ├── figures/                          # Vector figure blueprints and audits
│   │   ├── FIGURE_AUDIT.md               # Audit of baseline figures
│   │   └── FIGURE_PLANS.md               # Blueprints for 8 publication-grade figures
│   ├── gaps/                             # Literature gaps & novelty landscape
│   │   ├── RESEARCH_GAPS.md              # 10 documented industrial bottlenecks
│   │   ├── REVIEW_LANDSCAPE_2020_2025.md # Comparison against 6 recent reviews
│   │   └── REVIEW_NOVELTY_ANALYSIS.md    # Novelty claims matrix
│   ├── lca_tea/                          # LCA system boundaries & TEA models
│   │   ├── FINAL_LCA_TEA_ASSUMPTIONS_AND_LIMITATIONS.md # Complete boundary assumptions
│   │   ├── LCA_REVIEW.md                 # Cradle-to-grave boundary definitions
│   │   ├── SCENARIO_COMPARISON.csv       # Multi-scenario grid sensitivity matrix
│   │   └── TEA_REVIEW.md                 # Levelized cost modeling & CAPEX/OPEX
│   ├── literature/                       # Bibliometric databases & coverage
│   │   ├── BENCHMARK_PAPER_ANALYSIS.md   # Deep-dive of landmark 2020-2025 papers
│   │   ├── FINAL_LITERATURE_COVERAGE_REPORT.md # Coverage synthesis report
│   │   └── MASTER_LITERATURE_MATRIX.csv  # 32-column master benchmark matrix
│   ├── methodology/                      # PRISMA review protocol
│   │   └── LITERATURE_REVIEW_PROTOCOL.md # Systematic search queries & criteria
│   ├── pathways/                         # 13 Technological pathway reports
│   │   ├── Biotechnology_and_MES.md
│   │   ├── Carbon_Nanomaterials.md
│   │   ├── Dry_and_Bi_Reforming.md
│   │   ├── Electrochemical_Reduction.md
│   │   ├── Integrated_Capture_Conversion.md
│   │   ├── Methanol.md
│   │   ├── Mineralisation_and_Construction.md
│   │   ├── Pharmaceutical_Applications.md
│   │   ├── Photocatalytic_Conversion.md
│   │   ├── Policy_and_Market_Analysis.md
│   │   ├── Polycarbonates_and_DMC.md
│   │   ├── Sustainability_LCA_TEA.md
│   │   └── Urea_and_CN_Coupling.md
│   ├── references/                       # Citation verification registers
│   │   └── REFERENCE_VERIFICATION.csv    # 48 audited baseline citations
│   └── tables/                           # Cross-pathway matrices & audits
│       ├── CROSS_PATHWAY_TABLE.csv       # 13-pathway quantified comparison
│       ├── FINAL_CROSS_PATHWAY_COMPARISON.csv # Expanded cross-pathway matrix
│       └── TABLE_AUDIT.md                # Rebuilt table specifications
├── scripts/                              # Reproducible Python generation modules
│   ├── build_claim_register.py           # Generates CLAIM_REGISTER.csv
│   ├── build_docs_and_qc.py              # Generates risk registers & QC reports
│   ├── build_final_manuscript.py         # Compiles MANUSCRIPT_FINAL_RESEARCH_DRAFT.md
│   ├── build_lca_tea.py                  # Generates LCA/TEA scenarios & reviews
│   ├── build_literature_matrix.py        # Generates MASTER_LITERATURE_MATRIX.csv
│   ├── build_pathway_reports.py          # Generates 13 pathway dossiers
│   ├── build_reaction_database.py        # Generates REACTION_DATABASE_FINAL.csv
│   ├── build_research_gaps.py            # Generates research gap & novelty reports
│   └── build_tables_and_figures.py       # Generates cross-pathway tables & figure plans
└── tests/                                # Automated test suite
    ├── __init__.py                       # Test package initializer
    ├── test_csv_integrity.py             # Validates RFC 4180 conformance and column counts
    ├── test_docs.py                      # Validates markdown files and heading structure
    ├── test_reactions.py                 # Validates chemical stoichiometry and thermodynamics
    └── test_scripts.py                   # Validates CLI flags and script idempotency
```

---

## Root Governance & Configuration Manifest

| File | Purpose | Format |
|---|---|---|
| `README.md` | Flagship project portal containing architecture, ASCII diagrams, data flows, and setup instructions. | CommonMark |
| `LICENSE` | MIT License granting open-source distribution and use permissions. | Plain Text |
| `CHANGELOG.md` | Canonical changelog tracking releases and historical changes according to Keep a Changelog. | CommonMark |
| `CONTRIBUTING.md` | Guidelines for academic and open-source contributors, detailing PR workflows and DOI standards. | CommonMark |
| `CODE_OF_CONDUCT.md` | Community code of conduct adapted from Contributor Covenant v2.1. | CommonMark |
| `SECURITY.md` | Security policy detailing scientific data integrity, DOI immutability, and reporting timelines. | CommonMark |
| `SUPPORT.md` | Support channels, triage workflows, and institutional contact information. | CommonMark |
| `ROADMAP.md` | Research and engineering roadmap detailing completed and upcoming publication milestones. | CommonMark |
| `ARCHITECTURE.md` | Multi-tier architectural specifications, data flow diagrams, and mathematical normalization engines. | CommonMark |
| `API.md` | Programmatic Python API and CLI script execution reference. | CommonMark |
| `PROJECT_STRUCTURE.md` | This document; complete repository structure and file taxonomy. | CommonMark |
| `DEVELOPMENT.md` | Developer setup guide with toolchain prerequisites, build commands, and testing instructions. | CommonMark |
| `DEPLOYMENT.md` | Archiving procedures for Zenodo, ChemRxiv preprint deposition, and versioning. | CommonMark |
| `RELEASE.md` | Release management policy, SemVer 2.0.0 guidelines, and release checklist. | CommonMark |
| `Makefile` | POSIX make automation for building, testing, linting, and formatting. | Makefile |
| `pyproject.toml` | Standardized Python project configuration for Ruff, Pytest, and Mypy. | TOML |
| `requirements.txt` | Production environment declaration (zero third-party runtime dependencies). | Requirements |
| `requirements-dev.txt` | Development dependencies for local testing, linting, and typing. | Requirements |
| `.editorconfig` | Cross-editor indentation, newline, and charset settings. | INI |
