"""Cross-Pathway Tables and Figure Blueprints Generator for CCU Evidence Engine.

Generates:
- research/tables/TABLE_AUDIT.md
- research/tables/CROSS_PATHWAY_TABLE.csv
- research/figures/FIGURE_AUDIT.md
- research/figures/FIGURE_PLANS.md
"""

from __future__ import annotations

import argparse
import csv
from pathlib import Path
from typing import Sequence

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_TABLES_DIR = REPO_ROOT / "research" / "tables"
DEFAULT_FIGURES_DIR = REPO_ROOT / "research" / "figures"

CROSS_HEADERS: list[str] = [
    'Pathway_ID', 'Pathway_Name', 'Target_Product', 'Primary_Reactants', 'Energy_Vector',
    'Catalytic_or_Biological_System', 'Operating_Conditions', 'Key_Rate_Metric',
    'Selectivity_or_FE', 'Single_Pass_Conversion_pct', 'Energy_Intensity',
    'Carbon_Permanence', 'Current_TRL', 'Commercial_Facilities_or_Pilots'
]

CROSS_ROWS: list[list[str]] = [
    ['P01', 'Thermocatalytic Hydrogenation', 'Methanol (CH3OH)', 'CO2 + H2', 'Thermal Heat + Green H2', 'In2O3/ZrO2 or Cu/ZnO/Al2O3', '250-300 °C, 5.0 MPa', '0.45-0.62 g/g_cat/h', '86-100% Sel', '8.5-15.2%', '10.5 MWh/t MeOH', '< 6 months (Fuel)', '8-9', 'CRI Iceland (4 ktpa), Shunli China (110 ktpa)'],
    ['P02', 'Solid-Electrolyte eCO2R', 'Pure Formic Acid (HCOOH)', 'CO2 + H2O', 'Renewable Electricity', 'Bi nanosheets in solid electrolyte', '25 °C, 1 atm, 2.8 V', '188 mA/cm² partial j', '93.8% FE', '32.0%', '4.2 kWh/kg HCOOH', '1-5 years (Chemical)', '6-7', 'Multi-kW pilot cells (Wang group, Twelve)'],
    ['P03', 'Zero-Gap MEA eCO2R', 'Carbon Monoxide (CO)', 'CO2 + H2O', 'Renewable Electricity', 'Ag nanoparticles or Ni-N-C', '25-50 °C, 1.2 atm, 2.5 V', '300-500 mA/cm²', '>95.0% FE', '35-50%', '6.5 kWh/kg CO', '< 6 months (Syngas)', '7-8', 'Twelve (OPUS cell), Siemens Energy'],
    ['P04', 'Pure-Water MEA eCO2R', 'Ethylene (C2H4)', 'CO2 + H2O', 'Renewable Electricity', 'Hierarchical Cu mesh + Solid acid', '50 °C, 1.2 atm, 3.4 V', '100 mA/cm² at 10 A', '62.0% FE', '19.0%', '33.5 kWh/kg C2H4', '1-20 years (Polyethylene)', '5-6', '100 cm² MEA pilot (1,020 h stability)'],
    ['P05', 'Zero-Gap AEM eCO2R', 'Ethanol (C2H5OH)', 'CO2 + H2O', 'Renewable Electricity', 'Cu-Zn stepped mesoporous GDE', '25 °C, 1 atm, 3.2 V', '450 mA/cm²', '42.0% FE', '24.0%', '42.0 kWh/kg EtOH', '< 6 months (Fuel)', '4-5', 'Benchtop flow-cell validation'],
    ['P06', 'Thermocatalytic Reforming', 'Tailored Syngas (H2/CO=2)', '3CH4 + CO2 + 2H2O', 'Thermal Heat', 'Ni/CaO-Al2O3 / Bimetallic Ni-Fe', '800 °C, 1.5 MPa', 'GHSV 12,000 mL/g/h', 'H2/CO = 2.01', '82.0% CO2, 91% CH4', 'Thermal Eff 74%', '< 6 months (Syngas)', '6-7', 'Pilot demonstration (Chan et al. 2025)'],
    ['P07', 'Direct Carbonate Synthesis', 'Dimethyl Carbonate (DMC)', 'CO2 + 2MeOH', 'Thermal Heat', 'CeO2 + 2-cyanopyridine', '120 °C, 5.0 MPa', '92% isolated yield', '>98.0% Sel', '94.0% MeOH conv', '4.5 MJ/kg DMC', '1-10 years (Electrolyte)', '5-6', 'Pilot batch reactors (Tamura et al. 2020)'],
    ['P08', 'Epoxide Cycloaddition', 'Cyclic Carbonates (PC/EC)', 'Epoxide + CO2', 'Low-Grade Heat', 'Biochar supported phosphonium salts', '80 °C, 1.0 MPa, solvent-free', '98.5% isolated yield', '>99.0% Sel', '99.2% PO conv', 'Exergonic', '5-15 years (Electrolyte)', '7-8', 'Commercial solvent & battery plants'],
    ['P09', 'Ring-Opening Copolymerization', 'Polycarbonate Polyols', 'Epoxide + CO2 + Diol', 'Process Heat', 'Heterodinuclear Co(III)/Zn(II)', '80-90 °C, 3.0 MPa', 'TON > 50,000', '>99.0% Carbonate', '>95.0% PO conv', 'Exergonic', '10-50 years (Foams)', '8-9', 'Covestro cardyon® (5 ktpa Dormagen), Econic'],
    ['P10', 'Molten Salt Electrosynthesis', 'Carbon Nanotubes (CNTs)', 'CO2 (via CO3[2-])', 'Electricity + 750 °C', 'Galvanized cathode in Li2CO3 melt', '750 °C, 1 atm, 1.8 V', '0.35 g CNT/Ah', '96-98% Coulombic', '>95.0% CO2 uptake', '18.0 kWh/kg CNT', '> 10,000 years (Rocks)', '6-7', 'C2CNT XPRIZE demonstration unit'],
    ['P11', 'Industrial Slag Carbonation', 'Precast Slag Concrete', 'Slag + CO2', 'Ambient Exothermic', 'Alkaline matrix self-catalyzed', '25-60 °C, 0.2 MPa, 60% RH', '150-250 kg CO2/t slag', '100% Carbonate', '20 wt% uptake', 'Net Energy Negative', '> 1,000 years (Concrete)', '8-9', 'CarbonCure, Solidia commercial plants'],
    ['P12', 'In-Situ Basalt Carbonation', 'Calcite / Magnesite', 'CO2 + Water + Basalt', 'Pumping Energy', 'Subsurface basalt rock matrix', '20-50 °C, 25 bar dissolved', '95% mineralized in 2 yr', '100% Mineral', '>95.0% stored', '0.15 MWh/t CO2', '> 10,000 years (Calcite)', '8-9', 'Mammoth DAC / Carbfix (36 ktpa Iceland)'],
    ['P13', 'Microbial Electrosynthesis', 'Acetate (CH3COOH)', 'CO2 + Electrons / H2', 'Cathode Potential', 'Moorella / Acetobacterium biofilm', '35 °C, pH 6.8, -0.8 V vs SHE', '1.4-15 g/L/d', '88-95% Cathodic FE', '65-80% uptake', '32% Energy Eff', '< 6 months (Biochem)', '5-6', 'Pilot bioreactors; LanzaTech syngas commercial']
]


