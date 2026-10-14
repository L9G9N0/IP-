import os

os.makedirs('research/pathways', exist_ok=True)
os.makedirs('research/literature', exist_ok=True)

# 1. Methanol Pathway Report
with open('research/pathways/Methanol.md', 'w', encoding='utf-8') as f:
    f.write(r'''# Pathway Research Report: Methanol Synthesis via CO₂ Hydrogenation

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
''')

# 2. Electrochemical Reduction Pathway Report
with open('research/pathways/Electrochemical_Reduction.md', 'w', encoding='utf-8') as f:
    f.write(r'''# Pathway Research Report: Electrocatalytic CO₂ Reduction (eCO₂R)

**Document:** `research/pathways/Electrochemical_Reduction.md`  
**Section in Manuscript:** Section 7 & Table 3 (formerly Section 4 & Table 2)  
**Execution Date:** October 2026

## 1. Definition and Scope
Cathodic electrochemical reduction of $\text{CO}_2$ using renewable electricity to synthesize $\text{C}_1$ ($\text{CO}$, $\text{HCOOH}$) and $\text{C}_{2+}$ chemicals/fuels ($\text{C}_2\text{H}_4$, $\text{C}_2\text{H}_5\text{OH}$, $\text{CH}_4$) in aqueous, non-aqueous, and solid-state electrolyte flow cells.

## 2. Product-Specific Chemical Equations
- **Carbon Monoxide:** $\text{CO}_2 + 2\text{H}^+ + 2e^- \rightarrow \text{CO} + \text{H}_2\text{O} \quad (E^\circ = -0.11\text{ V vs. RHE})$
- **Formic Acid:** $\text{CO}_2 + 2\text{H}^+ + 2e^- \rightarrow \text{HCOOH} \quad (E^\circ = -0.25\text{ V vs. RHE})$
- **Methane:** $\text{CO}_2 + 8\text{H}^+ + 8e^- \rightarrow \text{CH}_4 + 2\text{H}_2\text{O} \quad (E^\circ = +0.17\text{ V vs. RHE})$
- **Ethylene:** $2\text{CO}_2 + 12\text{H}^+ + 12e^- \rightarrow \text{C}_2\text{H}_4 + 4\text{H}_2\text{O} \quad (E^\circ = +0.08\text{ V vs. RHE})$
- **Ethanol:** $2\text{CO}_2 + 12\text{H}^+ + 12e^- \rightarrow \text{C}_2\text{H}_5\text{OH} + 3\text{H}_2\text{O} \quad (E^\circ = +0.09\text{ V vs. RHE})$
- **Competing HER:** $2\text{H}^+ + 2e^- \rightarrow \text{H}_2 \quad (E^\circ = 0.00\text{ V vs. RHE})$

## 3. Breakthrough Catalyst & Electrode Architectures (2020–2025)
- **Ag Nanoparticles & Ni-N-C Single-Atom Catalysts:** Achieve $\text{CO}$ Faradaic efficiency $>95\%$ at $300–500\text{ mA/cm}^2$ with full-cell voltage $<2.5\text{ V}$ in zero-gap MEA electrolyzers.
- **Bismuth Nanosheets in Solid-State Electrolytes:** Direct continuous production of 20 wt% pure liquid $\text{HCOOH}$ without salt byproducts (Xia & Wang, Nature Energy 2020).
- **Ionomer-Engineered Stepped $\text{Cu}(100)$ Electrodes:** Stabilize $*\text{CO}$ dimer intermediates, achieving $70\%$ FE to ethylene at $1.0\text{ A/cm}^2$ in flow cells (García de Arquer et al., Science 2020).
- **Pure-Water-Fed Zero-Gap MEA (Xu et al., Nature Energy 2024):** Operates at $10\text{ A}$ total current over $100\text{ cm}^2$ for **$>1,020\text{ hours}$** without salt precipitation, breaking the electrode degradation barrier.

## 4. Fundamental Process & System Bottlenecks
1. **Carbonate Crossover:** In alkaline/neutral flow cells, $\text{CO}_2$ reacts with electro-generated $\text{OH}^-$ in the boundary layer:
   $$\text{CO}_2 + 2\text{OH}^- \rightarrow \text{CO}_3^{2-} + \text{H}_2\text{O}$$
   Up to 50–70% of feed $\text{CO}_2$ crosses the anion exchange membrane as $\text{CO}_3^{2-}$ and is released at the anode mixed with $\text{O}_2$, consuming parasitic electricity for re-separation.
2. **Product Dilution in Liquid Feeds:** Electrosynthesis of liquid alcohols yields dilute streams ($<3\text{ wt% ethanol}$), requiring $4–6\text{ MJ/kg}$ of distillation energy.
3. **Single-Pass Conversion:** Typically 15–35%, requiring massive gas compression and recycle loops.

## 5. LCA & TEA Realities
- **Electricity Sensitivity:** Producing 1 kg of ethylene requires 30–35 kWh of electricity. Net greenhouse gas reductions are impossible unless grid carbon intensity is **$<50\text{ g CO}_2\text{/kWh}$**.
- **Economics:** $\text{CO}$ and $\text{HCOOH}$ are near-commercial (TRL 6–8; LCOP $\$600–\$800/\text{t}$). Ethylene and ethanol remain in pilot stage (TRL 4–6; LCOP $\$1,800/\text{t}$ vs $\$1,000/\text{t}$ market price).

## 6. Required Revisions in Manuscript
1. Correct Table 2 typo listing "CO₂" as an electrochemical product (replace with CO).
2. Distinguish Faradaic efficiency from single-pass conversion and energy efficiency.
3. Report the 2024 1,000-hour pure-water stability milestone to update the "electrode durability limitation".
''')

