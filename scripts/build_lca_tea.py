"""LCA and TEA Scenario Generator for CCU Evidence Engine.

Generates Life-Cycle Assessment boundaries, Techno-Economic reviews, and
the multi-scenario sensitivity comparison matrix in research/lca_tea/.
"""

from __future__ import annotations

import argparse
import csv
from pathlib import Path
from typing import Sequence

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_OUTPUT_DIR = REPO_ROOT / 'research' / 'lca_tea'


def build_lca_tea(output_dir: Path | str = DEFAULT_OUTPUT_DIR) -> None:
    """Generate LCA review, TEA review, and scenario comparison CSV."""
    out_dir = Path(output_dir).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / 'LCA_REVIEW.md', 'w', encoding='utf-8') as f:
        f.write(r'''# Life-Cycle Assessment (LCA) Review: System Boundaries, Energy Penalties, and Net Avoided Emissions

**Document:** `research/lca_tea/LCA_REVIEW.md`  
**Execution Date:** October 2026  
**Guidelines:** Harmonized with ISO 14040/14044 and Global CO₂ Initiative Guidelines for CCU.

---

## 1. Methodological Framework & System Boundaries

Evaluating whether carbon dioxide utilisation yields a net climate benefit requires strict life-cycle accounting. A common fallacy is equating the *gross amount of CO₂ chemically incorporated into a product* with a *net climate reduction*.

```
┌───────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                   Cradle-to-Grave System Boundary                                 │
│                                                                                                   │
│  [CO2 Source] ──► [Capture & Clean] ──► [H2 / Power] ──► [Conversion] ──► [Separation] ──► [Use] ──► [End-of-Life]
│    (Point / DAC)    (Solvent / DFM)      (Green / Grey)    (Reactor / Cell)  (Distillation) (Fuel/Mat) (EoL / Leak)│
└───────────────────────────────────────────────────────────────────────────────────────────────────┘
```

### 1.1 Net Avoided Emissions Equation
$$\Delta E_\text{avoided} = E_\text{conventional, cradle-to-grave} - E_{\text{CCU}, \text{cradle-to-grave}}$$
- **True Mitigation Condition:** $\Delta E_\text{avoided} > 0$.
- **Adverse Condition:** If $\Delta E_\text{avoided} < 0$, the CCU process generates **more atmospheric GHG emissions** than the incumbent fossil route, despite consuming CO₂ as a physical reactant.

### 1.2 Upstream Dependency Thresholds
As established by Sternberg & Bardow (*Nature Climate Change* 2021), CCU chemical pathways are intensely sensitive to two upstream parameters:
1. **Grid Electricity Carbon Intensity ($CI_\text{grid}$):**  
   - Break-even threshold across chemical products: **$CI_\text{grid} < 100–150\text{ g CO}_2\text{e/kWh}$**.
   - On average fossil-heavy grids (e.g., US average ~380 g/kWh; India average ~710 g/kWh; EU average ~230 g/kWh), electrocatalytic and hydrogenation pathways emit **net positive greenhouse gases**.
2. **Hydrogen Carbon Intensity ($CI_{\text{H}_2}$):**  
   - Producing 1 tonne of methanol requires ~190 kg $\text{H}_2$.
   - Sourcing grey $\text{H}_2$ via Steam Methane Reforming (SMR, emitting $10–12\text{ kg CO}_2\text{e/kg H}_2$) contributes $+1.9\text{ to }+2.3\text{ t CO}_2\text{e/t MeOH}$, turning the net balance positive (+2.5 to +2.8 kg $\text{CO}_2\text{e/kg MeOH}$).
   - Sourcing green $\text{H}_2$ via water electrolysis ($<2\text{ kg CO}_2\text{e/kg H}_2$) achieves net avoided emissions of **-1.2 to -1.4 kg $\text{CO}_2\text{e/kg MeOH}$**.

---

## 2. Carbon Fate & Durability Across Product Classes

| Product Class | Representative Pathways | Typical Retention Lifespan | Carbon Fate at End-of-Life | Climate Impact Role |
|---|---|---|---|---|
| **Synthetic Fuels** | e-Methanol, e-Methane, e-Kerosene, Fischer-Tropsch Diesel | **< 6 months** | Rapid combustion releases 100% of incorporated CO₂ back to atmosphere | **Avoided fossil emissions only**; zero net atmospheric carbon removal |
| **Agricultural Fertilizers** | Urea | **7 to 28 days** | Urease enzymatic hydrolysis releases 100% of incorporated CO₂ in soil | Nitrogen carrier only; **zero sequestration** |
| **Short-Lived Chemicals** | Formic acid (de-icing), Acetic acid, Solvents | **6 months to 2 years** | Biodegradation or wastewater oxidation | Avoided fossil extraction emissions |
| **Durable Polymers & Materials** | Polycarbonate polyols, Polypropylene carbonate (PPC) | **10 to 50 years** | Landfill, mechanical recycling, or incineration | Medium-term delay of carbon release |
| **Mineral Carbonation** | In-situ basalt storage, Precast concrete slag blocks, Aggregates | **> 1,000 to > 10,000 years** | Permanent calcite/magnesite geological matrix; thermodynamically stable | **Permanent Carbon Dioxide Removal (CDR)** |

---

## 3. Detailed Cross-Pathway LCA Findings

### 3.1 Methanol Hydrogenation
- **Stoichiometry:** $\text{CO}_2 + 3\text{H}_2 \rightarrow \text{CH}_3\text{OH} + \text{H}_2\text{O}$
- **Energy Requirement:** 10.5 MWh/tonne MeOH (dominated by electrolysis).
- **Life-Cycle Balance:**
  - With Grey $\text{H}_2$ (SMR): $+2.75\text{ kg CO}_2\text{e/kg MeOH}$ (fossil baseline is $+0.80\text{ kg CO}_2\text{e/kg}$).
  - With Green $\text{H}_2$ (Wind/Solar): **$-1.35\text{ kg CO}_2\text{e/kg MeOH}$** (net avoided: $+2.15\text{ kg CO}_2\text{e/kg}$).

### 3.2 Electrochemical Ethylene
- **Stoichiometry:** $2\text{CO}_2 + 12\text{H}^+ + 12e^- \rightarrow \text{C}_2\text{H}_4 + 4\text{H}_2\text{O}$
- **Energy Requirement:** 32–35 kWh/kg $\text{C}_2\text{H}_4$.
- **Life-Cycle Balance:**
  - On average US grid (380 g/kWh): $+11.8\text{ kg CO}_2\text{e/kg C}_2\text{H}_4$ (fossil baseline is $+1.7\text{ kg CO}_2\text{e/kg}$).
  - With 100% Renewable Electricity (20 g/kWh): **$-1.40\text{ kg CO}_2\text{e/kg C}_2\text{H}_4$** (net avoided: $+3.10\text{ kg CO}_2\text{e/kg}$).

### 3.3 Carbonated Concrete & Steel Slag
- **Stoichiometry:** $\text{Ca(OH)}_2 + \text{CO}_2 \rightarrow \text{CaCO}_3 + \text{H}_2\text{O}$
- **Energy Requirement:** Net energy negative (exothermic curing releases ~1.2 GJ/tonne $\text{CO}_2$).
- **Life-Cycle Balance:**
  - Sequestered Carbon: $0.15–0.25\text{ t CO}_2\text{/t slag}$.
  - Avoided Clinker Emissions: Displacing Ordinary Portland Cement (OPC) avoids **0.65–0.80 t $\text{CO}_2\text{e/t cement}$**, yielding a highly negative net footprint of **-0.85 to -1.05 t $\text{CO}_2\text{e/t}$**.
''')

