# Life-Cycle Assessment (LCA) and Techno-Economic Analysis (TEA): Rigorous Methodological Framework, Harmonized Assumptions, and Scientific Boundaries

**Document:** `research/lca_tea/FINAL_LCA_TEA_ASSUMPTIONS_AND_LIMITATIONS.md`  
**Execution Date:** October 2026  
**Auditor:** Scientific Pair-Programming Research Sprint (IIIT-Delhi)  
**Standard Compliance:** ISO 14040/14044; Global CO₂ Initiative Guidelines for CCU Assessment

---

## 1. Fundamental Principles & Definition of Terms

A critical scientific deficiency in many CCU publications is the conflation of **chemical utilisation**, **avoided emissions**, and **carbon dioxide removal (CDR)**. To prevent scientific overstatement, this review enforces the following strict definitions:

```
┌──────────────────────────────────────────────────────────────────────────────────┐
│                             THE CCU IMPACT TAXONOMY                              │
├──────────────────────────────────────────────────────────────────────────────────┤
│ 1. Direct Carbon Utilisation (Physical Reactant):                                 │
│    CO2 is a physical chemical building block in the reaction stoichiometry.      │
│    Gross CO2 uptake does NOT equal net climate benefit.                          │
│                                                                                  │
│ 2. Avoided Greenhouse Gas Emissions (Relative Climate Benefit):                 │
│    ΔE_avoided = E_fossil_baseline - E_CCU_system > 0                              │
│    The CCU product displaces an incumbent fossil product, emitting fewer cradle-  │
│    to-grave greenhouse gases overall. The carbon is eventually returned to the    │
│    atmosphere upon product combustion or degradation.                            │
│                                                                                  │
│ 3. Carbon Dioxide Removal (CDR / Permanent Geological/Mineral Storage):          │
│    CO2 is captured directly from ambient air (DAC) or biogenic sources (BECCS)    │
│    and transformed into a thermodynamically inert, permanent mineral or solid    │
│    matrix with physical retention > 1,000–10,000 years.                          │
│    CO2 captured from fossil point sources and stored is AVOIDANCE, not REMOVAL.   │
└──────────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Derivation of Avoided Emissions & Grid Sensitivity Models

### 2.1 The Cradle-to-Grave Mathematical Balance
$$\Delta E_\text{avoided} = E_\text{conventional, cradle-to-grave} - E_{\text{CCU}, \text{cradle-to-grave}}$$

Where the life-cycle footprint of the CCU system ($E_\text{CCU}$) is expanded into seven explicit lifecycle stages:
$$E_\text{CCU} = E_\text{capture} + E_{\text{H}_2} + E_\text{electricity} + E_\text{thermal} + E_\text{catalyst/materials} + E_\text{separation} + E_\text{end-of-life} - M_{\text{CO}_2, \text{incorporated}}$$

- $E_\text{capture}$: Direct emissions from solvent regeneration ($3.0–3.5\text{ GJ/t CO}_2$ thermal for liquid amines) or DAC electrical/thermal input ($1.5–2.5\text{ MWh/t CO}_2$).
- $E_{\text{H}_2}$: Upstream emissions from hydrogen production ($m_{\text{H}_2} \times CI_{\text{H}_2}$). SMR grey hydrogen emits $10.0–12.0\text{ kg CO}_2\text{e/kg H}_2$; water electrolysis green hydrogen emits $<0.5–2.0\text{ kg CO}_2\text{e/kg H}_2$ depending on the generation mix.
- $E_\text{electricity}$: Process electrical duty multiplied by the grid carbon intensity:
  $$E_\text{electricity} = \text{SEC}_\text{process} \times CI_\text{grid}$$
- $E_\text{separation}$: Energy consumed in product downstream recovery (distillation of dilute ethanol/acetate, azeotropic drying of formic acid, or crystallization).
- $E_\text{end-of-life}$: Carbon released upon oxidation, combustion, or biodegradation. For synthetic fuels and agricultural urea, $E_\text{end-of-life} = +M_{\text{CO}_2, \text{incorporated}}$, exactly cancelling the gross capture credit!

### 2.2 Derivation of the Break-Even Grid Carbon Intensity ($CI_\text{grid}^*$)
Setting $\Delta E_\text{avoided} = 0$:
$$CI_\text{grid}^* = \frac{E_\text{conventional} + M_{\text{CO}_2, \text{incorporated}} - (E_\text{capture} + E_{\text{H}_2} + E_\text{thermal} + E_\text{separation} + E_\text{end-of-life})}{\text{SEC}_\text{process}}$$

- **Model Result:** As established by Sternberg & Bardow (*Nature Climate Change* 2021), because electrocatalytic pathways and water electrolysis are intensely electricity-demanding ($\text{SEC} = 30–50\text{ kWh/kg}$ for $\text{C}_2$ products), the break-even grid carbon intensity threshold across chemical syntheses is:
  $$CI_\text{grid}^* \approx 100\text{ to }150\text{ g CO}_2\text{e/kWh}$$
- **Geographic Reality Check:**
  - India Grid Average (2024): ~710 g $\text{CO}_2\text{e}$/kWh
  - United States Grid Average (2024): ~380 g $\text{CO}_2\text{e}$/kWh
  - European Union Average (2024): ~230 g $\text{CO}_2\text{e}$/kWh
  - **Direct Consequence:** If CCU electrochemical or hydrogenation processes are connected to average municipal power grids anywhere in the world today, **they emit significantly more net greenhouse gases than the conventional fossil processes they seek to displace.** Direct coupling to dedicated off-grid renewable energy (wind, solar, nuclear, or hydro) is an absolute, non-negotiable physical prerequisite.

---

## 3. Explicit Correction of Seven Critical Literature Overstatements

To ensure absolute scientific integrity, this audit formally refutes seven prevalent overstatements in the CCU literature:

### 1. "Exothermic Mineral Carbonation is Automatically Net-Negative"
- **Correction:** While the chemical carbonation of wollastonite ($\text{CaSiO}_3 + \text{CO}_2 \rightarrow \text{CaCO}_3 + \text{SiO}_2$, $\Delta H^\circ = -87\text{ kJ/mol}$) or portlandite is strongly exothermic, the *industrial process* requires quarrying, crushing, ultra-fine mechanical grinding ($<45\ \mu\text{m}$), and elevated thermal-pressure dissolution ($100–180^\circ\text{C}$, 2–5 MPa). The comminution energy of hard silicate ores consumes 30–60 kWh/tonne rock. Unless powered by renewable energy, upstream mining and comminution emissions erode up to 30–50% of the gross carbon sequestered.

### 2. "Urea Always Releases All Incorporated CO₂ Within a Fixed Number of Days"
- **Correction:** In agricultural fertilizer use, soil microbial urease rapidly hydrolyzes urea into $\text{NH}_3$ and $\text{CO}_2$ within 7 to 28 days under temperate field conditions (100% emission return). However, when urea is reacted with formaldehyde to form urea-formaldehyde (UF) resins or cyclic ethylene urea for wood adhesives and durable particleboards, the carbon remains locked for **10 to 50 years**. The carbon retention must be evaluated based on final market use, not the chemical molecule alone.

### 3. "Carbon Nanomaterials Automatically Store Carbon for Millennia"
- **Correction:** Pure carbon nanotubes and graphene are chemically inert and thermodynamically stable, theoretically persisting for $>10,000$ years in solid matrix composites. However, their lifecycle carbon permanence depends entirely on composite end-of-life: if CNT-reinforced polymers are incinerated in municipal waste-to-energy facilities at end-of-life, 100% of the incorporated carbon is oxidized back to gaseous $\text{CO}_2$ within decades.

### 4. "Renewable Electricity Automatically Makes Every CCU Process Climate-Beneficial"
- **Correction:** Renewable electricity has an opportunity cost. If scarce renewable electricity is diverted from decarbonizing the regional electrical grid (displacing coal/gas power at $500–800\text{ g CO}_2\text{/kWh}$) to power an inefficient electrochemical $\text{CO}_2$ cell (avoiding only $100–200\text{ g CO}_2\text{/kWh}$), the net societal climate impact is *negative*. Systemic merit order requires electrifying primary energy demand before deploying power-to-X CCU.

### 5. "High Faradaic Efficiency Automatically Proves Commercial Feasibility"
- **Correction:** A catalyst demonstrating 95% Faradaic efficiency in a dilute laboratory H-cell often operates at cell voltages $>3.5\text{ V}$ with single-pass conversion $<15\%$ and severe carbonate crossover (>50% loss of feed gas). Half-cell Faradaic efficiency completely ignores cell overpotential, membrane resistance, gas compression duty, and dilute product separation energy. Full-cell Energy Efficiency (EE) and space-time yield are the true techno-economic benchmarks.

### 6. "CO₂ Utilisation is Equivalent to Permanent Geological Storage"
- **Correction:** Converting captured $\text{CO}_2$ into synthetic kerosene, methanol, or methane circulates carbon in a closed or open atmospheric loop for $<6$ months. It does NOT lower the absolute atmospheric $\text{CO}_2$ concentration. Geological storage (e.g. injection into depleted saline aquifers) and basalt mineralization isolate carbon permanently from the active carbon cycle for $>10,000$ years. Utilisation and storage serve distinct climate functions and must never be conflated.

### 7. "A Universal Electricity-Intensity Threshold Exists for All CCU Pathways"
- **Correction:** Grid break-even intensity varies by an order of magnitude across products. High-electron products requiring massive hydrogen stoichiometry (e.g. ethylene, 12 electrons, requiring 32 kWh/kg) demand $CI_\text{grid} < 50\text{ g CO}_2\text{/kWh}$. Conversely, low-energy exergonic processes (e.g. concrete slag carbonation curing) achieve net avoided emissions on grids with $CI_\text{grid} > 400\text{ g CO}_2\text{/kWh}$.

---

## 4. Harmonized Techno-Economic Modeling Assumptions

All Levelized Cost of Product (LCOP) figures in `SCENARIO_COMPARISON.csv` and `FINAL_CROSS_PATHWAY_COMPARISON.csv` are calculated using a standardized Discounted Cash Flow (DCF) framework:

- **Plant Lifetime:** 20 years
- **Weighted Average Cost of Capital (WACC / Discount Rate):** 8.0% real
- **On-Stream Availability:** 8,000 operating hours/year (91.3% capacity factor)
- **Point-Source CO₂ Capture Cost:** \$40/tonne (dilute flue gas) to \$80/tonne (industrial cement/steel)
- **Direct Air Capture (DAC) CO₂ Cost:** \$400/tonne (current) declining to \$150/tonne (projected 2035)
- **Green Hydrogen Cost:** \$4.00/kg (current base case) and \$1.75/kg (2030 projected policy-supported case)
- **Industrial Electricity Tariff:** \$45/MWh (base industrial renewable PPA) with sensitivity evaluated from \$20 to \$80/MWh
- **Electrolyzer Stack Durability:** Formic acid SSE (2 years); Zero-gap MEA (3 years); Alkaline water electrolyzer (8 years)

---

## 5. Summary Table: Carbon Permanence & LCA-TEA Benchmarks

| Pathway | Target Product | Stoichiometric H2 Demand (kg/t) | Electricity Demand (MWh/t) | Retention Lifespan | Break-even Grid CI (g CO₂e/kWh) | Current LCOP (\$/t) | Fossil Market Baseline (\$/t) |
|---|---|---|---|---|---|---|---|
| **Thermocatalytic** | Methanol | 190 | 10.5 | < 6 months | < 120 | \$550–\$850 | \$350–\$450 |
| **Solid-Electrolyte eCO2R** | Formic Acid | 0 | 4.2 | 1–5 years | < 220 | \$600–\$750 | \$750–\$900 |
| **Zero-Gap MEA eCO2R** | Carbon Monoxide | 0 | 7.2 | Short-lived | < 180 | \$600–\$900 | \$700–\$1,000 |
| **Pure-Water MEA eCO2R** | Ethylene | 0 | 32.0 | 1–20 years | < 50 | \$1,800–\$2,500 | \$1,000–\$1,200 |
| **Industrial Melt** | Urea | 570 (via NH3) | 1.1 | 7–28 days | < 150 | \$380–\$500 | \$350–\$450 |
| **Ceria Heterogeneous** | Cyclic Ethylene Urea | 0 | 1.8 | 10–50 years | < 250 | \$1,400–\$1,800 | \$1,500–\$2,000 |
| **Direct Synthesis** | DMC | 0 | 2.5 | 2–10 years | < 200 | \$1,300–\$1,600 | \$1,100–\$1,300 |
| **Epoxide Copolymerization** | Polycarbonate Polyols | 0 | 0.8 | 10–50 years | < 350 | \$1,800–\$2,400 | \$2,000–\$2,500 |
| **Molten Carbonate C2CNT** | Carbon Nanotubes | 0 | 18.0 | > 10,000 years | < 180 | \$1,500–\$2,500 | \$20,000–\$100,000 |
| **In-Situ Basalt Mineralization** | Calcite Stone | 0 | 0.2 | > 10,000 years | < 800 | \$100–\$150/t CO₂ | N/A (Disposal) |
| **Slag Concrete Curing** | Precast Concrete | 0 | 0.1 | > 1,000 years | < 600 | \$15–\$25/t product | \$25–\$35/t product |

---