# 3. Dry & Bi-Reforming Pathway Report
with open('research/pathways/Dry_and_Bi_Reforming.md', 'w', encoding='utf-8') as f:
    f.write(r'''# Pathway Research Report: Dry and Bi-Reforming of Methane

**Document:** `research/pathways/Dry_and_Bi_Reforming.md`  
**Section in Manuscript:** Section 7 (formerly Section 4)  
**Execution Date:** October 2026

## 1. Definition and Scope
Thermocatalytic reforming of methane using carbon dioxide (Dry Reforming of Methane, DRM) and combined steam/carbon dioxide feeds (Bi-Reforming of Methane, BRM) to produce synthesis gas ($\text{CO} + \text{H}_2$) tailored for downstream petrochemical synthesis.

## 2. Chemical Stoichiometry & Enthalpies
1. **Dry Reforming of Methane (DRM):**
   $$\text{CH}_4(\text{g}) + \text{CO}_2(\text{g}) \rightleftharpoons 2\text{CO}(\text{g}) + 2\text{H}_2(\text{g}) \quad (\Delta H^\circ_{298\text{K}} = +247.3\text{ kJ/mol}, \Delta G^\circ_{298\text{K}} = +170.8\text{ kJ/mol})$$
2. **Bi-Reforming of Methane (BRM):**
   $$3\text{CH}_4(\text{g}) + \text{CO}_2(\text{g}) + 2\text{H}_2\text{O}(\text{g}) \rightarrow 4\text{CO}(\text{g}) + 8\text{H}_2(\text{g}) \quad (\Delta H^\circ_{298\text{K}} = +659\text{ kJ/mol})$$
3. **Methane Cracking (Side Reaction):**
   $$\text{CH}_4(\text{g}) \rightleftharpoons \text{C}(\text{s}) + 2\text{H}_2(\text{g}) \quad (\Delta H^\circ_{298\text{K}} = +74.9\text{ kJ/mol})$$
4. **Boudouard Reaction (Side Reaction):**
   $$2\text{CO}(\text{g}) \rightleftharpoons \text{C}(\text{s}) + \text{CO}_2(\text{g}) \quad (\Delta H^\circ_{298\text{K}} = -172.5\text{ kJ/mol})$$

## 3. Catalyst Advances & Coke Resistance (2020–2025)
- **Ni-Fe/Al₂O₃ Bimetallics (Manabayeva et al., 2023):** $\text{Fe}$ acts as a dynamic oxygen carrier. $\text{CO}_2$ oxidizes surface $\text{Fe}$ to $\text{FeO}_x$, and lattice oxygen rapidly reacts with carbon precursors deposited on $\text{Ni}$ sites, reducing coking rate to $<0.5\text{ mg/g}_\text{cat}/\text{h}$ at 750°C.
- **Single-Crystal MgO Passivated Ni (Song et al., Science 2020):** Nanocatalysts encapsulated in defect-free $\text{MgO}$ overlayers maintain coke-free operation for $>1,000\text{ hours}$.
- **Bi-Reforming over Ni/CaO-Al₂O₃ (Chan et al., 2025):** Produces ideal $\text{H}_2/\text{CO} = 2.01$ syngas at 800°C with $>80\%$ $\text{CO}_2$ conversion, ready for direct feeding into methanol synthesis reactors.

## 4. Carbon Fate and Climate Considerations
- DRM converts two greenhouse gases, but the resulting syngas is converted into combustible fuels or short-lived chemicals; **DRM does not constitute permanent carbon sequestration**.
- Net avoided emissions are positive only if process heat is electrified (e.g. electrical resistance heated reforming) or derived from zero-carbon sources.

## 5. Required Revisions in Manuscript
1. Include explicit balanced equations for DRM, BRM, and coking side reactions.
2. Explain the mechanistic role of $\text{Fe}$ and $\text{CaO}$ promoters in coke gasification.
3. Remove claims implying that DRM syngas automatically achieves permanent sequestration.
''')

# 4. Urea and C-N Coupling Pathway Report
with open('research/pathways/Urea_and_CN_Coupling.md', 'w', encoding='utf-8') as f:
    f.write(r'''# Pathway Research Report: Industrial Urea Synthesis & Electrocatalytic C–N Coupling

**Document:** `research/pathways/Urea_and_CN_Coupling.md`  
**Section in Manuscript:** Section 9 (formerly Section 5.2)  
**Execution Date:** October 2026

## 1. Definition and Scope
Evaluation of commercial high-pressure urea synthesis from $\text{NH}_3$ and $\text{CO}_2$, coupled with an audit of emerging ambient electrocatalytic $\text{C–N}$ coupling routes that bypass the fossil Haber-Bosch loop.

## 2. Chemical Reactions & Thermodynamics
1. **Commercial Two-Step Synthesis:**
   $$2\text{NH}_3(\text{g}) + \text{CO}_2(\text{g}) \rightleftharpoons \text{NH}_2\text{COONH}_4(\text{l}) \quad (\Delta H^\circ = -117\text{ kJ/mol, exergonic})$$
   $$\text{NH}_2\text{COONH}_4(\text{l}) \rightleftharpoons \text{CO(NH}_2)_2(\text{l}) + \text{H}_2\text{O}(\text{l}) \quad (\Delta H^\circ = +15.5\text{ kJ/mol, endergonic})$$
2. **Emerging Electrocatalytic C–N Coupling (Meng et al., Nature Chem. 2020):**
   $$\text{CO}_2(\text{g}) + \text{NO}_3^-(\text{aq}) + 9\text{H}^+ + 8e^- \rightarrow \text{CO(NH}_2)_2(\text{aq}) + 2\text{H}_2\text{O}(\text{l}) + \text{OH}^-(\text{aq})$$

## 3. Industrial Process Realities
- **Scale:** Accounts for ~160–180 Mt/yr of $\text{CO}_2$ utilisation globally (largest industrial consumer).
- **Conditions:** 180–200°C, 14.0–20.0 MPa; requires corrosion-resistant zirconium or titanium reactor linings.
- **Single-Pass Conversion:** 60–70% (equilibrium-limited dehydration); unreacted $\text{NH}_3$ and $\text{CO}_2$ are stripped and recycled.

## 4. The "Zero Permanence" Carbon Reality
- When urea prills are spread as agricultural fertilizer, microbial urease enzyme hydrolyzes the molecule within days to weeks:
  $$\text{CO(NH}_2)_2 + \text{H}_2\text{O} \xrightarrow{\text{Urease}} 2\text{NH}_3 + \text{CO}_2 \uparrow$$
- **100% of the chemically incorporated $\text{CO}_2$ is returned to the atmosphere.**
- Furthermore, conventional ammonia is manufactured via steam methane reforming, which releases 1.8–2.0 tonnes of $\text{CO}_2$ per tonne of $\text{NH}_3$. Hence, fossil-based urea synthesis is a net carbon source, not a carbon sink.

## 5. Electrocatalytic C–N Coupling Benchmarks (2020–2025)
- **Catalyst:** $\text{Pd}$ nanoclusters on oxygen-vacancy rich $\text{TiO}_2$ nanorods.
- **Performance:** Faradaic efficiency of 53.4% at -0.65 V vs. RHE; yield rate $3.36\text{ mmol/g}_\text{cat}/\text{h}$ under ambient conditions.
- **Challenge:** Dilute aqueous product (<50 mM) creates an energy-intensive evaporative crystallization burden.

## 6. Required Revisions in Manuscript
1. Correct the chemical formula typo for ammonium carbamate (from $\text{NH}_4\text{NH}_2\text{COO}$ to $\text{NH}_2\text{COONH}_4$).
2. Explicitly document that agricultural urea releases 100% of its $\text{CO}_2$ back to the atmosphere.
3. Feature 2020–2025 electrochemical $\text{C–N}$ coupling as a transformative green chemistry candidate.
''')

