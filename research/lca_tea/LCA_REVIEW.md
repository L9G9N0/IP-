# Life-Cycle Assessment (LCA) Review: System Boundaries, Energy Penalties, and Net Avoided Emissions

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
