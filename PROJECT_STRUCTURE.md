# Project Structure & File Manifest

> **Document:** `PROJECT_STRUCTURE.md`  
> **Repository:** `https://github.com/L9G9N0/IP-.git`  
> **Status:** Canonical Production Manifest  
> **Last Updated:** October 2026  

---

## 1. High-Level Directory Overview

```text
IP-/
├── [Root Documentation & Governance]     # Master guides, architecture, API, security, lifecycle
├── .licenses/                            # Open-access and API licensing documentation
├── docs/                                 # Operational logs, decision records, research workflows
├── manuscript/                           # Baseline drafts, extracted figures, revision plan
├── research/                             # 10 core research directories containing databases & dossiers
└── scripts/                              # 8 reproducible Python data generation scripts
```

---

## 2. Comprehensive File-by-File Manifest

### 2.1 Root Documentation & Governance Files
| File Name | Purpose & Contents | Format |
|---|---|---|
| `README.md` | Master project portal featuring visual Mermaid diagrams, problem statement, executive summary, engineering journey, milestones, and dataset showcases. | CommonMark |
| `ARCHITECTURE.md` | In-depth technical architecture describing the multi-tier data engine, metric normalization algorithms, LCA boundaries, and relational database schemas. | CommonMark |
| `API.md` | Technical specifications for the 8 data generation scripts in `scripts/`, command-line execution parameters, schema definitions, and programmatic query recipes (Python/R). | CommonMark |
| `PROJECT_STRUCTURE.md` | This document; complete file-by-file directory tree explaining the purpose and scope of every file in the repository. | CommonMark |
| `DEVELOPMENT.md` | Guide for local setup, Python 3.14 execution, virtual environments, RFC-4180 CSV validation, and script modification guidelines. | CommonMark |
| `DEPLOYMENT.md` | Operational release pipeline detailing publication workflows, Overleaf/LaTeX synchronization, preprint submission, Zenodo archiving, and versioning. | CommonMark |
| `SECURITY.md` | Academic integrity and security framework covering DOI immutability, data provenance, tamper resistance, and credential isolation. | CommonMark |
| `ROADMAP.md` | Comprehensive milestone tracker documenting completed audit phases (Phases 0–12) and forward-looking publication phases (Phases 13–15). | CommonMark |
| `CONTRIBUTING.md` | Contribution guidelines for academic and open-science collaborators, including commit message conventions, PR review standards, and data verification protocols. | CommonMark |
| `SUPPORT.md` | Support channels, institutional points of contact at IIIT-Delhi, bug reporting, and academic data citation guidelines. | CommonMark |
| `CODE_OF_CONDUCT.md` | Scientific integrity and academic ethical guidelines adapted from the Contributor Covenant 2.1. | CommonMark |
| `RELEASE.md` | Formal release notes for `v1.0.0-audit`, summarizing the completed research audit, evidence databases, and revision framework. | CommonMark |
| `.gitignore` | Standard Git ignore file specifying exclusions (`.DS_Store`, `__pycache__`, temporary build artifacts). | Plain Text |
| `CO2_UTILIZATION_ResearchPaper_2026 (1).pdf` | Canonical archive of the original 26-page unrevised draft manuscript. | Binary (PDF) |
| `original_manuscript_text.txt` | Complete line-numbered raw text extracted from the baseline PDF (804 lines) for automated text processing and audit reference. | UTF-8 Text |

---

### 2.2 `.licenses/`
| File Name | Purpose & Contents |
|---|---|
| `literature_search_openalex_LICENSE.txt` | Attribution and Open Data Commons (ODC-BY) licensing notice for OpenAlex bibliometric API data integration. |

---

### 2.3 `manuscript/` (Manuscript Drafting & Assets)
```text
manuscript/
├── original/
│   ├── original_manuscript.pdf           # Canonical duplicate of the baseline PDF
│   └── figures/
│       ├── page_6_img_1_22.png           # Original Figure 1 bitmap (Carbon cycle schematic)
│       ├── page_10_img_2_33.png          # Original Figure 2 bitmap (Formate reaction mechanism)
│       ├── page_13_img_3_41.jpeg         # Original Figure 3 bitmap (Electrochemical cell setup)
│       ├── page_13_img_4_42.png          # Original Figure 4 bitmap (Overpotential stability plot)
│       └── page_20_img_5_60.png          # Original Figure 5 bitmap (Cost breakdown chart)
└── revisions/
    └── REVISION_PLAN.md                  # Comprehensive 21-section blueprint detailing exact restructuring, text deletions, and new paragraph drafts.
```

---

### 2.4 `research/` (Core Research Datasets & Synthesis Dossiers)