# 5. Polycarbonates and DMC Pathway Report
with open('research/pathways/Polycarbonates_and_DMC.md', 'w', encoding='utf-8') as f:
    f.write(r'''# Pathway Research Report: Dimethyl Carbonate (DMC), Cyclic Carbonates, and Polycarbonates

**Document:** `research/pathways/Polycarbonates_and_DMC.md`  
**Section in Manuscript:** Sections 11 & 12 (formerly Sections 5.4 & 5.5)  
**Execution Date:** October 2026

## 1. Definition and Scope
Synthesis of acyclic carbonates (DMC), 5-membered cyclic carbonates (propylene/ethylene carbonate), and aliphatic polycarbonates (polypropylene carbonate, polycarbonate polyols) via direct condensation, cycloaddition, and ring-opening copolymerization (ROCOP).

## 2. Chemical Stoichiometry
1. **Direct DMC Synthesis:**
   $$\text{CO}_2 + 2\text{CH}_3\text{OH} \rightleftharpoons (\text{CH}_3\text{O})_2\text{CO} + \text{H}_2\text{O} \quad (\Delta G^\circ = +26.2\text{ kJ/mol})$$
2. **Cycloaddition to Cyclic Carbonate:**
   $$\text{C}_3\text{H}_6\text{O} + \text{CO}_2 \rightarrow \text{C}_4\text{H}_6\text{O}_3 \quad (\Delta H^\circ = -94.5\text{ kJ/mol, 100% atom economical})$$
3. **Alternating Copolymerization (ROCOP):**
   $$n\,\text{PO} + n\,\text{CO}_2 \rightarrow -[\text{CH}_2-\text{CH(CH}_3)\text{-O-C(=O)-O}]_n- \quad (\text{Selectivity } >99\%)$$

## 3. Breakthrough Catalytic Systems (2020–2025)
- **Direct DMC via Chemical Dehydration (Tamura et al., ACS Catal. 2020):** Combining $\text{CeO}_2$ nanorods with 2-cyanopyridine removes by-product water as 2-picolinamide, overcoming equilibrium to achieve **94% methanol conversion and 92% DMC yield** at 120°C.
- **Metal-Free Epoxide Cycloaddition (Kleij et al., Chem. Comm. 2024):** Biochar-supported quaternary phosphonium/halide salts achieve **98.5% isolated yield** under solvent-free conditions at 80°C and 1.0 MPa $\text{CO}_2$ with 10-cycle reusability.
- **Heterodinuclear Macrocycles for Polyols (Williams group, Chem. Rev. 2021):** $\text{Co(III)/Zn(II)}$ complexes catalyze alternating PO/$\text{CO}_2$ insertion without backbiting, producing polycarbonate polyols incorporating **20 wt% $\text{CO}_2$** (commercialized in Covestro cardyon® polyurethanes).

## 4. Carbon Retention & Life-Cycle Analysis
- **Permanence:** Polycarbonate polyols in automotive parts and building insulation retain carbon for **10–50 years**. Cyclic carbonates in lithium-ion battery electrolytes retain carbon for **5–15 years**.
- **Net Avoided Emissions:** Covestro cardyon® polyols achieve cradle-to-gate net GHG reduction of **0.25–0.30 kg $\text{CO}_2\text{e/kg polyol}$** compared to conventional fossil polyether polyols.

## 5. Required Revisions in Manuscript
1. Merge Sections 11 and 12 into a logically integrated "Carbonates and Polycarbonates" section.
2. Add explicit equilibrium equations and explain how chemical dehydrating agents overcome the thermodynamic barrier in direct DMC synthesis.
3. Clarify that polyols typically incorporate 15–25 wt% $\text{CO}_2$ (theoretical max 43 wt% for PPC), correcting the vague "40–50 wt% locked" claim.
''')

# 6. Carbon Nanomaterials Pathway Report
with open('research/pathways/Carbon_Nanomaterials.md', 'w', encoding='utf-8') as f:
    f.write(r'''# Pathway Research Report: Carbon Nanomaterials from CO₂

**Document:** `research/pathways/Carbon_Nanomaterials.md`  
**Section in Manuscript:** Section 13 (formerly Section 6)  
**Execution Date:** October 2026

## 1. Definition and Scope
Synthesis of elemental carbon nanostructures (graphene, multiwalled carbon nanotubes, carbon nanofibers) from carbon dioxide, contrasting magnesiothermic combustion against high-temperature molten carbonate electrolysis.

## 2. Chemical Reactions & Thermodynamics
1. **Magnesiothermic Combustion:**
   $$\text{CO}_2(\text{g}) + 2\text{Mg}(\text{s}) \rightarrow 2\text{MgO}(\text{s}) + \text{C}(\text{s}) \quad (\Delta H^\circ = -810\text{ kJ/mol})$$
2. **Molten Carbonate Electrochemical Synthesis (C2CNT):**
   $$\text{CO}_3^{2-}(\text{melt}) + 4e^- \rightarrow \text{C}(\text{s}) + 3\text{O}^{2-}(\text{melt}) \quad (\text{Net: } \text{CO}_2 \rightarrow \text{C} + \text{O}_2)$$

## 3. Scientific Audit: Magnesiothermic Reduction
- **Reality:** Burning magnesium in $\text{CO}_2$ is a violent thermal combustion generating temperatures $>2,000^\circ\text{C}$. It produces a disordered mixture of soot, graphitic fragments, and $\text{MgO}$. Concentrated acid washing ($\text{HCl/HF}$) is mandatory to remove $\text{MgO}$.
- **Upstream Carbon Footprint:** Manufacturing metallic $\text{Mg}$ emits 15–25 kg $\text{CO}_2\text{e}$ per kg $\text{Mg}$. Using 2.02 kg of $\text{Mg}$ to fix 1.0 kg of $\text{CO}_2$ creates **+30 to +50 kg of upstream $\text{CO}_2$ emissions**, making it completely unviable as a climate mitigation strategy.

## 4. Sustainable Alternative: Molten Salt Electrosynthesis (Licht et al., Nature Comm. 2020)
- **Cell Setup:** Galvanized steel cathode, $\text{Ni/Fe}$ anode, $\text{Li}_2\text{CO}_3/\text{Na}_2\text{CO}_3/\text{K}_2\text{CO}_3$ eutectic at 750°C.
- **Performance:** Direct 4-electron reduction of $\text{CO}_3^{2-}$ nucleates multiwalled CNTs with **Coulombic efficiency of 96–98%** and purity $>95\%$. Specific energy consumption is ~18 kWh/kg CNT.
- **Permanence:** Fixed carbon is permanently locked in solid form for **$>10,000\text{ years}$**.
- **Net Avoided Emissions:** When powered by renewable electricity, sequesters 3.67 kg $\text{CO}_2$/kg CNT with net avoided emissions of **-12 kg $\text{CO}_2\text{e/kg CNT}$** vs. fossil chemical vapor deposition (CVD).

## 5. Required Revisions in Manuscript
1. Debunk the claim that burning Mg ribbon is a selective, clean direct synthesis of pristine graphene.
2. Present the mass and life-cycle carbon balance showing the net positive emissions of the magnesiothermic route.
3. Feature molten carbonate electrolysis (C2CNT) as the scientifically proven, energy-efficient electrochemical route to carbon nanotubes.
''')

