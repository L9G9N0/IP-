# Release Notes: v1.0.0-audit

> **Release Tag:** `v1.0.0-audit`  
> **Release Name:** Canonical Scientific Audit, Evidence Database & Revision Architecture  
> **Institution:** Indraprastha Institute of Information Technology Delhi (IIIT-Delhi)  
> **Release Date:** October 2026  
> **Git Remote:** `https://github.com/L9G9N0/IP-.git`  

---

## 1. Executive Summary

We are pleased to announce the formal release of **v1.0.0-audit** of the Carbon Dioxide Utilisation (CCU) Evidence Engine & Research Review Platform. 

This release marks the successful completion of **Phases 0 through 12** of our scientific overhaul of the review manuscript:
> *“Advancements in Carbon Dioxide Utilisation: Pathways to Sustainable Chemicals, Fuels, and Materials for a Net-Zero Future”*

Through this release, the project transitions from an unverified 26-page working paper into an enterprise-grade, reproducible scientific data engine ready for full LaTeX manuscript drafting and submission to leading peer-reviewed journals (*Chemical Reviews*, *Nature Catalysis*, *Energy & Environmental Science*).

---

## 2. Key Deliverables & Research Achievements

### 2.1 Complete Forensic Audit of Baseline Manuscript
- Audited all 21 sections of the original draft (`research/audit/ORIGINAL_MANUSCRIPT_ANALYSIS.md`).
- Established 21-row disposition matrix (`SECTION_BY_SECTION_AUDIT.csv`).
- Identified and mitigated 10 fatal peer-review vulnerabilities (`PUBLICATION_RISK_REGISTER.md`), including:
  - Complete elimination of pro-coal advocacy claims.
  - Reassignment of KS-21 solvent from hydrogenation to capture technologies.
  - Correction of ammonium carbamate formula to $\text{NH}_2\text{COONH}_4$.
  - Debunking magnesiothermic soot and replacing it with molten carbonate CNT electrosynthesis.
  - Removal of 8 off-topic citations on coal bioleaching and fruit fermentation.

### 2.2 Relational Literature & Reaction Databases
- **Master Literature Matrix (`research/literature/MASTER_LITERATURE_MATRIX.csv`):** 32 standardized columns capturing 22 primary 2020–2025 research benchmarks with 100% verified DOIs.
- **Reaction Database (`research/chemistry/REACTION_DATABASE.csv`):** 25 columns covering 22 balanced candidate reactions with standard enthalpy ($\Delta H^\circ$), Gibbs energy ($\Delta G^\circ$), standard reduction potentials ($E^\circ$), and active-site mechanisms.
- **Reference Verification Matrix (`research/references/REFERENCE_VERIFICATION.csv`):** Comprehensive audit of all 48 baseline citations.
- **Cross-Pathway Comparison Table (`research/tables/CROSS_PATHWAY_TABLE.csv`):** Harmonized comparison of 13 CCU pathways across reactants, energy vectors, TRL, rate metrics, and commercial pilot status.
- **Claim Register (`research/evidence/CLAIM_REGISTER.csv`):** 16-point traceability matrix tracking baseline manuscript claims against empirical literature.

### 2.3 Synthesis Dossiers & Visual Blueprints
- **13 Pathway Research Reports (`research/pathways/*.md`):** Deep dives covering thermocatalytic hydrogenation, eCO₂R, photocatalysis, dry/bi-reforming, DMC, polycarbonates, carbon nanomaterials, pharma, biotechnology/MES, mineralisation, ICCC, sustainability, and policy.
- **Metric Normalization (`research/evidence/METRIC_NORMALIZATION.md`):** Mathematical guide strictly decoupling Faradaic efficiency from single-pass conversion, carbonate crossover, and energy efficiency.
- **LCA & TEA Models (`research/lca_tea/`):** Cradle-to-grave boundary models establishing grid carbon intensity break-even thresholds ($CI_{\text{grid}} < 120\text{ g/kWh}$) and LCOP sensitivity matrices.
- **Figure Specifications (`research/figures/FIGURE_PLANS.md`):** Production plans and Python Matplotlib scripts for 8 publication-grade vector figures to replace the 5 baseline bitmaps.
- **Master Revision Blueprint (`manuscript/revisions/REVISION_PLAN.md`):** Comprehensive 21-section blueprint guiding the forthcoming LaTeX rewrite.

### 2.4 Automated Python Build Engine
- 8 idempotent Python scripts in `scripts/` allowing deterministic byte-for-byte regeneration of all datasets and dossiers.
- Zero external runtime dependencies; 100% compliant with Python 3.11, 3.12, 3.13, and 3.14.

---

## 3. Breaking Changes & Scientific Corrections

| Component | Baseline Manuscript State | v1.0.0-audit Corrected State | Impact |
|---|---|---|---|
| **Climate Role of CCU** | Claimed CCU enables continued coal combustion and avoids renewables | Purged; reframed strictly as circular carbon management for hard-to-electrify chemicals/aviation | Prevents immediate desk rejection |
| **KS-21 Attribution** | Listed as a hydrogenation catalyst with 88% conversion | Reassigned to Section 5 under solvent absorption capture (MHI amine) | Eliminates domain error |
| **Formic Acid Speciation** | Conflated formic acid (HCOOH) with formate salts (HCOO⁻) | Separated; featured solid-state electrolyte cell producing 20 wt% pure liquid acid | Eliminates salt waste issue |
| **Graphene Synthesis** | Claimed burning Mg in CO₂ yields pristine graphene | Debunked soot/defects; featured molten salt C2CNT process (98% CE) | Scientific rigor |
| **Electrochemical Table** | Listed CO₂ as an electrochemical reduction product | Corrected typo to Carbon Monoxide (CO) | Editorial quality |
| **Market Valuation** | Stated CCU market as USD 6.45 million in 2026 | Corrected unit typo to USD 6.45 billion | Market data provenance |

---

## 4. Verification & Testing Summary

All generated datasets have been audited and verified:
- **RFC 4180 CSV Conformance:** 100% passed across all 6 CSV matrices.
- **DOI Verification:** 100% of claims and reactions link to active, validated DOIs.
- **Thermodynamic Consistency:** 100% of chemical reactions are stoichiometrically balanced and thermodynamically classified.
- **Git State:** Synchronized with remote `origin/main` at commit `e06eeb1`.

---

## 5. Next Steps

With the audit and data engine finalized, the research team is initiating **Phase 13 (Overleaf LaTeX Manuscript Drafting)** and **Phase 14 (High-Resolution Vector Graphic Compilation)** leading to journal submission in late 2026.