#### `research/audit/` (Manuscript & Code Audits)
- `ORIGINAL_MANUSCRIPT_ANALYSIS.md`: Rigorous section-by-section audit of all 21 original manuscript sections documenting what the text says, scientific flaws, and necessary actions.
- `SECTION_BY_SECTION_AUDIT.csv`: Tabular 21-row matrix assigning disposition statuses (`KEEP`, `UPDATE`, `REWRITE`, `MERGE`, `MOVE`, `VERIFY`, `REMOVE`).
- `INITIAL_RESEARCH_PROBLEMS.md`: Foundational critique exposing the pro-coal thermodynamic fallacy, KS-21 solvent misattribution, and uncredited figures.
- `PUBLICATION_RISK_REGISTER.md`: 10 fatal peer-review vulnerabilities identified in the baseline draft with corresponding executed mitigation protocols.
- `FINAL_SCIENTIFIC_CONSISTENCY_AUDIT.md`: 15-point verification checklist evaluating thermodynamic consistency, mass balances, and citation traceability.
- `REPOSITORY_ENGINEERING_AUDIT.md`: 12-dimension technical audit evaluating repository engineering rigor.
- `REPOSITORY_MODERNIZATION_REPORT.md`: Comprehensive modernization report summarizing repository transition from raw draft to enterprise data engine.

#### `research/chemistry/` (Reactions, Thermodynamics & Kinetics)
- `REACTION_DATABASE.csv`: 25-column database of 22 balanced candidate reactions with calculated $\Delta H^\circ$, $\Delta G^\circ$, standard reduction potentials ($E^\circ$), and active sites.
- `REACTION_MECHANISM_ANALYSIS.md`: Detailed chemical kinetics and intermediate surface analysis (e.g., oxygen-vacancy formate pathway vs stepped Cu(100) C–C coupling).
- `NEW_REACTION_CANDIDATES.md`: Technical dossiers for 13 new-to-the-manuscript high-potential reactions (e.g., molten salt CNT synthesis, ethylene eCO₂R, tandem DMC synthesis).

#### `research/evidence/` (Claims & Metric Normalization)
- `CLAIM_REGISTER.csv`: 12-column matrix tracking 16 core claims from the original draft, auditing evidence sources, conflict status, and required revisions.
- `METRIC_NORMALIZATION.md`: Mathematical formulation guide strictly decoupling Faradaic efficiency from single-pass conversion, carbonate crossover, and energy efficiency.
- `EVIDENCE_COVERAGE_REPORT.md`: Quantitative report documenting PRISMA screening metrics, deduplication statistics, and 100% DOI verification rates.

#### `research/figures/` (Visual Blueprints)
- `FIGURE_AUDIT.md`: Forensic audit of original Figures 1–5 detailing copyright/provenance risks, resolution issues, and scientific shortcomings.
- `FIGURE_PLANS.md`: High-resolution specifications and Matplotlib/Seaborn visualization scripts for 8 rebuilt publication figures.

#### `research/gaps/` (Novelty & Competitive Review Landscape)
- `REVIEW_LANDSCAPE_2020_2025.md`: Critical audit of 6 recent published reviews in *Chem. Rev.*, *Nat. Clim. Change*, and *J. CO2 Util.*, establishing specific gaps.
- `RESEARCH_GAPS.md`: Deep dive into 10 unresolved industrial CCU bottlenecks (carbonate crossover, hydrogen footprint, electrode scaling, catalyst coking).
- `REVIEW_NOVELTY_ANALYSIS.md`: Explicit 7-point novelty statement establishing the unique scientific contributions of our revised review.

#### `research/lca_tea/` (Life-Cycle & Techno-Economics)
- `LCA_REVIEW.md`: Cradle-to-grave LCA review covering system boundaries, electricity carbon intensity thresholds ($CI_{\text{grid}}$), and carbon permanence.
- `TEA_REVIEW.md`: Techno-economic review modeling CAPEX, OPEX, electricity sensitivity curves, and Levelized Cost of Product (LCOP) vs. fossil parity.
- `SCENARIO_COMPARISON.csv`: Multi-scenario matrix comparing emissions and costs across fossil baseline, 100% renewable electricity, and current national grid averages.

#### `research/literature/` (Bibliometrics & Primary Literature)
- `MASTER_LITERATURE_MATRIX.csv`: 32-column database cataloging 22 landmark primary benchmark papers published between 2020 and 2025.
- `BENCHMARK_PAPER_ANALYSIS.md`: Exhaustive technical dissection of 9 landmark papers (*Science*, *Nature Energy*, *JACS*, *Nature Catalysis*).

#### `research/methodology/` (Search Protocols)
- `LITERATURE_REVIEW_PROTOCOL.md`: PRISMA-compliant reproducible literature search protocol detailing Boolean queries, database sources, and inclusion/exclusion criteria.

