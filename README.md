# Evidence-Based Review of Carbon Dioxide Utilisation: Literature Verification, Chemical Reaction Analysis, Research Gaps, and GitHub Documentation

**Institution:** Indraprastha Institute of Information Technology Delhi (IIIT-Delhi), New Delhi 110020, India  
**Project Lead:** Anusha Rana, Rishab Raghuvanshi, Amit Beniwal, and Durlubh Kumar Sharma  
**Repository Remote:** `https://github.com/L9G9N0/IP-.git`  
**Execution Date:** October 2026

---

## 1. Project Overview & Scientific Purpose

This repository houses the complete evidence-based research audit, literature database, balanced reaction networks, techno-economic models, and revision blueprint for the review paper:

> **“Advancements in Carbon Dioxide Utilisation: Pathways to Sustainable Chemicals, Fuels, and Materials for a Net-Zero Future”**

The goal of this initiative is to elevate the original manuscript into an authoritative, scientifically rigorous, and publishable review suitable for submission to premier peer-reviewed journals (*Chemical Reviews*, *Nature Catalysis*, *Energy & Environmental Science*).

---

## 2. Repository Structure

```text
IP-/
├── README.md                                  # Repository overview and guide
├── .licenses/                                 # OpenAlex and data licenses
├── manuscript/
│   ├── original/
│   │   ├── original_manuscript.pdf           # Preserved original 26-page manuscript PDF
│   │   └── figures/                          # Extracted figures from original manuscript
│   └── revisions/
│       └── REVISION_PLAN.md                  # Comprehensive restructuring plan for revised paper
├── research/
│   ├── audit/
│   │   ├── ORIGINAL_MANUSCRIPT_ANALYSIS.md   # Detailed audit of all 21 original sections
│   │   ├── SECTION_BY_SECTION_AUDIT.csv      # Section-by-section audit matrix
│   │   ├── INITIAL_RESEARCH_PROBLEMS.md      # Foundational scientific and thermodynamic critique
│   │   ├── PUBLICATION_RISK_REGISTER.md      # Peer-review risk analysis and mitigation actions
│   │   └── FINAL_SCIENTIFIC_CONSISTENCY_AUDIT.md # 15-point quality assurance checklist
│   ├── chemistry/
│   │   ├── REACTION_DATABASE.csv             # 22 candidate reactions with thermodynamic parameters
│   │   ├── REACTION_MECHANISM_ANALYSIS.md    # Detailed active site and intermediate kinetics
│   │   └── NEW_REACTION_CANDIDATES.md        # Profiles of 13 new-to-the-manuscript reactions
│   ├── evidence/
│   │   ├── METRIC_NORMALIZATION.md           # Mathematical guide separating FE from yield
│   │   ├── CLAIM_REGISTER.csv                # 16-point claim verification and traceability matrix
│   │   └── EVIDENCE_COVERAGE_REPORT.md       # Literature coverage and verification statistics
│   ├── figures/
│   │   ├── FIGURE_AUDIT.md                   # Critical audit of original Figures 1–5
│   │   └── FIGURE_PLANS.md                   # Code and specifications for 8 rebuilt figures
│   ├── gaps/
│   │   ├── REVIEW_LANDSCAPE_2020_2025.md     # Comparative audit of 6 recent CCU reviews
│   │   ├── RESEARCH_GAPS.md                  # Unresolved cross-pathway bottlenecks
│   │   └── REVIEW_NOVELTY_ANALYSIS.md        # Unique evidence-backed novelty statement
│   ├── lca_tea/
│   │   ├── LCA_REVIEW.md                     # System boundaries, CI thresholds, and carbon fate
│   │   ├── TEA_REVIEW.md                     # CAPEX/OPEX benchmarks and LCOP models
│   │   └── SCENARIO_COMPARISON.csv           # Cross-pathway multi-scenario comparison matrix
│   ├── literature/
│   │   ├── MASTER_LITERATURE_MATRIX.csv      # 32-column database of 22 verified benchmark papers
│   │   └── BENCHMARK_PAPER_ANALYSIS.md       # Deep technical analysis of 9 landmark papers
│   ├── methodology/
│   │   └── LITERATURE_REVIEW_PROTOCOL.md     # PRISMA-compliant reproducible search protocol
│   ├── pathways/                             # 13 dedicated pathway research reports
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
│   ├── references/
│   │   └── REFERENCE_VERIFICATION.csv        # Comprehensive audit of all 48 original citations
│   └── tables/
│       ├── TABLE_AUDIT.md                    # Critical audit of original Tables 1 & 2
│       └── CROSS_PATHWAY_TABLE.csv           # Rebuilt 13-pathway quantified comparison matrix
├── docs/
│   ├── RESEARCH_WORKFLOW.md                  # Methodological execution log
│   ├── DECISION_LOG.md                       # Traceable record of scientific decisions
│   └── CHANGELOG.md                          # Record of all generated files and changes
└── scripts/                                  # Reproducible Python build scripts
    ├── build_literature_matrix.py
    ├── build_reaction_database.py
    ├── build_pathway_reports.py
    ├── build_lca_tea.py
    ├── build_tables_and_figures.py
    ├── build_research_gaps.py
    ├── build_claim_register.py
    └── build_docs_and_qc.py
```

---

## 3. Key Research Findings & Core Contributions

1. **Thermodynamic Honesty:** Debunked the fallacy that CCU justifies burning coal. Recycling coal-plant $\text{CO}_2$ into synthetic fuels consumes 4–6 times more energy than the coal produced; CCU must be reserved for essential non-fossil chemicals and aviation fuels.
2. **Metric Normalization:** Strictly decoupled Faradaic Efficiency (FE) from single-pass conversion, proving that a 95% FE can coexist with $<10\%$ single-pass conversion and $>50\%$ carbonate crossover loss.
3. **Electrocatalytic Durability:** Documented the breakthrough 2024 Nature Energy benchmark demonstrating $>1,020\text{ hours}$ continuous ethylene electrosynthesis at 10 A in a pure-water MEA cell.
4. **Permanent Carbon Sinks:** Proved that agricultural urea releases 100% of incorporated $\text{CO}_2$ within weeks, while mineral carbonation (Carbfix / industrial slags) provides permanent storage ($>10,000$ years).
5. **Traceable Verification:** 100% of claims and reactions mapped to active, validated DOIs across the 2020–2025 primary literature.