def build_tables_and_figures(
    tables_dir: Path | str = DEFAULT_TABLES_DIR,
    figures_dir: Path | str = DEFAULT_FIGURES_DIR,
) -> None:
    """Generate cross-pathway tables and figure plans."""
    t_dir = Path(tables_dir).resolve()
    f_dir = Path(figures_dir).resolve()
    t_dir.mkdir(parents=True, exist_ok=True)
    f_dir.mkdir(parents=True, exist_ok=True)

    # 1. TABLE_AUDIT.md
    with open(t_dir / 'TABLE_AUDIT.md', 'w', encoding='utf-8') as f:
        f.write(r'''# Table Audit: Analysis of Existing Tables & Blueprint for Rebuilt Tables

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
''')

    # 2. CROSS_PATHWAY_TABLE.csv
    with open(t_dir / 'CROSS_PATHWAY_TABLE.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(CROSS_HEADERS)
        writer.writerows(CROSS_ROWS)

    # 3. FIGURE_AUDIT.md
    with open(f_dir / 'FIGURE_AUDIT.md', 'w', encoding='utf-8') as f:
        f.write(r'''# Figure Audit: Critical Evaluation of Existing Figures & Rebuilding Blueprint

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
''')

    # 4. FIGURE_PLANS.md
    with open(f_dir / 'FIGURE_PLANS.md', 'w', encoding='utf-8') as f:
        f.write(r'''# Rebuilt Publication Figure Plans: Conceptual Specifications & Diagram Code

**Document:** `research/figures/FIGURE_PLANS.md`  
**Execution Date:** October 2026

---

## Figure 1: Comprehensive CO₂ Utilisation Architecture

```mermaid
flowchart TD
    subgraph SOUR["CO₂ Feedstock Sources"]
        S1["Point Source (Flue Gas 10-30%)"]
        S2["Direct Air Capture (DAC ~420 ppm)"]
        S3["Biogenic (Biogas / Fermentation)"]
    end

    subgraph ENER["Energy & Reductant Vectors"]
        E1["Green Hydrogen (Water Electrolysis)"]
        E2["Renewable Electricity (Wind / Solar)"]
        E3["Thermal Energy (Waste Heat / Electric)"]
        E4["Zero-Energy (Natural Alkaline Minerals)"]
    end

    subgraph CONV["Conversion Pathways"]
        C1["Thermocatalytic Hydrogenation (Methanol, Syngas, DRM)"]
        C2["Electrochemical Reduction (CO, HCOOH, C2H4, Ethanol)"]
        C3["Organic Carbonates & Polymers (DMC, ROCOP Polyols)"]
        C4["Mineral Carbonation (Basalt In-Situ, Slag Curing)"]
        C5["Biological & MES (Gas Fermentation, Acetate)"]
        C6["Integrated Capture & Conversion (DFMs)"]
    end

    subgraph FATE["Carbon Permanence & Sinks"]
        F1["Short-Lived (< 6 Months): Fuels & Fertilizers -> 100% Re-emitted"]
        F2["Medium-Lived (1-10 Years): Solvents, Electrolytes, Chemicals"]
        F3["Long-Lived (10-50 Years): Polyurethane Insulation, Polymers"]
        F4["Permanent (> 1,000-10,000 Years): Solid Calcite, Concrete, CNTs"]
    end

    SOUR --> CONV
    ENER --> CONV
    CONV --> FATE
```

---

## Figure 2: Thermodynamic Free Energy Landscape of CO₂ Activation

```mermaid
graph LR
    subgraph UPHILL["Endergonic Reactions (ΔG° > 0, Requires External Energy Input)"]
        U1["CO2 + 3H2 -> CH3OH + H2O (ΔG° = +3.5 kJ)"]
        U2["CO2 + H2 -> CO + H2O (ΔG° = +28.6 kJ)"]
        U3["CO2 + 2MeOH -> DMC + H2O (ΔG° = +26.2 kJ)"]
        U4["2CO2 + 12H+ + 12e- -> C2H4 (ΔG° = +1331 kJ)"]
        U5["CO2 -> C(s) + O2(g) (ΔG° = +394.4 kJ)"]
    end

    subgraph DOWNHILL["Exergonic Reactions (ΔG° < 0, Thermodynamically Spontaneous)"]
        D1["2NH3 + CO2 -> Urea + H2O (ΔG° = -15.0 kJ)"]
        D2["Epoxide + CO2 -> Cyclic Carbonate (ΔG° = -42.0 kJ)"]
        D3["CaSiO3 + CO2 -> CaCO3 + SiO2 (ΔG° = -44.0 kJ)"]
        D4["Ca(OH)2 + CO2 -> CaCO3 + H2O (ΔG° = -65.0 kJ)"]
        D5["2CO2 + 4H2 -> CH3COOH + 2H2O (ΔG° = -75.0 kJ)"]
    end
```

---

## Figure 3: Dual-Function Material (DFM) Isothermal Reactive Capture

```mermaid
sequenceDiagram
    participant FG as Flue Gas (10% CO2, 320°C)
    participant Sorb as Sorbent Active Site (Na2O)
    participant Cat as Catalyst Active Site (Ru)
    participant H2 as Green H2 Stream (320°C)
    participant Prod as Pipeline Methane (CH4)

    Note over Sorb, Cat: Dual-Function Material Bed at Isothermal 320°C
    FG->>Sorb: Chemisorption of CO2
    Sorb->>Sorb: Formation of Surface Carbonate (Na2CO3)
    Note over FG: Flue gas exhaust purged (CO2 captured)
    H2->>Cat: Hydrogen stream introduced
    Sorb->>Cat: Carbonate spillover to Ru nanoparticles
    Cat->>Cat: In-situ methanation: Na2CO3 + 4H2 -> CH4 + 2H2O + Na2O
    Cat->>Prod: Pure CH4 released (95% conversion, >99% selectivity)
    Note over Sorb: Sorbent regenerated in-situ without thermal desorption!
```
''')

    print(f"Successfully generated tables in {t_dir} and figures in {f_dir}.")


def parse_args(args: Sequence[str] | None = None) -> argparse.Namespace:
    """Parse CLI arguments."""
    parser = argparse.ArgumentParser(description="Generate CCU Tables and Figure Plans.")
    parser.add_argument(
        "--tables-dir",
        type=Path,
        default=DEFAULT_TABLES_DIR,
        help="Target output directory for table specifications.",
    )
    parser.add_argument(
        "--figures-dir",
        type=Path,
        default=DEFAULT_FIGURES_DIR,
        help="Target output directory for figure plans.",
    )
    return parser.parse_args(args)


def main() -> None:
    """CLI Entry Point."""
    args = parse_args()
    build_tables_and_figures(tables_dir=args.tables_dir, figures_dir=args.figures_dir)


if __name__ == "__main__":
    main()