#### `research/pathways/` (13 Dedicated Pathway Dossiers)
- `Methanol.md`: Thermocatalytic hydrogenation, $\text{In}_2\text{O}_3/\text{ZrO}_2$ vacancy mechanics, commercial plant data (CRI Iceland, Shunli China).
- `Urea_and_CN_Coupling.md`: Ammonium carbamate equilibria, Basaroff process kinetics, carbon fate analysis (100% re-release in 7–28 days).
- `Electrochemical_Reduction.md`: Zero-gap MEA electrosynthesis of $\text{CO}$, $\text{HCOOH}$, $\text{C}_2\text{H}_4$, and carbonate crossover dynamics.
- `Photocatalytic_Conversion.md`: Semiconductor Z-scheme photocatalysis, apparent quantum yield (AQY), and solar-to-chemical (STC) limitations.
- `Dry_and_Bi_Reforming.md`: Dry ($\text{CO}_2+\text{CH}_4$) and bi-reforming, coke suppression mechanisms, and industrial CALCOR/SPARG processes.
- `Polycarbonates_and_DMC.md`: Direct DMC synthesis with in-situ dehydrants, ring-opening copolymerization of epoxides into PPC and polyols.
- `Carbon_Nanomaterials.md`: Debunking magnesiothermic combustion soot; high-temperature molten carbonate electrolysis (C2CNT) to pristine CNTs.
- `Pharmaceutical_Applications.md`: Visible-light photoredox C–H carboxylation, flow chemistry, and active pharmaceutical ingredient (API) synthesis.
- `Biotechnology_and_MES.md`: Acetogenic gas fermentation (LanzaTech *C. autoethanogenum*), microbial electrosynthesis (MES), and mass transfer limits.
- `Mineralisation_and_Construction.md`: Ex-situ slag/fly-ash carbonation, in-situ basalt injection (Carbfix), and permanent thermodynamic trapping ($>10,000$ yrs).
- `Integrated_Capture_Conversion.md`: Dual-function materials (DFMs) integrating alkali capture with Ru/Ni isothermal hydrogenation.
- `Sustainability_LCA_TEA.md`: Synthesis of cross-pathway carbon abatement costs and global electricity consumption demands.
- `Policy_and_Market_Analysis.md`: Regulatory drivers (EU RED II, US IRA 45Q/45V), carbon border adjustments (CBAM), and verifiable market sizing.

#### `research/references/` (Citation Audits)
- `REFERENCE_VERIFICATION.csv`: Comprehensive audit of all 48 citations in the baseline draft, identifying 8 off-topic citations, DOI errors, and publication dates.

#### `research/tables/` (Rebuilt Tables)
- `TABLE_AUDIT.md`: Critical audit of baseline Tables 1 and 2, defining the blueprint for 9 rebuilt high-density tables.
- `CROSS_PATHWAY_TABLE.csv`: 14-column comparison matrix harmonizing all 13 CCU pathways across reactants, energy vector, TRL, rate metrics, and commercial status.

---

### 2.5 `docs/` (Workflow Logs & Decision Records)
- `RESEARCH_WORKFLOW.md`: Methodological timeline documenting the exact sequence of research and code execution.
- `DECISION_LOG.md`: Traceable record of key scientific decisions (e.g., purge of pro-coal advocacy, correction of KS-21 solvent, speciation of formic acid vs formate).
- `CHANGELOG.md`: Chronological log of all commits and generated files in the repository.

---

### 2.6 `scripts/` (Automated Build Engine)
- `build_literature_matrix.py`: Compiles `MASTER_LITERATURE_MATRIX.csv`.
- `build_reaction_database.py`: Compiles `REACTION_DATABASE.csv`, `REACTION_MECHANISM_ANALYSIS.md`, and `NEW_REACTION_CANDIDATES.md`.
- `build_pathway_reports.py`: Compiles all 13 research reports in `research/pathways/`.
- `build_lca_tea.py`: Compiles `LCA_REVIEW.md`, `TEA_REVIEW.md`, and `SCENARIO_COMPARISON.csv`.
- `build_tables_and_figures.py`: Compiles `TABLE_AUDIT.md`, `CROSS_PATHWAY_TABLE.csv`, `FIGURE_AUDIT.md`, and `FIGURE_PLANS.md`.
- `build_research_gaps.py`: Compiles `REVIEW_LANDSCAPE_2020_2025.md`, `RESEARCH_GAPS.md`, and `REVIEW_NOVELTY_ANALYSIS.md`.
- `build_claim_register.py`: Compiles `CLAIM_REGISTER.csv`.
- `build_docs_and_qc.py`: Compiles `PUBLICATION_RISK_REGISTER.md`, `EVIDENCE_COVERAGE_REPORT.md`, `FINAL_SCIENTIFIC_CONSISTENCY_AUDIT.md`, `REVISION_PLAN.md`, `DECISION_LOG.md`, `CHANGELOG.md`, and `RESEARCH_WORKFLOW.md`.