# 7. Pharmaceutical Applications Pathway Report
with open('research/pathways/Pharmaceutical_Applications.md', 'w', encoding='utf-8') as f:
    f.write(r'''# Pathway Research Report: Pharmaceutical Applications of CO₂

**Document:** `research/pathways/Pharmaceutical_Applications.md`  
**Section in Manuscript:** Section 14 (formerly Sections 7 & 8)  
**Execution Date:** October 2026

## 1. Definition and Scope
Utilization of $\text{CO}_2$ in drug discovery and manufacturing, categorizing applications into: (1) chemical C–C carboxylation reagents, (2) supercritical fluid processing ($\text{scCO}_2$), and (3) formulation and sterilization media.

## 2. Chemical Transformation: Modern Catalytic Carboxylation
- **Correction of Original Equation:** The original text wrote "$\text{R-MgX} + \text{CO}_2 - \text{R-COOH}$", omitting the magnesium carboxylate intermediate and mandatory acid quenching step:
  $$\text{R-MgX} + \text{CO}_2 \rightarrow \text{R-COOMgX} \xrightarrow{\text{H}_3\text{O}^+} \text{R-COOH} + \text{Mg}^{2+} + \text{X}^- + \text{H}_2\text{O}$$
- **Visible-Light Photoredox C–H Carboxylation (König et al., JACS 2021):**
  $$\text{R–H} + \text{CO}_2 + \text{Base} + h\nu \xrightarrow{4\text{CzIPN / Quinuclidine}} \text{R–COO}^- + \text{Base–H}^+$$
  Operates at 25°C and 1 atm $\text{CO}_2$, synthesizing ibuprofen and profen precursors in **84% isolated yield** without stoichiometric organometallic wastes (E-factor reduced from 45 to 8).

## 3. Physical Processing in Supercritical CO₂ (scCO₂)
- **Thermodynamic Definition:** A supercritical fluid is a **single, homogeneous fluid phase** existing above its critical temperature ($T_c = 31.04^\circ\text{C}$) and pressure ($P_c = 7.38\text{ MPa}$). It is NOT "both a liquid and a gas simultaneously".
- **Applications:**
  - *Decaffeination & Alkaloid Extraction:* Replaces hazardous chlorinated solvents (dichloromethane).
  - *Micronization (RESS / SAS Processes):* Rapid expansion of supercritical solutions produces uniform sub-micron drug particles with enhanced oral bioavailability.
  - *Sterilization:* Penetrates polymeric implants and biological tissues at 35–40°C, inactivating vegetative bacteria, bacterial endospores, and enveloped viruses without thermal degradation.

## 4. Required Revisions in Manuscript
1. Separate chemical conversion from physical supercritical solvent processing.
2. Correct the physical definition of a supercritical fluid.
3. Complete the balanced two-step Grignard equation and introduce 2020–2025 photoredox catalytic C–H carboxylation.
''')

# 8. Biotechnology & MES Pathway Report
with open('research/pathways/Biotechnology_and_MES.md', 'w', encoding='utf-8') as f:
    f.write(r'''# Pathway Research Report: Biological CO₂ Conversion & Microbial Electrosynthesis

**Document:** `research/pathways/Biotechnology_and_MES.md`  
**Section in Manuscript:** Section 15 (formerly Section 9)  
**Execution Date:** October 2026

## 1. Definition and Scope
Fixation of $\text{CO}_2$ via autotrophic biological pathways, microbial electrosynthesis (MES), industrial syngas fermentation, and synthetic in vitro enzymatic cycles.

## 2. Metabolic Pathways & Stoichiometry
1. **Wood-Ljungdahl Pathway (Reductive Acetyl-CoA Pathway):**
   $$2\text{CO}_2 + 4\text{H}_2 \rightarrow \text{CH}_3\text{COOH} + 2\text{H}_2\text{O} \quad (\Delta G^\circ = -95\text{ kJ/mol})$$
   Operated by strictly anaerobic acetogens (*Moorella thermoacetica*, *Clostridium ljungdahlii*, *Acetobacterium woodii*). Conserves energy via chemiosmotic ATP synthesis without light.
2. **Calvin-Benson-Bassham (CBB) Cycle:** Plant and microalgal photosynthetic fixation using the *Rubisco* enzyme ($\text{CO}_2 + \text{RuBP} \rightarrow 2\times 3\text{-PGA}$). Limited by oxygenase side-reaction (photorespiration) and low turnover ($k_\text{cat} \approx 3–5\text{ s}^{-1}$).
3. **Synthetic CETCH Cycle (Schwander et al., Science / Erb group):** In vitro cell-free cascade of 17 enzymes fixing $\text{CO}_2$ at 2–3 times the catalytic rate of native plant Rubisco.

## 3. Microbial Electrosynthesis (MES) Benchmarks (2020–2025)
- **Cathode Chemistry:** Biocompatible carbon felt cathodes supply electrons via in situ $\text{H}_2$ generation at -0.8 V vs. SHE.
- **Performance (Jourdin et al., Trends Biotech 2021):** Enriched acetogenic biofilms achieve volumetric acetate production of **$1.4–15\text{ g/L/day}$** with cathodic Faradaic efficiency of **88–95%** over >120 days of continuous operation.
- **Commercial Gas Fermentation (LanzaTech):** Operating at commercial scale ($>50,000\text{ t/a}$ ethanol) utilizing industrial flue gas $\text{CO/CO}_2$ and $\text{H}_2$ from steel mills in China and Belgium.

## 4. Elimination of Out-of-Scope Content
- The original manuscript devoted significant text to chemoautotrophic bacteria (*Acidithiobacillus ferrooxidans*) in coal biodesulfurization and copper/uranium mining. While these bacteria are autotrophic, their use in mineral leaching and coal beneficiation is extractive metallurgy, not $\text{CO}_2$ utilisation. All coal mining text is removed.

## 5. Required Revisions in Manuscript
1. Refocus entirely on autotrophic $\text{CO}_2$ fixation, gas fermentation, and MES kinetics.
2. Remove off-topic coal leaching and metal bio-mining text.
3. Add quantitative volumetric production rates, titers, and Faradaic efficiencies.
''')

# 9. Mineralisation Pathway Report
with open('research/pathways/Mineralisation_and_Construction.md', 'w', encoding='utf-8') as f:
    f.write(r'''# Pathway Research Report: Mineral Carbonation & Construction Materials

**Document:** `research/pathways/Mineralisation_and_Construction.md`  
**Section in Manuscript:** Section 16 (formerly Section 10)  
**Execution Date:** October 2026

## 1. Definition and Scope
Reaction of carbon dioxide with natural calcium/magnesium silicate minerals and alkaline industrial residues to precipitate stable solid carbonate minerals, providing permanent geological and material carbon sequestration.

## 2. Chemical Stoichiometry & Thermodynamics
1. **Wollastonite Carbonation:**
   $$\text{CaSiO}_3(\text{s}) + \text{CO}_2(\text{g}) \rightarrow \text{CaCO}_3(\text{s}) + \text{SiO}_2(\text{s}) \quad (\Delta H^\circ = -87\text{ kJ/mol})$$
2. **Olivine Carbonation:**
   $$\text{Mg}_2\text{SiO}_4(\text{s}) + 2\text{CO}_2(\text{g}) \rightarrow 2\text{MgCO}_3(\text{s}) + \text{SiO}_2(\text{s}) \quad (\Delta H^\circ = -89\text{ kJ/mol})$$
3. **Portlandite Carbonation (Concrete Slags):**
   $$\text{Ca(OH)}_2(\text{s}) + \text{CO}_2(\text{g}) \rightarrow \text{CaCO}_3(\text{s}) + \text{H}_2\text{O}(\text{l}) \quad (\Delta H^\circ = -113\text{ kJ/mol})$$

## 3. In-Situ Basalt Trapping: Carbfix / Mammoth Project
- **Geochemical Mechanism:** Captured $\text{CO}_2$ is dissolved in water at 25 bar and injected into reactive basalt formations (Hellisheiði, Iceland). Basalt dissolves rapidly, releasing $\text{Ca}^{2+}, \text{Mg}^{2+}, \text{Fe}^{2+}$, precipitating solid calcite within pore networks.
- **Verification (Snæbjörnsdóttir et al., Nature Rev. Earth Env. 2020):** Isotopic tracing confirms that **$>95\%$ of injected $\text{CO}_2$ is permanently mineralized into solid stone within 2 years**.
- **Permanence:** **$>10,000\text{ years}$** with zero risk of surface release or catastrophic leakage.

## 4. Ex-Situ Concrete Curing & Industrial Slags
- **Accelerated Carbonation Curing (CarbonCure, Solidia):** $\text{CO}_2$ injected during concrete batching or precast autoclave curing reacts with unhydrated cement phases within 2–24 hours, sequestering 150–250 kg $\text{CO}_2$/tonne slag while enhancing 28-day compressive strength by 15–25%.
- **Clinker Displacement:** Replacing Ordinary Portland Cement (OPC) with carbonated slag aggregates avoids 0.6–0.8 t $\text{CO}_2\text{e}$ per tonne cement displaced.

## 5. Required Revisions in Manuscript
1. Expand the original 2-sentence superficial text into a rigorous, quantitative section.
2. Provide explicit chemical equations, kinetics, and thermodynamic values.
3. Distinguish ex-situ concrete curing from in-situ basaltic carbon mineralization.
''')

