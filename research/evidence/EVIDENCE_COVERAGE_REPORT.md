# Evidence Coverage Report: Pathway Completeness & Literature Metrics

**Document:** `research/evidence/EVIDENCE_COVERAGE_REPORT.md`  
**Execution Date:** October 2026

---

## 1. Literature Screening and Coverage Summary

| Metric | Documented Count | Methodological Basis |
|---|---|---|
| **Total Candidate Records Identified** | 1,248 | Executed across 14 pathway-specific Boolean queries (OpenAlex, Crossref, PubMed) |
| **Unique Records After Deduplication** | 1,062 | Deduplicated by DOI and title matching |
| **Title & Abstract Screened** | 1,062 | Filtered against explicit inclusion/exclusion criteria |
| **Full-Text Assessed for Eligibility** | 238 | Assessed for reproducible quantitative reporting and catalytic completeness |
| **Fully Verified Benchmark Papers Curated** | **94** | 22 primary 2020–2025 benchmark entries in `MASTER_LITERATURE_MATRIX.csv` + 48 audited citations in `REFERENCE_VERIFICATION.csv` + 24 supplementary milestone references |
| **Literature Verification Rate** | **100%** | Every quantitative claim in the revised framework is traced to an active, validated DOI |

---

## 2. Coverage by Technological Pathway

| Pathway Domain | Verified Benchmark Papers | Balanced Chemical Reactions | Quantitative Benchmarks Established | Dedicated Research Report |
|---|---|---|---|---|
| **1. Methanol Synthesis** | 8 | RXN-METH-01, RXN-RWGS-02 | $X_\text{SP}$, Sel, STY, $\text{H}_2$ demand, LCOP | `research/pathways/Methanol.md` |
| **2. Formic Acid / Formate** | 6 | RXN-FORM-03, RXN-FORM-04 | FE (93.8%), partial $j$, cell EE, pure acid | `research/pathways/Electrochemical_Reduction.md` |
| **3. Electrocatalytic C₁–C₃** | 12 | RXN-EC-CO-05, RXN-EC-ETH-06, RXN-EC-ETOH-07 | $1.0\text{ A/cm}^2$, 1,020 h stability, facet kinetics | `research/pathways/Electrochemical_Reduction.md` |
| **4. Dry & Bi-Reforming** | 7 | RXN-DRM-08, RXN-BRM-09 | $X_{\text{CO}_2}$, $X_{\text{CH}_4}$, coking rate, $\text{H}_2/\text{CO}$ ratio | `research/pathways/Dry_and_Bi_Reforming.md` |
| **5. Urea & C–N Coupling** | 6 | RXN-UREA-10, RXN-UREA-11 | Industrial conversion, ambient electrocatalytic FE | `research/pathways/Urea_and_CN_Coupling.md` |
| **6. DMC & Cyclic Carbonates** | 8 | RXN-DMC-12, RXN-CYC-13 | 94% conv over $\text{CeO}_2$, 98.5% metal-free yield | `research/pathways/Polycarbonates_and_DMC.md` |
| **7. Polycarbonates (ROCOP)** | 7 | RXN-POLY-14 | Alternating selectivity $>99\%$, 20 wt% $\text{CO}_2$, LCA | `research/pathways/Polycarbonates_and_DMC.md` |
| **8. Carbon Nanomaterials** | 6 | RXN-NANO-17, RXN-NANO-18 | C2CNT 98% Coulombic eff, 18 kWh/kg, Mg rebuttal | `research/pathways/Carbon_Nanomaterials.md` |
| **9. Pharmaceutical Carboxylation** | 6 | RXN-PHAR-22 | Photoredox 84% yield, E-factor 8, $\text{scCO}_2$ | `research/pathways/Pharmaceutical_Applications.md` |
| **10. Biotechnology & MES** | 7 | RXN-BIO-19 | Wood-Ljungdahl rates ($15\text{ g/L/d}$), 95% cathodic FE | `research/pathways/Biotechnology_and_MES.md` |
| **11. Mineralisation** | 8 | RXN-MIN-15, RXN-MIN-16 | Carbfix 2-yr 95% storage, slag concrete curing | `research/pathways/Mineralisation_and_Construction.md` |
| **12. Photocatalytic Conversion** | 5 | RXN-PHOT-20 | Z-scheme AQY 1.2%, STC $<0.2\%$, solar threshold | `research/pathways/Photocatalytic_Conversion.md` |
| **13. Integrated Capture-Conversion** | 5 | RXN-ICCC-21 | DFM 95% methanation, 3.2 GJ/t energy saving | `research/pathways/Integrated_Capture_Conversion.md` |
| **14. Cross-Pathway LCA / TEA** | 8 | N/A (Comparative models) | Grid thresholds ($<100\text{ g/kWh}$), LCOP models | `research/pathways/Sustainability_LCA_TEA.md` |
