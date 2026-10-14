# Pathway Research Report: Methanol Synthesis via CO₂ Hydrogenation

**Document:** `research/pathways/Methanol.md`  
**Section in Manuscript:** Section 8 (formerly Section 5.1)  
**Execution Date:** October 2026

## 1. Definition and Scope
Thermocatalytic hydrogenation of carbon dioxide with green hydrogen to produce chemical-grade methanol ($\text{CH}_3\text{OH}$), evaluated across traditional $\text{Cu/ZnO/Al}_2\text{O}_3$ catalysts and next-generation vacancy-engineered oxide systems ($\text{In}_2\text{O}_3/\text{ZrO}_2$, $\text{ZnO-ZrO}_2$).

## 2. Overall Chemical Reactions
1. **Methanol Synthesis:**
   $$\text{CO}_2(\text{g}) + 3\text{H}_2(\text{g}) \rightleftharpoons \text{CH}_3\text{OH}(\text{g}) + \text{H}_2\text{O}(\text{g}) \quad (\Delta H^\circ_{298\text{K}} = -49.5\text{ kJ/mol}, \Delta G^\circ_{298\text{K}} = +3.5\text{ kJ/mol})$$
2. **Reverse Water-Gas Shift (Competing):**
   $$\text{CO}_2(\text{g}) + \text{H}_2(\text{g}) \rightleftharpoons \text{CO}(\text{g}) + \text{H}_2\text{O}(\text{g}) \quad (\Delta H^\circ_{298\text{K}} = +41.2\text{ kJ/mol}, \Delta G^\circ_{298\text{K}} = +28.6\text{ kJ/mol})$$

## 3. Thermodynamic Basis & Equilibrium Constraints
- Exothermic hydrogenation is thermodynamically favored at low temperatures ($<250^\circ\text{C}$) and elevated pressures ($3.0–8.0\text{ MPa}$).
- Endothermic RWGS becomes thermodynamically dominant above 250°C, lowering methanol equilibrium selectivity from ~80% at 200°C to <30% at 300°C under 5 MPa.
- Theoretical maximum single-pass conversion is constrained by equilibrium to 15–25% under industrial conditions, necessitating high gas recycling ratios (3:1 to 5:1).

## 4. Catalytic Systems & Active Sites
- **$\text{Cu/ZnO/Al}_2\text{O}_3$ (Industrial Baseline):** Stepped $\text{Cu}(211)$ sites decorated with $\text{Zn}$ atoms. Highly active, but by-product water vapor induces rapid $\text{Cu}$ sintering and $\text{ZnO}$ phase separation under pure $\text{CO}_2$ feeds.
- **$\text{In}_2\text{O}_3/\text{ZrO}_2$ (2020–2025 Benchmark):** Oxygen vacancies ($V_\text{O}$) in $\text{In}_2\text{O}_3$ activate $\text{CO}_2$; heterolytic $\text{H}_2$ splitting occurs on adjacent $\text{In–O}$ pairs. Completely suppresses RWGS, achieving **100% methanol selectivity at 300°C and 5 MPa** with >1,000 h stability (Tsoukalou et al., JACS 2020).
- **$\text{ZnO-ZrO}_2$ Solid Solutions:** Dual-site activation where $\text{ZrO}_2$ coordinates $\text{CO}_2$ and $\text{Zn-O}$ pairs activate $\text{H}_2$, achieving 86.5% selectivity at 320°C (Wang et al., ACS Catal. 2022).

## 5. Quantitative Performance Benchmarks
- **Single-Pass Conversion:** 8.5% ($\text{In}_2\text{O}_3/\text{ZrO}_2$) to 15.2% ($\text{Cu/ZnO/Al}_2\text{O}_3$ optimized).
- **Methanol Selectivity:** 68–80% on $\text{Cu/ZnO}$; up to 100% on $\text{In}_2\text{O}_3$.
- **Space-Time Yield:** $0.45–0.62\text{ g}_\text{MeOH}/\text{g}_\text{cat}/\text{h}$.
- **Turnover Frequency (TOF):** $1.2 \times 10^{-2}\text{ s}^{-1}$ at 250°C.

## 6. Industrial Facilities & Commercial Scale
- **Carbon Recycling International (CRI) George Olah Plant (Svartsengi, Iceland):** 4,000 t/a capacity using geothermal $\text{CO}_2$ and hydroelectric $\text{H}_2$.
- **Shunli Plant (Anyang, Henan, China):** World's largest commercial $\text{CO}_2$-to-methanol facility (operational 2022), converting 160,000 t/a of captured industrial flue gas and coke-oven gas $\text{H}_2$ into 110,000 t/a of certified low-carbon methanol.

## 7. Life-Cycle Assessment (LCA)
- **Stoichiometric Hydrogen Demand:** Producing 1.0 tonne of methanol consumes ~188–200 kg of $\text{H}_2$.
- **Electrolysis Energy Intensity:** Water electrolysis consumes ~10–11 MWh of electricity per tonne of methanol produced.
- **Emission Sensitivity:** If $\text{H}_2$ is sourced from steam methane reforming (grey $\text{H}_2$, emitting 10–12 kg $\text{CO}_2\text{e/kg H}_2$), the resulting methanol emits **+2.5 to +2.8 kg $\text{CO}_2\text{e/kg MeOH}$**, vastly worse than fossil methanol (+0.8 kg $\text{CO}_2\text{e/kg}$). Only with green $\text{H}_2$ ($<2\text{ kg CO}_2\text{e/kg H}_2$) does net avoided emissions reach **-1.2 to -1.4 kg $\text{CO}_2\text{e/kg MeOH}$**.

## 8. Techno-Economic Analysis (TEA)
- **Levelized Cost of Product (LCOP):** \$550–\$850/tonne MeOH (compared to fossil market price of \$350–\$450/tonne).
- **Cost Sensitivity:** Green $\text{H}_2$ accounts for 65–75% of total production cost. Every \$1.00/kg reduction in $\text{H}_2$ price lowers methanol production cost by ~\$200/tonne. Break-even with fossil methanol requires green $\text{H}_2 < \$2.00/\text{kg}$ and renewable electricity $<\$30/\text{MWh}$.

## 9. Required Revisions in Manuscript
1. Integrate RWGS equilibrium equations and explain temperature-dependent selectivity drop.
2. Introduce $\text{In}_2\text{O}_3/\text{ZrO}_2$ and $\text{ZnO-ZrO}_2$ vacancy-engineered catalysts to update the single-catalyst $\text{Cu/ZnO}$ narrative.
3. Quantify stoichiometric green $\text{H}_2$ electricity penalties (10–11 MWh/t) to refute unverified sustainability claims.