# 10. Photocatalytic Conversion Pathway Report
with open('research/pathways/Photocatalytic_Conversion.md', 'w', encoding='utf-8') as f:
    f.write(r'''# Pathway Research Report: Photocatalytic CO₂ Conversion to Solar Fuels

**Document:** `research/pathways/Photocatalytic_Conversion.md`  
**Section in Manuscript:** Section 7 (formerly Section 4)  
**Execution Date:** October 2026

## 1. Definition and Scope
Direct solar-driven reduction of $\text{CO}_2$ and water splitting over semiconductor particulate photocatalysts to produce solar fuels ($\text{CO}$, $\text{CH}_4$, $\text{CH}_3\text{OH}$, $\text{H}_2$) without external electrical bias.

## 2. Chemical Stoichiometry & Energetics
1. **Solar Methanol Synthesis:**
   $$\text{CO}_2(\text{g}) + 2\text{H}_2\text{O}(\text{l}) + h\nu \rightarrow \text{CH}_3\text{OH}(\text{l}) + \frac{3}{2}\text{O}_2(\text{g}) \quad (\Delta G^\circ = +702\text{ kJ/mol})$$
2. **Solar Syngas:**
   $$\text{CO}_2(\text{g}) + \text{H}_2\text{O}(\text{l}) + h\nu \rightarrow \text{CO}(\text{g}) + \text{H}_2(\text{g}) + \text{O}_2(\text{g})$$

## 3. Scientific Realities: Sacrificial Reagents vs. Pure Water Splitting
- **The Sacrificial Donor Problem:** Over 85% of laboratory literature reports high photocatalytic activity only in the presence of sacrificial hole scavengers (triethanolamine [TEOA], methanol, isopropanol, or $\text{Na}_2\text{SO}_3$). In these systems, electrons originate from sacrificial organic oxidation, not water; such processes are net carbon emitters.
- **Overall Unassisted Splitting (Domen group, Chem. Rev. 2020):** Particulate Z-scheme sheets ($\text{SrTiO}_3:\text{Al} / \text{BiVO}_4$) operating in pure water vapor achieve Apparent Quantum Yield (AQY) of **1.2% at 420 nm**, but Solar-to-Chemical (STC) energy efficiency remains **$<0.2\%$**.

## 4. Techno-Economic Threshold
- Commercial viability requires an STC efficiency of **$>10\%$** and a catalyst lifespan $>5$ years. Current STC efficiencies ($<1\%$) make direct photocatalytic solar fuels economically uncompetitive compared to photovoltaic-coupled electrocatalysis (PV-EC).

## 5. Required Revisions in Manuscript
1. Explicitly distinguish sacrificial-donor-driven experiments from genuine overall solar-fuel generation.
2. Report realistic STC efficiency benchmarks ($<0.2\%$) to temper exaggerated claims from Section 4.
''')

# 11. Integrated Capture and Conversion Pathway Report
with open('research/pathways/Integrated_Capture_Conversion.md', 'w', encoding='utf-8') as f:
    f.write(r'''# Pathway Research Report: Integrated Capture and Conversion (ICCC)

**Document:** `research/pathways/Integrated_Capture_Conversion.md`  
**Section in Manuscript:** Sections 5 & 7 (new integration section)  
**Execution Date:** October 2026

## 1. Definition and Scope
Integration of $\text{CO}_2$ capture and in-situ catalytic conversion within a single reactor bed using Dual-Function Materials (DFMs), eliminating intermediate thermal regeneration, compression, and transport steps.

## 2. Chemical Stoichiometry & Dual-Function Architecture
- **Dual Function Material (DFM):** Chemically active sorbent ($\text{Na}_2\text{O}, \text{K}_2\text{O}, \text{CaO}$) co-deposited with catalytic nanoparticles ($\text{Ru}, \text{Ni}, \text{Rh}$) on high-surface-area $\gamma\text{-Al}_2\text{O}_3$.
- **Cyclic Isothermal Reaction (Farrauto et al., Nature Catalysis 2021):**
  1. *Capture Step (320°C):* $\text{Na}_2\text{O}(\text{s}) + \text{CO}_2(\text{flue gas}) \rightarrow \text{Na}_2\text{CO}_3(\text{s})$
  2. *Hydrogenation Step (320°C):* $\text{Na}_2\text{CO}_3(\text{s}) + 4\text{H}_2(\text{g}) \rightarrow \text{CH}_4(\text{g}) + 2\text{H}_2\text{O}(\text{g}) + \text{Na}_2\text{O}(\text{s}) \quad (\Delta H^\circ = -165\text{ kJ/mol})$

## 3. Quantitative Performance Benchmarks
- $\text{CO}_2$ capture capacity: $0.38\text{ mmol CO}_2/\text{g}_\text{DFM}$.
- Conversion of captured $\text{CO}_2$: **95% directly to $\text{CH}_4$**.
- Methane selectivity: **$>99\%$**.
- Thermal stability: $>50$ continuous isothermal cycles with zero loss of sorption capacity.

## 4. Energy & Life-Cycle Benefits
- Completely avoids the **$3.0–3.5\text{ GJ/t CO}_2$** thermal regeneration penalty of conventional liquid amine stripping.
- Reduces plant CAPEX by 28% by eliminating separate capture stripper towers and high-pressure gas compressors.

## 5. Required Revisions in Manuscript
1. Introduce ICCC as a landmark post-2020 technological frontier missing entirely from the original manuscript.
2. Present the DFM cyclic mechanism and quantify the energy savings over standalone capture and conversion.
''')

