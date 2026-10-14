# Figure Audit: Critical Evaluation of Existing Figures & Rebuilding Blueprint

**Document:** `research/figures/FIGURE_AUDIT.md`  
**Execution Date:** October 2026

---

## 1. Audit of Original Manuscript Figures

### Figure 1: "Classification of CO₂ utilisation pathways" (Page 6)
- **Original Content:** Simplistic box diagram dividing CCU into chemical, biological, and mineralisation.
- **Scientific Flaws:**
  1. Conflates physical processes with chemical transformation.
  2. Duplicates labels; fails to include modern post-2020 pathways (electrocatalytic reduction, reactive capture/DFMs, chemical looping).
  3. Lacks thermodynamic categorization (downhill exergonic vs uphill endergonic).
- **Recommendation:** **REPLACE** with comprehensive Figure 1 (Source-to-Product-to-Carbon-Fate Architecture).

### Figure 2: "Industrial CO₂-to-methanol production process" (Pages 9–10)
- **Original Content:** Generic box flow diagram of methanol synthesis.
- **Scientific Flaws:**
  1. Shows only forward hydrogenation, omitting competing RWGS reaction and gas recycling loop.
  2. Fails to show water separation and downstream two-column distillation.
  3. Ignores hydrogen production electrolyzer interface and electricity penalty.
- **Recommendation:** **REPLACE** with Figure 3 (Complete Reaction Network & Process Flowsheet).

### Figure 3: "Schematic representation of CO₂ conversion into graphene using Mg/Ni catalysts..." (Page 12)
- **Original Content:** Schematic claiming clean production of graphene from solid CO₂ burning with Mg ribbon, followed by nanocomposite blending.
- **Scientific Flaws:**
  1. Severe scientific exaggeration: portrays violent, soot-producing magnesiothermic combustion as a selective, pristine graphene manufacturing process.
  2. Conceals toxic acid leaching ($\text{HCl/HF}$) required to dissolve $\text{MgO}$.
  3. Ignores upstream $\text{Mg}$ manufacturing emissions (+30–50 kg $\text{CO}_2$/kg carbon).
- **Recommendation:** **REPLACE** with Figure 7 (Comparative Carbon Nanomaterial Synthesis: Magnesiothermic vs Molten Carbonate C2CNT).

### Figure 4: "Pharmaceutical uses of CO₂" (Page 13)
- **Original Content:** Circular diagram listing extraction, sterilization, and chemical synthesis.
- **Scientific Flaws:**
  1. Blends physical solvent behavior with chemical bond-forming transformations without distinction.
  2. Contains outdated Grignard chemistry rather than modern photoredox catalytic carboxylation.
- **Recommendation:** **REPLACE** with Figure 5 (Pharmaceutical Touchpoints: Catalytic Carboxylation vs Supercritical Processing).

### Figure 5: "Life-Cycle Carbon Analysis: Case 1, 2, 3" (Pages 19–20)
- **Original Content:** Bar chart showing Grey H₂ vs Green H₂ methanol emissions.
- **Scientific Flaws:**
  1. Concept is sound (identifies positive emissions of grey H₂), but lacks quantified axis values, system boundaries, and sensitivity to grid carbon intensity.
- **Recommendation:** **UPGRADE** to Figure 8 (Parametric LCA System Boundaries & Grid Intensity Thresholds).

---

## 2. Specification of 8 Rebuilt Publication-Grade Figures

1. **Figure 1:** Overall CO₂ Source-to-Product-to-Carbon-Fate Architecture (Mermaid & SVG specification).
2. **Figure 2:** Thermodynamic and Kinetic Landscape of CO₂ Activation (Downhill exergonic vs uphill endergonic free energy profiles).
3. **Figure 3:** Methanol Synthesis Reaction Network, Active Site Geometry, and Competing RWGS Dynamics.
4. **Figure 4:** Electrochemical CO₂ Reduction Product Pathways & Intermediate Bifurcation on Cu Facets.
5. **Figure 5:** Integrated Capture and Conversion (ICCC) via Dual-Function Materials.
6. **Figure 6:** Mineral Carbonation Mechanisms: In-Situ Basalt Trapping vs Ex-Situ Industrial Slag Curing.
7. **Figure 7:** Carbon Retention Durability and End-of-Life Sinks Across All Product Classes.
8. **Figure 8:** Cradle-to-Grave LCA System Boundaries & Sensitivity to Grid Carbon Intensity ($CI_\text{grid}$).
