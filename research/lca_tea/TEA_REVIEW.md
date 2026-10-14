# Techno-Economic Analysis (TEA) Review: CAPEX, OPEX, and Levelized Cost of Products (LCOP)

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