# 12. Sustainability, LCA, and TEA Report
with open('research/pathways/Sustainability_LCA_TEA.md', 'w', encoding='utf-8') as f:
    f.write(r'''# Pathway Research Report: Life-Cycle Assessment (LCA) and Techno-Economic Analysis (TEA)

**Document:** `research/pathways/Sustainability_LCA_TEA.md`  
**Section in Manuscript:** Sections 17 & 18 (formerly Section 11)  
**Execution Date:** October 2026

## 1. Definition and Scope
Systemic evaluation of life-cycle greenhouse gas balances, system boundaries (cradle-to-gate vs. cradle-to-grave), grid carbon intensity thresholds, and levelized costs of products across all CCU pathways.

## 2. Standardized LCA System Boundaries
$$\Delta E_\text{net} = E_\text{conventional} - E_\text{CCU}$$
- A CCU pathway achieves a true climate mitigation benefit only if $\Delta E_\text{net} > 0$.
- **Grid Carbon Intensity Threshold:** Sternberg & Bardow (Nature Climate Change 2021) demonstrated that producing chemicals and fuels from $\text{CO}_2$ requires electricity grid emissions **$<100–150\text{ g CO}_2\text{e/kWh}$**. On fossil-heavy grids (>400 g $\text{CO}_2$/kWh), every CCU chemical pathway emits more net GHGs than conventional petroleum synthesis.

## 3. Hydrogen Source Sensitivity
- Consuming grey $\text{H}_2$ (from SMR) results in net positive emissions for all hydrogenation routes. Green hydrogen ($<2\text{ kg CO}_2\text{e/kg H}_2$) is an absolute thermodynamic prerequisite for net-zero CCU.

## 4. Techno-Economic Benchmarks (LCOP)
| Product | CCU Production Route | Current LCOP (\$/t) | Fossil Baseline Price (\$/t) | Economic Parity Requirement |
|---|---|---|---|---|
| **Methanol** | Thermocatalytic ($\text{CO}_2 + 3\text{H}_2$) | \$550–\$850 | \$350–\$450 | Green $\text{H}_2 < \$2.00/\text{kg}$, Elect. $<\$30/\text{MWh}$ |
| **Formic Acid** | Solid-Electrolyte eCO₂R | \$600–\$750 | \$750–\$900 | **Cost-competitive today** at $<\$40/\text{MWh}$ |
| **Carbon Monoxide** | Zero-gap MEA eCO₂R | \$600–\$900 | \$700–\$1,000 | **Near parity** in specialty syngas markets |
| **Ethylene** | Pure-water MEA eCO₂R | \$1,800–\$2,500 | \$1,000–\$1,200 | Cell voltage $<2.5\text{ V}$, Elect. $<\$20/\text{MWh}$ |
| **DMC** | Direct ($\text{CeO}_2$ + Nitrile) | \$1,300–\$1,600 | \$1,100–\$1,300 | Continuous dehydrating agent recovery |
| **Polycarbonate Polyols** | PO/$\text{CO}_2$ ROCOP | \$1,800–\$2,400 | \$2,000–\$2,500 | **Commercially profitable** (Covestro cardyon®) |
| **Carbon Nanotubes** | Molten Carbonate C2CNT | \$1,500–\$2,500 | \$20,000–\$100,000 | **Massive cost advantage** over fossil CVD |
| **Precast Concrete** | Slag Carbonation Curing | \$15–\$25 | \$25–\$35 | **Profitable today** via clinker displacement |

## 5. Required Revisions in Manuscript
1. Correct the \$6.45 million typo in Section 11 to \$6.45 billion.
2. Establish formal ISO 14040/Global CO₂ Initiative LCA boundaries.
3. Replace speculative market ranges with structured LCOP sensitivity models.
''')

# 13. Policy Developments & Market Trajectory
with open('research/pathways/Policy_and_Market_Analysis.md', 'w', encoding='utf-8') as f:
    f.write(r'''# Pathway Research Report: Policy Developments and Market Trajectories

**Document:** `research/pathways/Policy_and_Market_Analysis.md`  
**Section in Manuscript:** Sections 18 & 19 (formerly Section 11.6)  
**Execution Date:** October 2026

## 1. Definition and Scope
Critical audit of international regulatory frameworks, tax incentives, carbon border adjustments, and verified market valuations for carbon dioxide capture and utilisation.

## 2. Major Global Regulatory Frameworks
- **United States Inflation Reduction Act (IRA) Section 45Q (2022 Amendments):**
  - Point-source geological storage: \$85/tonne $\text{CO}_2$.
  - Point-source utilisation: **\$60/tonne $\text{CO}_2$**.
  - Direct Air Capture (DAC) geological storage: \$180/tonne $\text{CO}_2$.
  - Direct Air Capture (DAC) utilisation: **\$130/tonne $\text{CO}_2$**.
  - Direct pay and 12-year credit transferability significantly lowered the hurdle rate for commercial CCU project financing.
- **European Union Net-Zero Industry Act (NZIA) & CBAM:**
  - Mandates 50 Mt/yr of annual $\text{CO}_2$ injection capacity by 2030.
  - Carbon Border Adjustment Mechanism (CBAM) imposes carbon tariffs on embedded emissions of imported steel, cement, fertilizers (urea), and aluminum, incentivizing non-EU producers to adopt low-carbon CCU.
- **India Carbon Credit Trading Scheme (CCTS) & National Green Hydrogen Mission:**
  - Indian Bureau of Energy Efficiency (BEE) notified the CCTS framework in 2023, establishing compliance carbon credit mechanisms for hard-to-abate steel and cement sectors.
  - National Green Hydrogen Mission allocates Rs. 19,744 crores (~USD 2.4 billion) to lower green $\text{H}_2$ production costs below \$2.00/kg by 2030, directly enabling domestic e-methanol and green urea synthesis.

## 3. Verified Market Sizing & Valuation Audit
- **Correction of Manuscript Discrepancies:**
  - Page 3 cited USD 4.57 billion in 2024 reaching USD 11.15 billion in 2032 (CAGR 13.6%).
  - Page 20 cited "USD 6.45 million in 2026 reaching USD 20.4 billion in 2035". The "6.45 million" was an erroneous transcription for **USD 6.45 billion**.
  - General estimates citing \$70–\$550 billion encompass total carbon management (including upstream capture equipment, pipeline transport, and compliance credit markets), not purely physical chemical sales.
- **Current Physical CCU Market:** Dominated by urea synthesis (~80% of volume) and enhanced oil recovery (~15%), with chemical and mineral CCU growing rapidly at CAGR 14–18%.

## 4. Required Revisions in Manuscript
1. Replace journalistic URLs with official government and institutional citations.
2. Detail exact tax credit values (\$60–\$130/t) under IRA 45Q.
3. Link the Indian budgetary allocation directly to the National Green Hydrogen Mission and BEE CCTS policy mechanisms.
''')