# 2. TEA_REVIEW.md
    with open(out_dir / 'TEA_REVIEW.md', 'w', encoding='utf-8') as f:
        f.write(r'''# Techno-Economic Analysis (TEA) Review: CAPEX, OPEX, and Levelized Cost of Products (LCOP)

**Document:** `research/lca_tea/TEA_REVIEW.md`  
**Execution Date:** October 2026  
**Guidelines:** Harmonized cost modeling based on discounted cash flow (DCF), 20-year plant life, 8% weighted average cost of capital (WACC).

---

## 1. Cost Drivers & Sensitivity Hierarchy across CCU Pathways

The levelized cost of producing chemicals and materials from $\text{CO}_2$ is dictated by four major cost components:
1. **Feedstock Cost:** Cost of captured $\text{CO}_2$ (\$40–\$120/t from point sources; \$300–\$600/t from Direct Air Capture).
2. **Energy Vector Cost:** Green $\text{H}_2$ (\$3.00–\$6.00/kg currently) and renewable electricity (\$30–\$60/MWh).
3. **Electrolyzer Stack / Reactor CAPEX:** Stack replacement frequency (dependent on lifetime: 100 h vs 1,000 h vs 40,000 h) and balance-of-plant (BOP).
4. **Product Separation & Purification OPEX:** Distillation of dilute aqueous streams, azeotropic drying, and salt waste disposal.

```
Cost Distribution for e-Chemicals (Average):
┌──────────────────────────────┬──────────────┬──────────────┬──────────────┐
│ Electricity & H2 (55–70%)    │ CAPEX (15–25%)│ CO2 (8–12%)  │ O&M (5–10%)  │
└──────────────────────────────┴──────────────┴──────────────┴──────────────┘
```

---

## 2. Levelized Cost of Product (LCOP) Benchmarks

$$\text{LCOP} = \frac{\sum_{t=0}^N \frac{\text{CAPEX}_t + \text{OPEX}_t + \text{Feedstock}_t}{(1 + r)^t}}{\sum_{t=0}^N \frac{\text{Production}_t}{(1 + r)^t}}$$

### 2.1 Cross-Pathway LCOP Summary Table

| Product | Pathway | Current LCOP (\$/tonne) | Fossil Baseline Price (\$/tonne) | Cost Parity Gap | Key Sensitivity Driver |
|---|---|---|---|---|---|
| **Methanol** | Thermocatalytic $\text{CO}_2 + 3\text{H}_2$ | \$550–\$850 | \$350–\$450 | +55% to +100% | Green $\text{H}_2$ cost ($-\$200/\text{t}$ per $\$1/\text{kg H}_2$) |
| **Formic Acid** | Solid-Electrolyte eCO₂R | \$600–\$750 | \$750–\$900 | **Competitive (-15%)** | Stack lifetime & electricity price |
| **Carbon Monoxide** | Zero-gap MEA eCO₂R | \$600–\$900 | \$700–\$1,000 | **Near Parity** | Cell voltage & membrane durability |
| **Ethylene** | Pure-water MEA eCO₂R | \$1,800–\$2,500 | \$1,000–\$1,200 | +80% to +120% | High electricity intensity ($32\text{ kWh/kg}$) |
| **DMC** | Direct $\text{CeO}_2$ + Nitrile | \$1,300–\$1,600 | \$1,100–\$1,300 | +20% | Dehydrating agent recovery thermal duty |
| **Polycarbonate Polyols** | PO/$\text{CO}_2$ ROCOP | \$1,800–\$2,400 | \$2,000–\$2,500 | **Profitable today** | Epoxide feedstock price & catalyst TON |
| **Carbon Nanotubes** | Molten Carbonate C2CNT | \$1,500–\$2,500 | \$20,000–\$100,000 | **Massive Advantage** | Molten salt corrosion & cathode lifetime |
| **Precast Concrete** | Slag Carbonation Curing | \$15–\$25 | \$25–\$35 | **Profitable today** | Displaces expensive virgin Portland clinker |

---

## 3. Path to Commercial Competitiveness (2025–2035)

1. **Green Hydrogen Deflation:** Under the US IRA (\$3/kg production credit) and Indian Green Hydrogen Mission, green $\text{H}_2$ costs are projected to drop to **$\$1.50–\$2.00/\text{kg}$ by 2030**, bringing e-methanol LCOP directly into the competitive \$350–\$420/tonne range.
2. **Electrolyzer Capital Learning Curves:** Modular zero-gap MEA stacks are projected to experience 18% cost decline per doubling of manufacturing capacity, dropping stack CAPEX from $\$1,500/\text{kW}$ to $<\$400/\text{kW}$ by 2032.
3. **Policy Parity Enablers:** Carbon pricing (EU ETS at €80–€100/t) and US IRA 45Q utilisation subsidies (\$60–\$130/t) bridge the remaining cost premium for early commercial adopters.
''')

