# Table Audit: Analysis of Existing Tables & Blueprint for Rebuilt Tables

**Document:** `research/tables/TABLE_AUDIT.md`  
**Execution Date:** October 2026

---

## 1. Audit of Original Manuscript Tables

### Table 1: "Comparative techno-economic analysis of CO₂ utilisation pathways" (Pages 7–8)
- **What it currently communicates:** Qualitative 4-row matrix comparing Hydrogenation (Methanol), Electrochemical, Mineralization, and Bioconversion across TRL, Energy Input, Carbon Permanence, Scalability, and Main Limitations.
- **Scientific Flaws & Limitations:**
  1. *Undefined Qualitative Categorization:* Energy inputs are listed vaguely as "High (H2 dependent)", "Electricity based", "Moderate", and "Low medium" with no functional units or energy numbers ($\text{MWh/t}$ or $\text{kWh/kg}$).
  2. *Excessively Broad TRL Ranges:* Lists Electrochemical as TRL 5–7. In reality, electrochemical $\text{CO}$ is TRL 7–8, while ethylene/ethanol is TRL 4–5.
  3. *Missing Major Pathways:* Omits organic carbonates, polycarbonates, dry reforming (DRM/BRM), carbon nanomaterials, and integrated capture-conversion (ICCC).
- **Recommendation:** **REPLACE** with comprehensive 13-pathway quantified cross-pathway matrix (`research/tables/CROSS_PATHWAY_TABLE.csv`).

### Table 2: "Comparison of Chemical Conversion Methods (Updated with 2024–2026 Data)" (Page 8)
- **What it currently communicates:** 3-row table comparing Hydrogenation, Electrochemical, and Dry Reforming.
- **Scientific Flaws & Critical Errors:**
  1. *Severe Misattribution:* Lists "KS-21 solvent; 88% CO₂ conversion" under Hydrogenation advances. KS-21 is an amine solvent for post-combustion capture, NOT a hydrogenation catalyst!
  2. *Typographical Error:* Lists "CO₂" as a product of electrochemical reduction (obvious typo for CO).
  3. *Unverified Pilot Claim:* Notes "Oxylus direct methanol: >80% selectivity" without specifying cell architecture, current density, or primary source citation.
- **Recommendation:** **REPLACE** with dedicated tables for Thermocatalytic, Electrocatalytic, and Reforming systems.

---

## 2. Specification of 9 Rebuilt Evidence-Based Tables

1. **Table 1: Taxonomy & Technological Readiness of All 13 CCU Pathways** (Classification, Reactants, Energy Vector, TRL, Permanence).
2. **Table 2: Thermocatalytic Hydrogenation Benchmarks** (Catalysts, T, P, Conv, Sel, Space-Time Yield, Durability).
3. **Table 3: Electrocatalytic CO₂ Reduction Benchmarks** (Product, Catalyst, Cell Architecture, FE, Current Density, Voltage, EE).
4. **Table 4: Photocatalytic Solar Fuel Benchmarks** (Semiconductor, Z-scheme, Cocatalyst, Light Source, AQY, STC Efficiency).
5. **Table 5: Mineral Carbonation & Building Materials** (Feedstock, T, P, CO₂ Uptake wt%, Compressive Strength, Permanence).
6. **Table 6: Biological & Microbial Electrosynthesis Pathways** (Organism, Metabolic Pathway, Electron Donor, Rate g/L/d, FE).
7. **Table 7: Carbon Nanomaterial Synthesis Comparison** (Magnesiothermic vs Molten Carbonate C2CNT vs CVD, Energy, LCA Balance).
8. **Table 8: Techno-Economic & Levelized Cost (LCOP) Comparison** (LCOP vs Fossil Baseline, Parity Requirements, Carbon Abatement Cost).
9. **Table 9: Life-Cycle System Boundaries, Grid Carbon Thresholds, and Carbon Permanence** (Grid threshold, Avoided emissions).