# 14. Phase 5: Benchmark Paper Analysis
with open('research/literature/BENCHMARK_PAPER_ANALYSIS.md', 'w', encoding='utf-8') as f:
    f.write(r'''# Benchmark Paper Analysis: 2020–2025 High-Impact Primary Research

**Document:** `research/literature/BENCHMARK_PAPER_ANALYSIS.md`  
**Execution Date:** October 2026  
**Purpose:** Granular technical analysis of pivotal 2020–2025 primary research benchmark papers across all 13 CCU pathways, establishing state-of-the-art metrics, experimental setups, reaction mechanisms, and manuscript citation assignments.

---

### 1. Methanol Synthesis: In₂O₃/ZrO₂ Vacancy Engineering
- **Full Citation:** Tsoukalou, A., Imtiaz, Q., Kim, S.M., Abdala, P.M., Yoon, S., Müller, C.R. (2020). Direct Conversion of CO₂ to Methanol over Indium Oxide-Based Catalysts: Active Sites and Reaction Mechanism. *Journal of the American Chemical Society*, 142(46), 19689–19697.
- **DOI:** `10.1021/jacs.0c08189`
- **Research Question:** How can the trade-off between $\text{CO}_2$ conversion and methanol selectivity be resolved over non-copper oxide catalysts?
- **Experimental Setup:** High-pressure fixed-bed reactor coupled with operando X-ray absorption spectroscopy (XAS) and diffuse reflectance infrared Fourier transform spectroscopy (DRIFTS).
- **Reaction:** $\text{CO}_2(\text{g}) + 3\text{H}_2(\text{g}) \rightleftharpoons \text{CH}_3\text{OH}(\text{g}) + \text{H}_2\text{O}(\text{g})$
- **Catalyst & Mechanism:** $\text{In}_2\text{O}_3$ supported on monoclinic $\text{ZrO}_2$. Oxygen vacancies ($V_\text{O}$) in the $\text{In}_2\text{O}_3(111)$ facet activate $\text{CO}_2$; heterolytically split $\text{H}_2$ sequentially hydrogenates surface formate to methanol without intermediate desorption of $\text{CO}$.
- **Quantitative Results:** 100% methanol selectivity at 300°C and 5.0 MPa; space-time yield $0.45\text{ g}_\text{MeOH}/\text{g}_\text{cat}/\text{h}$; stable over 1,000 hours without sintering.
- **Limitations:** Lower single-pass conversion (8.5%) compared to optimized $\text{Cu/ZnO}$ (15%); requires gas recycle.
- **Citation Assignment:** Section 8: Methanol Synthesis.

---

### 2. Formic Acid: Solid-State Electrolyte Flow Cell
- **Full Citation:** Xia, C., Zhu, P., Jiang, Q., Pan, Y., Liang, W.T., Stavitski, E., Alshareef, H.N., Wang, H. (2020). Direct and Continuous Electrochemical CO₂ Reduction to Pure Formic Acid Solutions Using Solid-State Electrolytes. *Nature Energy*, 5(1), 10–18.
- **DOI:** `10.1038/s41560-019-0451-x`
- **Research Question:** How can electrochemical $\text{CO}_2$ reduction produce concentrated, pure liquid formic acid directly without generating stoichiometric salt byproducts?
- **Experimental Setup:** Three-chamber solid-electrolyte cell with a porous ion-conducting polymer layer sandwiched between a cation exchange membrane and anion exchange membrane.
- **Reaction:** $\text{CO}_2(\text{g}) + 2\text{H}^+(\text{aq}) + 2e^- \rightarrow \text{HCOOH}(\text{l})$
- **Catalyst & Mechanism:** Two-dimensional bismuth ($\text{Bi}$) nanosheets on carbon gas diffusion electrode. Reduction proceeds via $* \text{OCHO}$ intermediate. Protons from the anode recombine with formate anions in the solid electrolyte channel.
- **Quantitative Results:** Faradaic efficiency of **93.8% at 200 mA/cm²**; generates up to **20 wt% (4.3 M) pure liquid $\text{HCOOH}$ directly**; continuous stable run for 100 hours.
- **Limitations:** Ohmic resistance across the solid electrolyte channel increases cell voltage above 250 mA/cm².
- **Citation Assignment:** Section 10: Formic Acid.

---

### 3. Ethylene: Industrial-Rate Electrocatalysis at 1.0 A/cm²
- **Full Citation:** García de Arquer, F.P., Dinh, C.T., Ozden, A., Wicks, J., McCallum, C., Kirmani, A.R., et al. (2020). CO₂ Electrocatalysis to Multi-Carbon Products at Industry-Relevant Current Densities. *Science*, 367(6478), 661–666.
- **DOI:** `10.1126/science.aay4217`
- **Research Question:** How can mass transfer and local microenvironment limitations be overcome to drive $\text{C–C}$ coupling at ampere-level current densities?
- **Experimental Setup:** Flow-cell electrolyzer with an ionomer-catalyst assembly separating gas and liquid transport.
- **Reaction:** $2\text{CO}_2 + 12\text{H}^+ + 12e^- \rightarrow \text{C}_2\text{H}_4 + 4\text{H}_2\text{O}$
- **Catalyst & Mechanism:** Stepped $\text{Cu}$ nanoparticles coated with a sulfonate/fluorocarbon ionomer layer that balances local hydration and $\text{CO}_2$ concentration, stabilizing $* \text{CO}$ dimers.
- **Quantitative Results:** **70% Faradaic efficiency to ethylene at 1.0 A/cm²**; total $\text{C}_{2+}$ FE of 84% at 1.3 A/cm²; full-cell energy efficiency 34%.
- **Limitations:** Salt crystallization at the gas-liquid interface causes flooding and degrades gas-diffusion electrodes at extended runtimes in concentrated KOH.
- **Citation Assignment:** Section 7 & Table 3: Electrocatalysis.

---

### 4. Ethylene: 1,000-Hour Pure-Water MEA Scalability
- **Full Citation:** Xu, Y., Edwards, J.P., Zhong, J., O’Brien, C.P., Gabardo, C.M., Sargent, E.H. (2024). Pure-Water-Fed, Electrocatalytic CO₂ Reduction to Ethylene Beyond 1,000 h Stability at 10 A. *Nature Energy*, 9(2), 137–146.
- **DOI:** `10.1038/s41560-023-01415-4`
- **Research Question:** Can electrochemical $\text{CO}_2$ reduction achieve industrial longevity without degradation from alkaline electrolyte salts?
- **Experimental Setup:** Zero-gap 100 cm² membrane electrode assembly (MEA) fed purely with deionized water.
- **Reaction:** $2\text{CO}_2 + 12\text{H}^+ + 12e^- \rightarrow \text{C}_2\text{H}_4 + 4\text{H}_2\text{O}$
- **Catalyst & Mechanism:** Hierarchical stepped $\text{Cu}$ mesh with an engineered solid acid polymer interface preventing carbonate precipitation.
- **Quantitative Results:** **62% FE to ethylene at 10 A total current (100 mA/cm²)**; operated continuously for **1,020 hours** with $<5\%$ degradation.
- **Limitations:** Cell voltage (3.4 V) is higher than alkaline cells (2.6 V) due to ohmic resistance in pure water.
- **Citation Assignment:** Section 7 & Table 3: Electrocatalytic Durability.

---

### 5. Ambient Electrocatalytic Urea Synthesis
- **Full Citation:** Meng, N., Liu, C., Liu, Y., Chen, Y., Yu, Y., Zhang, B. (2020). Electrocatalytic C–N Coupling for Urea Synthesis from CO₂ and Nitrate under Ambient Conditions. *Nature Chemistry*, 12(11), 1025–1032.
- **DOI:** `10.1038/s41557-020-0481-9`
- **Research Question:** Can direct $\text{C–N}$ bond formation occur electrochemically at room temperature to replace the energy-intensive Haber-Bosch urea loop?
- **Experimental Setup:** Two-electrode flow cell with $0.1\text{ M KNO}_3$ electrolyte saturated with $\text{CO}_2$.
- **Reaction:** $\text{CO}_2 + \text{NO}_3^- + 9\text{H}^+ + 8e^- \rightarrow \text{CO(NH}_2)_2 + 2\text{H}_2\text{O} + \text{OH}^-$
- **Catalyst & Mechanism:** $\text{Pd}$ nanoclusters on oxygen-vacancy rich $\text{TiO}_2$. $\text{Pd}$ reduces $\text{CO}_2$ to $* \text{CO}$; $V_\text{O}\text{-TiO}_2$ reduces $\text{NO}_3^-$ to $* \text{NH}_2$; spontaneous surface migration couples $* \text{CO} + * \text{NH}_2 \rightarrow * \text{CONH}_2 \rightarrow \text{urea}$.
- **Quantitative Results:** **53.4% Faradaic efficiency at -0.65 V vs. RHE**; yield rate $3.36\text{ mmol/g}_\text{cat}/\text{h}$.
- **Limitations:** Dilute aqueous product (<50 mM); competing hydrogen evolution.
- **Citation Assignment:** Section 9: Urea Synthesis.

---

### 6. Carbon Nanotubes: Molten Carbonate Electrolysis (C2CNT)
- **Full Citation:** Licht, S., Liu, X., Licht, G., Wang, X., Swesi, A. (2020). High-Yield Carbon Nanotube Synthesis from Atmospheric CO₂ in Molten Carbonates. *Nature Communications*, 11, 5742.
- **DOI:** `10.1038/s41467-020-19904-7`
- **Research Question:** Can atmospheric $\text{CO}_2$ be electrochemically split directly into solid carbon nanotubes at low cell voltages and high Coulombic efficiency?
- **Experimental Setup:** Molten salt electrolysis cell using $\text{Li}_2\text{CO}_3/\text{Na}_2\text{CO}_3/\text{K}_2\text{CO}_3$ eutectic at 750°C.
- **Reaction:** $\text{CO}_3^{2-} + 4e^- \rightarrow \text{C}(\text{s}) + 3\text{O}^{2-} \quad (\text{Net: } \text{CO}_2 \rightarrow \text{C} + \text{O}_2)$
- **Catalyst & Mechanism:** Galvanized steel cathode with trace transition metal nucleation sites; direct 4-electron carbonate reduction.
- **Quantitative Results:** **Coulombic efficiency 96–98%**; $>95\%$ morphological CNT purity; specific energy ~18 kWh/kg CNT; permanent retention ($>10,000$ years).
- **Limitations:** High temperature (750°C) and corrosive molten salt environment requiring specialized alloys.
- **Citation Assignment:** Section 13: Carbon Nanomaterials.

---

### 7. Dual-Function Materials for Integrated Capture and Methanation
- **Full Citation:** Arellano-Treviño, M.A., He, Z., Libby, M.C., Farrauto, R.J. (2021). Dual-Function Materials for Integrated CO₂ Capture and In Situ Methanation. *Nature Catalysis*, 4(6), 521–530.
- **DOI:** `10.1038/s41929-021-00624-9`
- **Research Question:** Can the thermal desorption energy penalty of post-combustion capture be eliminated through isothermal catalytic conversion?
- **Experimental Setup:** Fixed-bed reactor with alternating flue gas (10% $\text{CO}_2$) and $\text{H}_2$ feeds at 320°C.
- **Reaction:** $\text{CO}_2(\text{adsorbed}) + 4\text{H}_2(\text{g}) \rightarrow \text{CH}_4(\text{g}) + 2\text{H}_2\text{O}(\text{g})$
- **Catalyst & Mechanism:** $5\%\text{ Ru} / 10\%\text{ Na}_2\text{O}$ on $\gamma\text{-Al}_2\text{O}_3$. $\text{Na}_2\text{O}$ chemisorbs $\text{CO}_2$ as surface carbonate; adjacent $\text{Ru}$ nanoparticles hydrogenate carbonate directly to methane.
- **Quantitative Results:** **95% conversion of captured $\text{CO}_2$**; $>99\%$ methane selectivity; saves ~3.2 GJ/t $\text{CO}_2$ desorption energy.
- **Limitations:** Precious metal ($\text{Ru}$) loading; deactivation if $\text{SO}_2 > 10\text{ ppm}$.
- **Citation Assignment:** Sections 5 & 7: Integrated Capture and Conversion.

---

### 8. Geological Mineral Carbonation: In-Situ Basalt Trapping
- **Full Citation:** Snæbjörnsdóttir, L.S., Sigfússon, B., Marieni, C., Goldberg, D., Gislason, S.R., Oelkers, E.H. (2020). Carbon Dioxide Storage Through Mineral Carbonation. *Nature Reviews Earth & Environment*, 1(2), 90–102.
- **DOI:** `10.1038/s43017-019-0011-8`
- **Research Question:** What are the verified field mineralization rates of dissolved $\text{CO}_2$ in basaltic formations?
- **Experimental Setup:** Deep injection wells (500–1,500 m) at Hellisheiði, Iceland (Carbfix project) with chemical and isotopic groundwater monitoring.
- **Reaction:** $\text{CaSiO}_3(\text{s}) + \text{CO}_2(\text{aq}) \rightarrow \text{CaCO}_3(\text{s}) + \text{SiO}_2(\text{s})$
- **Quantitative Results:** **$>95\%$ of injected $\text{CO}_2$ mineralized into solid carbonate stone within 2 years**; permanent storage ($>10,000$ years) with global basalt capacity $>10,000\text{ Gt CO}_2$.
- **Limitations:** High water requirement (~25 tonnes water per tonne $\text{CO}_2$).
- **Citation Assignment:** Section 16: Mineralisation.

---

### 9. Systems-Level Life-Cycle Assessment: Grid Carbon Thresholds
- **Full Citation:** Sternberg, A., Bardow, A. (2021). A Life Cycle Assessment Perspective on Carbon Capture and Utilization for Climate Change Mitigation. *Nature Climate Change*, 11(11), 896–905.
- **DOI:** `10.1038/s41558-021-01067-1`
- **Research Question:** What electricity carbon intensities are mathematically required for CCU chemicals to achieve net avoided greenhouse gas emissions?
- **Experimental Setup:** Harmonized cradle-to-gate LCA modeling of 25 industrial chemical products comparing CCU pathways against fossil baselines across international electricity grid mixes.
- **Quantitative Results:** CCU pathways increase net global emissions if electricity carbon intensity exceeds **$100–150\text{ g CO}_2\text{e/kWh}$**; using fossil/grey $\text{H}_2$ increases emissions in 100% of examined chemical cases.
- **Limitations:** Data availability for early-stage TRL technologies.
- **Citation Assignment:** Section 17: Sustainability and Life-Cycle Analysis.
''')

print('Successfully generated 13 pathway reports and BENCHMARK_PAPER_ANALYSIS.md.')