# 3. SCENARIO_COMPARISON.csv
    csv_headers = [
    'Pathway_ID', 'Pathway_Name', 'Target_Product', 'Functional_Unit',
    'Fossil_Baseline_Emissions_kgCO2e', 'CCU_GreyH2_Grid_Emissions_kgCO2e',
    'CCU_GreenH2_Renewable_Emissions_kgCO2e', 'Net_Avoided_Emissions_Best_Case_kgCO2e',
    'Electricity_Demand_kWh_per_FU', 'H2_Demand_kg_per_FU', 'Carbon_Retention_Duration',
    'Fossil_Baseline_Cost_USD_per_FU', 'CCU_Current_Cost_USD_per_FU', 'CCU_Projected_2030_Cost_USD_per_FU',
    'Current_TRL', 'Commercial_Deployment_Status'
    ]

    csv_rows = [
        [
            'PATH-01', 'Thermocatalytic Hydrogenation', 'Methanol', '1 kg Methanol',
            '0.80', '2.75', '-1.35', '2.15', '10.50', '0.190', '< 6 months (Fuel)',
            '0.40', '0.70', '0.42', '8-9', 'Commercial facilities operating (CRI Iceland, Shunli China)'
    ],
        [
            'PATH-02', 'Solid-Electrolyte Reduction', 'Formic Acid (Pure)', '1 kg Formic Acid',
            '1.20', '3.10', '-0.65', '1.85', '4.20', '0.000', '1-5 years (Chemical/LOHC)',
            '0.80', '0.68', '0.48', '6-7', 'Pilot / multi-kW demonstration units'
    ],
        [
            'PATH-03', 'Zero-Gap MEA Electrosynthesis', 'Carbon Monoxide', '1 kg CO',
            '0.95', '2.40', '-1.10', '2.05', '6.50', '0.000', '< 6 months (Syngas)',
            '0.85', '0.75', '0.50', '7-8', 'Commercial demonstrations (Twelve / Siemens Energy)'
    ],
        [
            'PATH-04', 'Pure-Water MEA Electrosynthesis', 'Ethylene', '1 kg Ethylene',
            '1.70', '11.80', '-1.40', '3.10', '33.50', '0.000', '1-20 years (Polyethylene)',
            '1.10', '2.15', '1.30', '5-6', '100 cm² MEA pilot operating >1,000 h'
    ],
        [
            'PATH-05', 'Zero-Gap AEM Electrosynthesis', 'Ethanol', '1 kg Ethanol',
            '1.40', '14.20', '-0.85', '2.25', '42.00', '0.000', '< 6 months (Fuel/Sanitizer)',
            '0.65', '1.85', '1.10', '4-5', 'Benchtop flow-cell validation'
    ],
        [
            'PATH-06', 'Direct Synthesis with Dehydration', 'Dimethyl Carbonate', '1 kg DMC',
            '1.65', '3.20', '-0.85', '2.50', '2.80', '0.000', '1-10 years (Electrolyte)',
            '1.20', '1.45', '1.05', '5-6', 'Pilot batch reactors (CeO2 nanorods)'
    ],
        [
            'PATH-07', 'Ring-Opening Copolymerization', 'Polycarbonate Polyols', '1 kg Polyol',
            '2.20', '2.50', '1.92', '0.28', '0.60', '0.000', '10-50 years (Polyurethanes)',
            '2.25', '2.10', '1.85', '8-9', 'Fully commercial (Covestro cardyon®, Econic)'
    ],
        [
            'PATH-08', 'Molten Carbonate Electrosynthesis', 'Carbon Nanotubes', '1 kg CNT',
            '15.50', '22.00', '-3.67', '19.17', '18.00', '0.000', '> 10,000 years (Permanent)',
            '50.00', '2.00', '1.20', '6-7', 'Industrial pilot deployment (C2CNT XPRIZE winner)'
    ],
        [
            'PATH-09', 'Magnesiothermic Combustion', 'Carbon / MgO Composite', '1 kg Carbon',
            '15.50', '45.00', '35.00', '-19.50', '75.00', '0.000', '> 10,000 years (Permanent)',
            '50.00', '18.00', '15.00', '3-4', 'Laboratory scale (Debunked: net positive emissions)'
    ],
        [
            'PATH-10', 'Industrial Slag Carbonation Curing', 'Carbonated Concrete Slag', '1 tonne Slag Block',
            '120.00', '35.00', '-180.00', '300.00', '15.00', '0.000', '> 1,000 years (Permanent)',
            '30.00', '20.00', '16.00', '8-9', 'Commercial precast concrete plants (CarbonCure, Solidia)'
    ],
        [
            'PATH-11', 'In-Situ Basalt Mineralization', 'Mineralized Calcite', '1 tonne CO2 stored',
            '0.00', '45.00', '-920.00', '920.00', '150.00', '0.000', '> 10,000 years (Permanent CDR)',
            '0.00', '30.00', '22.00', '8-9', 'Fully operational commercial DAC+storage (Mammoth/Carbfix)'
    ],
        [
            'PATH-12', 'Microbial Electrosynthesis', 'Acetate', '1 kg Acetate',
            '1.10', '4.50', '-1.10', '2.20', '12.00', '0.000', '< 6 months (Biochemical)',
            '0.75', '1.15', '0.80', '5-6', 'Pilot bioreactors (1.4 g/L/d demonstrated)'
    ],
        [
            'PATH-13', 'Bi-Reforming of Methane', 'Tailored Syngas (H2/CO=2)', '1 Nm³ Syngas',
            '0.45', '0.65', '0.35', '0.10', '0.30', '0.000', '< 6 months (Chemical feed)',
            '0.18', '0.20', '0.16', '6-7', 'Pilot demonstration (Ni/CaO catalysts)'
    ]
    ]

    with open(out_dir / 'SCENARIO_COMPARISON.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(csv_headers)
        writer.writerows(csv_rows)

    print(f'Successfully generated LCA_REVIEW.md, TEA_REVIEW.md, and SCENARIO_COMPARISON.csv in {out_dir}.')


def parse_args(args: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Generate CCU LCA/TEA Models.')
    parser.add_argument(
        '--output-dir',
        '-o',
        type=Path,
        default=DEFAULT_OUTPUT_DIR,
        help='Target output directory for LCA/TEA models.'
    )
    return parser.parse_args(args)


def main() -> None:
    args = parse_args()
    build_lca_tea(output_dir=args.output_dir)


if __name__ == '__main__':
    main()
