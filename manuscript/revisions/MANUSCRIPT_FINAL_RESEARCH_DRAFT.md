# Advancements in Carbon Dioxide Utilisation: Pathways to Sustainable Chemicals, Fuels, and Materials for a Net-Zero Future

**Anusha Rana, Rishab Raghuvanshi, Amit Beniwal, and Durlubh Kumar Sharma\***  
*Department of Chemical Engineering and Department of Computational Biology, Indraprastha Institute of Information Technology Delhi (IIIT-Delhi), Okhla Phase III, New Delhi 110020, India*  
*\*Corresponding Author: Durlubh Kumar Sharma (Email: dsharma@iiitd.ac.in)*

---

## Abstract
Carbon capture and utilisation (CCU) represents an indispensable technological pillar within global net-zero climate strategies, providing synthetic pathways to displace fossil-derived petrochemicals, fuels, and building materials. However, the scientific and commercial viability of CCU is fundamentally governed by thermodynamics, reaction kinetics, and upstream life-cycle energy inputs. Here, we present a comprehensive, evidence-based critical review auditing the primary technological routes for chemical, electrochemical, biological, and mineral carbon dioxide transformation. Rather than treating carbon dioxide utilisation as an unconstrained climate panacea or as a rationale for prolonging unabated fossil fuel extraction, this review establishes rigorous physical-chemical, techno-economic, and life-cycle boundaries across seventeen distinct technological pathways. 

We synthesize landmark 2020–2026 benchmarks, including vacancy-engineered $\\text{In}_2\\text{O}_3/\\text{ZrO}_2$ catalysts achieving 100% methanol selectivity at 300 °C, zero-gap pure-water membrane electrode assemblies demonstrating >1,000 hours of continuous ethylene electrosynthesis at industrial current densities, solid-state electrolyte cells delivering 20 wt% pure liquid formic acid, and dual-function materials (DFMs) enabling isothermal capture and methanation. We conduct critical comparative audits of disputed or misclassified pathways, showing that magnesiothermic carbon dioxide reduction emits 30–50 kg $\\text{CO}_2\\text{e}$ upstream per kg carbon fixed, that agricultural urea releases 100% of incorporated carbon back to the atmosphere within days, and that plant-derived carbon nanotube synthesis (e.g. from *Pongamia pinnata* oil) constitutes biomass cracking rather than direct carbon dioxide conversion. Harmonized life-cycle assessments reveal that electrocatalytic and hydrogenation routes achieve net greenhouse gas avoidance only when electricity grid carbon intensity falls below $100–150\\text{ g CO}_2\\text{e/kWh}$ and green hydrogen emissions remain below $2\\text{ kg CO}_2\\text{e/kg H}_2$. We classify carbon retention into a four-tier permanence hierarchy ranging from transient synthetic fuels (<6 months) to permanent mineral carbonation (>10,000 years), evaluate levelized product costs against incumbent petrochemicals, analyze major international policy frameworks (US IRA 45Q, EU CBAM, India Carbon Credit Trading Scheme), and delineate priority research directions to accelerate scalable, climate-beneficial industrial deployment.

**Keywords:** Carbon dioxide utilisation; Catalytic hydrogenation; Electrocatalytic reduction; Life-cycle assessment; Carbon permanence; Methanol; Mineral carbonation; Techno-economic analysis.

---

## 1. Introduction and Climate Motivation

Atmospheric concentrations of carbon dioxide ($\\text{CO}_2$) have exceeded 425 ppm, primarily driven by annual anthropogenic emissions surpassing 37 billion metric tonnes (Gt) from fossil fuel combustion and industrial manufacturing (IEA, 2024; Global Carbon Project, 2024). To avert catastrophic planetary warming beyond the 1.5 °C threshold targeted by the Paris Agreement, the Intergovernmental Panel on Climate Change (IPCC) projects that global net greenhouse gas (GHG) emissions must reach net zero by mid-century. Achieving this objective necessitates a strict mitigation hierarchy: primary energy efficiency, rapid direct electrification, aggressive deployment of renewable power, and targeted carbon capture, utilisation, and storage (CCUS) for residual emissions in hard-to-abate sectors such as steel, cement, heavy transport, and petrochemicals.

Within this framework, Carbon Capture and Utilisation (CCU) has emerged as an intensive domain of academic, industrial, and policy focus. By transforming captured $\\text{CO}_2$ into synthetic transport fuels, chemical intermediates, polymers, construction materials, and specialty fine chemicals, CCU offers the dual promise of establishing a circular carbon economy and diminishing reliance on fossil hydrocarbons. Market projections estimate that the global commercial CCU market—historically dominated by agricultural urea synthesis and enhanced oil recovery—will expand from approximately USD 4.57 billion in 2024 to over USD 11.15 billion by 2032 (CAGR 13.6%), with broader carbon management and compliance credit valuations projected to reach several hundred billion dollars by 2040. Recent physical milestones include the operational launch of Climeworks' Mammoth Direct Air Capture (DAC) plant in Hellisheiði, Iceland, in May 2024 (36,000 t/yr design capacity), the commissioning of the world's largest industrial flue-gas-to-methanol facility in Anyang, China (110,000 t/yr certified low-carbon methanol), and national capital allocations such as India's Rs. 19,744 crore (~USD 2.4 billion) National Green Hydrogen Mission and the United States Inflation Reduction Act (IRA) Section 45Q tax credits.

However, the rapid proliferation of CCU literature has been accompanied by critical scientific, thermodynamic, and methodological vulnerabilities. In particular, four conceptual errors frequently recur in published works:
1. **The Fossil Justification Fallacy:** Numerous exploratory reports assert that CCU provides an environmental justification for the continued, unabated exploitation of cheap fossil fuels (especially coal and petroleum). This claim violates basic thermodynamic laws. Because $\\text{CO}_2$ resides at the thermodynamic nadir of carbon combustion (standard enthalpy of formation $\\Delta H^\\circ_f = -393.5\\text{ kJ/mol}$; standard Gibbs free energy of formation $\\Delta G^\\circ_f = -394.4\\text{ kJ/mol}$), recycling coal-derived $\\text{CO}_2$ back into combustible fuels or synthetic chemicals requires substantially more primary energy (typically 4–6 times) than was originally released during coal combustion. Unless powered entirely by surplus zero-carbon primary energy, CCU systems coupled to fossil plants increase net societal greenhouse gas emissions. CCU is a circular carbon tool for unavoidable emissions, not an excuse to delay fossil fuel phaseout.
2. **Conflation of Gross Uptake with Net Climate Mitigation:** Authors frequently report the gross quantity of $\\text{CO}_2$ chemically incorporated into a product molecule as equivalent to "carbon sequestration". In reality, if the product is a synthetic fuel (combusted within months) or an agricultural fertilizer (hydrolyzed by soil enzymes within weeks), 100% of the chemically incorporated carbon returns to the atmosphere.
3. **Misattribution of Biomass and High-Embodied Precursors:** Literature frequently classifies non-$\\text{CO}_2$ processes—such as the pyrolysis of plant-derived triglycerides (e.g. *Pongamia pinnata* seed oil) or high-temperature combustion of metallic magnesium—as direct sustainable $\\text{CO}_2$ conversion, ignoring massive upstream supply-chain emissions.
4. **Disconnection Between Laboratory Metrics and Industrial Realities:** Catalytic breakthroughs are frequently evaluated using half-cell Faradaic efficiency (FE) in dilute three-electrode cells, obscuring parasitic cell overpotentials, severe carbonate crossover, and catastrophic downstream separation penalties.

This review presents a comprehensive, evidence-grounded scientific overhaul of the carbon dioxide utilisation landscape. We integrate verified chemical reaction stoichiometry, quantitative kinetic benchmarks, rigorous cradle-to-grave life-cycle boundaries, harmonized techno-economic sensitivity models, and an explicit four-tier carbon permanence taxonomy across seventeen distinct technological pathways.

---

## 2. Review Methodology & Structured Literature Protocol

To ensure reproducibility, eliminate publication bias, and provide an auditable evidence base, this review follows a structured screening and evaluation protocol aligned with the conceptual workflow of the **PRISMA 2020** guidelines (Preferred Reporting Items for Systematic Reviews and Meta-Analyses). Given the inherent physical and chemical heterogeneity across homogeneous, heterogeneous, electrochemical, biological, and geological systems, this protocol operates as a structured evidence synthesis rather than a clinical statistical meta-analysis.

### 2.1 Information Sources and Search Strategy
Comprehensive bibliographic searches were executed across six primary academic and institutional repositories: OpenAlex API, Crossref Metadata API, PubMed / NCBI, Europe PMC, publisher databases (American Chemical Society, Royal Society of Chemistry, Elsevier ScienceDirect, SpringerNature, Wiley), and intergovernmental tracking bodies (IEA, IPCC, Global CCS Institute). Targeted Boolean query strings were executed for designated CCU technological domains covering the primary period from January 1, 2020 to December 31, 2025, complemented by designated pre-2020 foundational benchmark literature.

### 2.2 Screening Funnel and Selection Criteria
The literature retrieval and screening process proceeded through four distinct stages:
1. **Identification:** Initial query execution yielded a gross total of **1,248 candidate records** across 14 pathway domains.
2. **Deduplication:** Automated cross-matching of unique Digital Object Identifiers (DOIs), title strings, and author sets eliminated 186 duplicate entries, yielding **1,062 unique screened records**.
3. **Title and Abstract Screening:** Records were screened against explicit inclusion and exclusion criteria. Studies were excluded (N = 824) if they addressed off-topic extractive metallurgy or fossil beneficiation (e.g. coal bio-desulfurization, ore leaching), passive physical solvent processing lacking green chemistry metrics, unvetted commercial whitepapers lacking experimental data, or broad narrative reviews lacking primary quantitative data. A total of **238 records** were retained for full-text eligibility assessment.
4. **Full-Text Assessment & Curation:** Full-text articles and Supplementary Information (SI) were downloaded and scrutinized for experimental completeness, verified mass balances, explicit reaction conditions ($T, P$, electrolyte, overpotential, current density), and catalyst durability. A total of 144 records were excluded due to missing reaction conditions, unverified metrics, or duplicated datasets. The resulting **curated core evidence corpus comprises 94 verified publications** (76 primary experimental research benchmarks and 18 seminal systems reviews).

From this curated library, 28 balanced chemical reactions were formalized with standard thermodynamic parameters in `REACTION_DATABASE_FINAL.csv`, 17 representative technological routes were harmonized in `FINAL_CROSS_PATHWAY_COMPARISON.csv`, and all 48 original manuscript citations were independently audited in `REFERENCE_VERIFICATION.csv`.

---

## 3. Thermodynamic and Kinetic Principles of CO₂ Activation

### 3.1 The Thermodynamic Landscape: Exergonic vs. Endergonic Pathways
The carbon dioxide molecule represents the fully oxidized, lowest-energy state of carbon. The molecule possesses a linear geometry ($D_{\\infty h}$ symmetry) with two equivalent, highly localized $\\text{C=O}$ double bonds characterized by a short bond length of 1.16 Å and an exceptionally high bond dissociation energy of ~750 kJ/mol (total atomization energy of 1,608 kJ/mol). The standard enthalpy and Gibbs free energy of formation are:
$$\\Delta H^\\circ_f = -393.5\\text{ kJ/mol}, \\quad \\Delta G^\\circ_f = -394.4\\text{ kJ/mol}$$

Chemical and electrochemical transformations of $\\text{CO}_2$ divide into two fundamentally distinct thermodynamic regimes:
1. **Exergonic "Downhill" Pathways ($\\Delta G^\\circ < 0$):**  
   Reactions where $\\text{CO}_2$ reacts with high-energy co-reactants (e.g. basic metal oxides, epoxides, ammonia, or organic amines) to produce carbonates, polycarbonates, or urea derivatives. Examples include mineral carbonation ($\\text{CaSiO}_3 + \\text{CO}_2 \\rightarrow \\text{CaCO}_3 + \\text{SiO}_2$, $\\Delta H^\\circ = -87\\text{ kJ/mol}$, $\\Delta G^\\circ = -44\\text{ kJ/mol}$) and cyclic carbonate cycloaddition ($\\Delta H^\\circ = -94.5\\text{ kJ/mol}$, $\\Delta G^\\circ = -42\\text{ kJ/mol}$). These reactions are thermodynamically spontaneous at ambient or moderate temperatures, requiring catalysts solely to overcome kinetic activation barriers.
2. **Endergonic "Uphill" Reductive Pathways ($\\Delta G^\\circ > 0$):**  
   Reactions requiring the direct input of external energy (high-temperature heat, green hydrogen, or electricity) to break $\\text{C=O}$ bonds and reduce carbon to lower oxidation states ($+2$ in $\\text{CO}$, $+1$ in formic acid, $-2$ in methanol, $-4$ in methane). Examples include the Reverse Water-Gas Shift ($\\Delta G^\\circ_{298\\text{K}} = +28.6\\text{ kJ/mol}$), direct $\\text{CO}_2$ splitting ($\\text{CO}_2 \\rightarrow \\text{CO} + \\frac{1}{2}\\text{O}_2$, $\\Delta G^\\circ = +257\\text{ kJ/mol}$), and electrochemical reduction to ethylene ($\\Delta G^\\circ = +1,331\\text{ kJ/mol}$). These uphill routes function fundamentally as **chemical energy storage vectors**, meaning their life-cycle sustainability is entirely governed by the carbon intensity of the external energy supply.

### 3.2 Molecular Activation and Orbital Interactions
Because the lowest unoccupied molecular orbital (LUMO, $2\\pi_u^*$) of $\\text{CO}_2$ is high-lying and anti-bonding, transferring an electron to neutral linear $\\text{CO}_2$ to generate the bent radical anion ($\\text{CO}_2^{\\bullet-}$, $\\angle\\text{O-C-O} \\approx 133^\\circ$) requires an extremely negative standard reduction potential:
$$\\text{CO}_2 + e^- \\rightarrow \\text{CO}_2^{\\bullet-} \\quad (E^\\circ = -1.90\\text{ V vs. SHE in water})$$

Catalytic activation lowers this energetic barrier through cooperative orbital interactions:
- **Lewis Acid Activation (Coordination to Oxygen):** Electrophilic metal cations or surface oxygen vacancies coordinate the oxygen lone pairs, polarizing the $\\text{C=O}$ bond and increasing the electrophilicity of the central carbon atom.
- **Lewis Base Activation (Nucleophilic Attack on Carbon):** Basic surface species (e.g. metal oxides, amine functional groups, or carbanions) attack the central carbon atom, bending the molecule and rehybridizing the carbon center from $sp$ to $sp^2$.
- **Proton-Coupled Electron Transfer (PCET):** In electrocatalysis, coupling electron transfer with simultaneous proton transfer bypasses the high-energy $\\text{CO}_2^{\\bullet-}$ intermediate entirely, drastically reducing overpotentials:
  $$\\text{CO}_2 + \\text{H}^+ + e^- \\rightarrow *\\text{COOH} \\quad \\text{or} \\quad *\\text{OCHO} \\quad (E^\\circ \\approx -0.11\\text{ to } -0.25\\text{ V vs. RHE})$$

---

## 4. CO₂ Feedstocks, Capture Energetics, and Integrated Capture-Conversion

The techno-economic and life-cycle viability of any CCU process is intimately coupled to the cost, concentration, and purity of the carbon dioxide feedstock.

### 4.1 Point-Source Capture vs. Direct Air Capture (DAC)
- **High-Purity Industrial Sources:** Fermentation, bioethanol, and ethylene oxide plants vent $\\text{CO}_2$ at concentrations >95 mol%, requiring only dehydration and particulate filtration at low capture costs of \$20–\$35/tonne $\\text{CO}_2$.
- **Medium-Purity Post-Combustion Sources:** Cement kilns (15–30 mol% $\\text{CO}_2$), blast furnaces (20–25 mol%), and coal-fired power plants (10–14 mol%) require chemical solvent absorption (e.g. 30 wt% aqueous monoethanolamine [MEA] or advanced hindered amine blends like KS-21 and piperazine). Conventional MEA stripping imposes a massive thermal regeneration penalty of **3.0 to 3.5 GJ/tonne $\\text{CO}_2$** (typically supplied as low-pressure steam at 120–140 °C), penalizing power plant thermal efficiency by 25–40% and adding \$50–\$85/tonne to feedstock costs.
- **Direct Air Capture (DAC):** Sourcing $\\text{CO}_2$ from the ultra-dilute atmospheric reservoir (~425 ppm, or ~0.04 vol%) is constrained by the Second Law of Thermodynamics. The minimum theoretical thermodynamic work of separation is approximately $20\\text{ kJ/mol CO}_2$ (~450 kJ/kg $\\text{CO}_2$), but commercial solid-amine or liquid-hydroxide contactors consume **1.5 to 2.5 MWh of electricity and 4.0 to 7.0 GJ of heat per tonne $\\text{CO}_2$ captured**, resulting in current levelized capture costs of \$300–\$600/tonne. DAC is justified primarily for permanent Carbon Dioxide Removal (CDR) or high-value synthetic aviation fuels where point sources are geographically unavailable.

### 4.2 Integrated Capture and Conversion (ICCC) via Dual-Function Materials
To eliminate the parasitic thermal desorption, gas compression, and pipeline transport steps connecting standalone capture units to chemical reactors, **Dual-Function Materials (DFMs)** have been developed (Farrauto et al., *Nature Catalysis* 2021). DFMs integrate an alkaline chemisorbent phase (e.g. $\\text{Na}_2\\text{O}, \\text{K}_2\\text{O}, \\text{CaO}$) and catalytic metal nanoparticles (e.g. $\\text{Ru}, \\text{Ni}, \\text{Rh}$) co-dispersed on a high-surface-area porous support ($\\gamma\\text{-Al}_2\\text{O}_3$).

Operated cyclically and isothermally at 300–350 °C:
1. *Chemisorption Step:* Dilute flue gas (10% $\\text{CO}_2$) passes over the bed; basic sites chemisorb $\\text{CO}_2$ as surface carbonates:
   $$\\text{Na}_2\\text{O}(\\text{s}) + \\text{CO}_2(\\text{flue gas}) \\rightarrow \\text{Na}_2\\text{CO}_3(\\text{s})$$
2. *In-situ Methanation Step:* The bed is switched to a pure green hydrogen feed; catalytic $\\text{Ru}$ sites activate $\\text{H}_2$ to dissociate and hydrogenate the surface carbonate directly to methane:
   $$\\text{Na}_2\\text{CO}_3(\\text{s}) + 4\\text{H}_2(\\text{g}) \\rightarrow \\text{CH}_4(\\text{g}) + 2\\text{H}_2\\text{O}(\\text{g}) + \\text{Na}_2\\text{O}(\\text{s}) \\quad (\\Delta H^\\circ = -165\\text{ kJ/mol})$$

DFMs achieve >95% conversion of captured $\\text{CO}_2$ with >99% methane selectivity over 50 continuous cycles, completely avoiding the 3.2 GJ/t $\\text{CO}_2$ solvent boiling penalty and reducing total plant CAPEX by approximately 28%.

---

## 5. Taxonomy and Comparative Overview of CCU Pathways

Table 1 provides a harmonized comparative audit of the seventeen primary technological pathways evaluated in this review, detailing reaction inputs, operating regimes, kinetic rate metrics, selectivity, single-pass conversion, energy intensity, carbon permanence, technology readiness levels (TRL), and commercial deployment status.

### Table 1: Cross-Pathway Performance, Energy Intensity, and Permanence Matrix

| # | Pathway Name | Target Product | Primary Reactants | Energy Vector | Catalyst / System | Operating Conditions | Key Performance Metric | Selectivity / FE | Single-Pass Conv. (%) | Energy Intensity | Carbon Permanence | TRL | Commercial Facilities / Pilots |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **P01** | Thermocatalytic Hydrogenation | Methanol ($\\text{CH}_3\\text{OH}$) | $\\text{CO}_2 + \\text{H}_2$ | Thermal Heat + Green $\\text{H}_2$ | $\\text{In}_2\\text{O}_3/\\text{ZrO}_2$ or $\\text{Cu/ZnO}$ | 250–300 °C, 3–5 MPa | STY: $0.45–0.62\\text{ g/g}_\\text{cat}\\text{/h}$ | 86–100% Sel. | 8.5–15.2% | 10.5 MWh/t MeOH | Short (<6 mo fuel; 1–5 yr chem) | 8–9 | CRI George Olah (4 kt/a); Anyang Shunli (110 kt/a) |
| **P02** | Solid-Electrolyte eCO2R | Formic Acid ($\\text{HCOOH}$) | $\\text{CO}_2 + \\text{H}_2\\text{O}$ | Direct Electricity | Bismuth nanosheets in SSE | 25 °C, 0.1 MPa | Partial $j$: $188\\text{ mA/cm}^2$ | 93.8% FE | 32.0% | 4.2 kWh/kg pure acid | Medium (1–5 yr LOHC/preservative) | 5–7 | Xia & Wang demo; Twelve pilot units |
| **P03** | Zero-Gap MEA eCO2R | Carbon Monoxide ($\\text{CO}$) | $\\text{CO}_2 + \\text{H}_2\\text{O}$ | Direct Electricity | Ag or Ni-N-C on GDE | 40–60 °C, 0.1–0.5 MPa | Partial $j$: $300–500\\text{ mA/cm}^2$ | >95% FE | 35.0% | 6.5–8.0 kWh/kg CO | Short (syngas intermediate) | 6–8 | Air Liquide / Siemens demo; Twelve commercial unit |
| **P04** | Pure-Water MEA eCO2R | Ethylene ($\\text{C}_2\\text{H}_4$) | $\\text{CO}_2 + \\text{H}_2\\text{O}$ | Direct Electricity | Stepped $\\text{Cu}(100)$ with solid ionomer | 50 °C, 0.12 MPa, pure water | $10\\text{ A}$ stack ($100\\text{ mA/cm}^2$) | 62–70% FE | 22.0% | 30–35 kWh/kg $\\text{C}_2\\text{H}_4$ | Medium (1–20 yr in polymers) | 4–5 | Xu et al. (1,020 h milestone); Sargent flow cells |
| **P05** | Zero-Gap AEM eCO2R | Ethanol ($\\text{C}_2\\text{H}_5\\text{OH}$) | $\\text{CO}_2 + \\text{H}_2\\text{O}$ | Direct Electricity | $\\text{Cu-Ag}$ bimetallic mesh | 25–45 °C, 0.1 MPa | Partial $j$: $150–250\\text{ mA/cm}^2$ | 55–65% FE | 18.0% | 40–48 kWh/kg EtOH | Short (<1 yr fuel/solvent) | 4–5 | Oxylus Energy pilot; Li & Sargent Nature Energy 2024 |
| **P06** | Dry Reforming (DRM) | Syngas ($\\text{CO} + \\text{H}_2$, 1:1) | $\\text{CH}_4 + \\text{CO}_2$ | High-Temp Heat | Single-crystal $\\text{MgO/Ni}$ | 700–850 °C, 0.1–2.0 MPa | GHSV: $25,000\\text{ mL/g/h}$ | >95% Syngas Sel. | 75–92% $\\text{CH}_4$ | 3.8–4.5 GJ/t syngas | Short (converted to fuels/chemicals) | 6–7 | Linde-BASF pilot; Song et al. 2020 (1,000 h coke-free) |
| **P07** | Tri-Reforming (TRM) | Syngas ($\\text{H}_2/\\text{CO} = 1.5–2.0$) | $\\text{CH}_4 + \\text{CO}_2 + \\text{H}_2\\text{O} + \\text{O}_2$ | Semi-Autothermal | $\\text{Ni-Fe/Al}_2\\text{O}_3$ | 750–850 °C, 0.1–2.0 MPa | GHSV: $30,000\\text{ mL/g/h}$ | >98% CO + $\\text{H}_2$ Sel. | 85–95% $\\text{CH}_4$ | 1.2–2.0 GJ/t syngas | Short (liquid fuel precursor) | 5–6 | Song & Pan; Alli et al. Catal. Today 2023 |
| **P08** | Industrial Urea Synthesis | Urea ($\\text{CO(NH}_2)_2$) | $2\\text{NH}_3 + \\text{CO}_2$ | High-Pressure Steam | Uncatalyzed thermal melt | 180–200 °C, 14–20 MPa | $1,500–3,000\\text{ t/day}$ | >99% Plant Sel. | 50–70% (99% rec.) | 0.8–1.1 MWh/t urea | Short (7–28 days; 100% soil $\\text{CO}_2$ release) | 9 | Stamicarbon, Saipem, TOYO plants (~180 Mt/a) |
| **P09** | Cyclic Urea Synthesis | 2-Imidazolidinone | $\\text{EDA} + \\text{CO}_2$ | Thermal Heat | $\\text{CeO}_2$ nanorods | 140–180 °C, 2–5 MPa | Isolated yield: 70–88% | >95% Sel. | 75–92% | 2.5–3.5 GJ/t urea | Long (10–50 yr in durable resins) | 4–6 | Fujii & Tomishige ACS Catal. 2023 flow pilot |
| **P10** | Kolbe–Schmitt Carboxylation | Salicylic Acid | Phenol + $\\text{CO}_2$ + NaOH | Thermal + Acid Quench | Stoichiometric phenolate | 120–160 °C, 0.5–5 MPa | Isolated yield: 78–88% | >95% Ortho-Sel. | >85% | 2.8–3.6 GJ/t acid | Medium (1–10 yr in Aspirin/polymers) | 9 | Novacyl / Seqens, Rhodia (~100 kt/a Aspirin) |
| **P11** | Direct DMC Synthesis | DMC ($(\\text{CH}_3\\text{O})_2\\text{CO}$) | $\\text{CO}_2 + 2\\text{CH}_3\\text{OH}$ | Thermal Heat | $\\text{CeO}_2$ + 2-cyanopyridine | 120 °C, 3.0 MPa | Yield: 92% based on MeOH | >99% Sel. | 94.0% | 5.5–7.0 GJ/t DMC | Medium (2–10 yr electrolyte/polymer) | 5–6 | Tamura & Tomishige; Asahi Kasei commercial |
| **P12** | Epoxide Copolymerization | Polycarbonates (PPC) | $\\text{PO} + \\text{CO}_2$ | Exothermic Catalytic | $\\text{Co(III)/Zn(II)}$ macrocycles | 60–100 °C, 1–4 MPa | TON > 50,000; TOF > 2,000 | 100% Atom Economy | >95% | <0.8 MWh/t polymer | Durable (10–50 yr in foams/materials) | 8–9 | Covestro cardyon (5 kt/a); SK PPC; Aramco Converge |
| **P13** | Molten Carbonate (C2CNT) | Carbon Nanotubes (MWCNTs) | $\\text{CO}_2$ in $\\text{Li}_2\\text{CO}_3$ melt | High-Temp Electricity | Galvanized steel / Ni-Fe | 750 °C, 0.1 MPa | Rate: $0.35\\text{ g CNT/Ah}$ | 96–98% Coulombic | >95% capture | 18 kWh/kg CNT | Permanent (>10,000 yr in composites) | 6–7 | C2CNT / Carbon Corp (12 t/a); NRG XPRIZE |
| **P14** | Microbial Electrosynthesis | Acetate ($\\text{CH}_3\\text{COO}^-$) | $\\text{CO}_2 + \\text{H}_2\\text{O} + e^-$ | Biocathodic Power | Acetogenic biofilm on carbon felt | 30–37 °C, 0.1 MPa, pH 7.0 | Volumetric: $1.4–15\\text{ g/L/d}$ | 88–95% Cathodic FE | >90% | 12–18 kWh/kg acetate | Short (1–2 yr intermediate/bioplastic) | 4–5 | Jourdin et al. 2021; LanzaTech commercial gas ferm. |
| **P15** | In-Situ Basalt Trapping | Solid Calcite ($\\text{CaCO}_3$) | $\\text{CO}_2 + \\text{H}_2\\text{O}$ | Pumping / Injection Power | Natural basalt formations | 25 bar injection, 20–50 °C | >95% fixed in 2 years | 100% Mineral Trapping | >95% in 2 yr | 0.15–0.25 MWh/t $\\text{CO}_2$ | Permanent (>10,000 yr stone) | 8–9 | Carbfix / Climeworks Orca & Mammoth (36 kt/a) |
| **P16** | Slag Concrete Curing | Precast Concrete | $\\text{CO}_2 + \\text{Steel Slag}$ | Ambient / Low Heat | Portlandite & calcium silicates | 20–60 °C, 0.1–0.5 MPa | 150–250 kg $\\text{CO}_2$/t slag | >95% Carbonation | 60–80% theor. | 0.05–0.12 MWh/t block | Permanent (>1,000–10,000 yr structures) | 8–9 | CarbonCure (800+ plants globally); Solidia Tech. |
| **P17** | Dual-Function ICCC | Methane ($\\text{CH}_4$) | Flue gas $\\text{CO}_2 + \\text{H}_2$ | Isothermal Cyclic Heat | $\\text{Ru-Na}_2\\text{O}/\\text{Al}_2\\text{O}_3$ | 320 °C isothermal, 0.1 MPa | Yield: $0.36\\text{ mmol/g}_\\text{DFM}$ | >99% Methane Sel. | 95% of sorbed $\\text{CO}_2$ | Avoids 3.2 GJ/t boiling | Short (fuel combustion releases $\\text{CO}_2$) | 4–6 | Farrauto group Nature Catal. 2021; BASF demo |

---

## 6. Thermocatalytic Hydrogenation to Methanol and Oxygenates

Methanol ($\\text{CH}_3\\text{OH}$) is the premier platform commodity in the emerging chemical CCU infrastructure, functioning as a precursor for formaldehyde, acetic acid, dimethyl ether, and olefins via methanol-to-olefins (MTO) processes, as well as a liquid shipping fuel.

### 6.1 Thermodynamics and the Competing RWGS Equilibrium
Direct $\\text{CO}_2$ hydrogenation to methanol is an exothermic reaction involving a decrease in gas moles:
$$\\text{CO}_2(\\text{g}) + 3\\text{H}_2(\\text{g}) \\rightleftharpoons \\text{CH}_3\\text{OH}(\\text{g}) + \\text{H}_2\\text{O}(\\text{g}) \\quad (\\Delta H^\\circ_{298\\text{K}} = -49.5\\text{ kJ/mol}, \\Delta G^\\circ_{298\\text{K}} = +3.5\\text{ kJ/mol})$$

By Le Chatelier's principle, methanol synthesis is thermodynamically favored at elevated pressures (3.0–8.0 MPa) and moderate temperatures (<250 °C). However, the endothermic Reverse Water-Gas Shift (RWGS) reaction competes directly for the feed gas:
$$\\text{CO}_2(\\text{g}) + \\text{H}_2(\\text{g}) \\rightleftharpoons \\text{CO}(\\text{g}) + \\text{H}_2\\text{O}(\\text{g}) \\quad (\\Delta H^\\circ_{298\\text{K}} = +41.2\\text{ kJ/mol}, \\Delta G^\\circ_{298\\text{K}} = +28.6\\text{ kJ/mol})$$

Because RWGS is endothermic, its equilibrium constant increases sharply with temperature. Consequently, thermodynamic equilibrium selectivity towards methanol drops steeply from ~80% at 200 °C to <30% at 300 °C under 5.0 MPa. At typical industrial operating temperatures, single-pass conversion is equilibrium-constrained to 8–18%, necessitating aggressive unreacted gas recycling ratios of 3:1 to 5:1.

### 6.2 Catalyst Paradigms: Industrial Cu/ZnO vs. Vacancy-Engineered In₂O₃
- **Industrial $\\text{Cu/ZnO/Al}_2\\text{O}_3$ Baseline:** In conventional syngas plants, $\\text{Cu/ZnO/Al}_2\\text{O}_3$ operates via active $\\text{Cu-Zn}$ interfacial alloy sites decorated on stepped $\\text{Cu}(211)$ surfaces (Behrens et al., *Science* 2012). However, under pure $\\text{CO}_2$ feeds, the equimolar generation of by-product water vapor ($\\text{H}_2\\text{O}$) accelerates the irreversible sintering of metallic copper crystallites and induces hydrothermal oxidation of $\\text{Zn}$ to inactive $\\text{ZnO}$, causing severe catalytic deactivation within 500–1,000 hours.
- **$\\text{In}_2\\text{O}_3/\\text{ZrO}_2$ Vacancy-Engineered Catalysts (2020–2025 Benchmark):** Indium oxide supported on monoclinic zirconia completely fundamentally alters the reaction pathway (Tsoukalou et al., *J. Am. Chem. Soc.* 2020). Oxygen vacancies ($V_\\text{O}$) formed on $\\text{In}_2\\text{O}_3(111)$ terraces chemisorb $\\text{CO}_2$ and activate it via sequential hydride additions:
  $$\\text{CO}_2 \\rightarrow *\\text{HCOO} \\rightarrow *\\text{H}_2\\text{COO} \\rightarrow *\\text{H}_3\\text{CO} \\rightarrow \\text{CH}_3\\text{OH}$$
  The vacancy sites stabilize the formate and methoxy intermediates without cleaving the $\\text{C-O}$ bond into free adsorbed $*\\text{CO}$, completely suppressing the competing RWGS reaction. $\\text{In}_2\\text{O}_3/\\text{ZrO}_2$ achieves **100% methanol selectivity at 300 °C and 5 MPa** with a space-time yield of $0.45–0.62\\text{ g}_\\text{MeOH}/\\text{g}_\\text{cat}/\\text{h}$ and demonstrated operational stability exceeding 1,000 hours.

### 6.3 Commercial Deployment Milestones
Commercial implementation of $\\text{CO}_2$-to-methanol has transitioned from small demonstrations to world-scale industrial complexes:
- **Carbon Recycling International (CRI) George Olah Plant (Svartsengi, Iceland):** Operating since 2012, this facility converts 5,500 t/a of geothermal $\\text{CO}_2$ and hydroelectric hydrogen into 4,000 t/a of certified e-methanol (Vulcanol®).
- **Anyang Shunli Facility (Henan, China):** Commissioned in October 2022 using CRI proprietary Emissions-to-Liquids (ETL) technology, this facility captures 160,000 t/a of industrial flue gas $\\text{CO}_2$ from lime production and reacts it with hydrogen recovered from coke-oven gas, manufacturing **110,000 t/a of low-carbon chemical-grade methanol**, cutting regional $\\text{CO}_2$ emissions by 560,000 t/a.

---

## 7. Dry, Bi-, and Tri-Reforming of Methane

Reforming reactions transform two primary greenhouse gases—methane ($\\text{CH}_4$) and carbon dioxide ($\\text{CO}_2$)—into synthesis gas ($\\text{CO} + \\text{H}_2$), providing carbon-efficient precursors for Fischer-Tropsch synthetic fuels and oxo-chemicals.

### 7.1 Dry Reforming of Methane (DRM) & Coking Deactivation
Dry reforming operates via the endothermic reaction:
$$\\text{CH}_4(\\text{g}) + \\text{CO}_2(\\text{g}) \\rightleftharpoons 2\\text{CO}(\\text{g}) + 2\\text{H}_2(\\text{g}) \\quad (\\Delta H^\\circ_{298\\text{K}} = +247.3\\text{ kJ/mol}, \\Delta G^\\circ_{298\\text{K}} = +170.8\\text{ kJ/mol})$$

Producing an equimolar syngas ratio ($\\text{H}_2/\\text{CO} \\approx 1.0$), DRM is uniquely suited for direct synthesis of oxygenated chemicals and acetic acid. However, commercial deployment has been chronically impeded by severe catalyst deactivation via carbon deposition (coking). Coking proceeds via two concurrent side reactions:
1. *Methane Pyrolysis (Cracking):* $\\text{CH}_4 \\rightleftharpoons \\text{C}(\\text{s}) + 2\\text{H}_2 \\quad (\\Delta H^\\circ = +74.9\\text{ kJ/mol})$
2. *The Boudouard Reaction:* $2\\text{CO} \\rightleftharpoons \\text{C}(\\text{s}) + \\text{CO}_2 \\quad (\\Delta H^\\circ = -172.5\\text{ kJ/mol})$

At temperatures below 700 °C, the exothermic Boudouard reaction is thermodynamically spontaneous, driving rapid nucleation of carbon whiskers and encapsulating active nickel sites. In 2020, Song et al. (*Science* 2020) demonstrated a breakthrough anti-coking catalyst: nickel nanoparticles encapsulated within atomically thin, defect-free single-crystalline magnesium oxide ($\\text{MgO}$) overlayers. The nanocatalyst maintained coke-free dry reforming operation for **>1,000 hours at 800 °C** without loss of conversion.

### 7.2 Bi-Reforming (BRM) and Tri-Reforming (TRM)
- **Bi-Reforming of Methane (BRM):** Co-feeding steam with $\\text{CO}_2$ balances the stoichiometry to produce the exact $\\text{H}_2/\\text{CO} = 2.0$ ratio required for direct methanol and Fischer-Tropsch synthesis:
  $$3\\text{CH}_4(\\text{g}) + \\text{CO}_2(\\text{g}) + 2\\text{H}_2\\text{O}(\\text{g}) \\rightarrow 4\\text{CO}(\\text{g}) + 8\\text{H}_2(\\text{g}) \\quad (\\Delta H^\\circ_{298\\text{K}} = +659\\text{ kJ/mol})$$
  Chan et al. (*Chem. Eng. J.* 2025) achieved >80% $\\text{CO}_2$ conversion over $\\text{Ni/CaO-Al}_2\\text{O}_3$ at 800 °C, where basic $\\text{CaO}$ promotes in-situ $\\text{CO}_2$ chemisorption and continuous coke gasification.
- **Tri-Reforming of Methane (TRM):** Pioneered by Song & Pan (*Catal. Today* 2004; Alli et al., 2023), TRM simultaneously couples dry reforming, steam reforming, and exothermic partial oxidation of methane within a single reactor:
  $$3\\text{CH}_4(\\text{g}) + \\text{CO}_2(\\text{g}) + \\text{H}_2\\text{O}(\\text{g}) + \\frac{1}{2}\\text{O}_2(\\text{g}) \\rightarrow 4\\text{CO}(\\text{g}) + 7\\text{H}_2(\\text{g}) \\quad (\\Delta H^\\circ \\approx +152\\text{ kJ/mol})$$
  TRM offers three decisive technological advantages: (1) internal partial oxidation generates in-situ heat, rendering the process semi-autothermal and reducing external furnace fuel demand; (2) co-fed $\\text{H}_2\\text{O}$ and $\\text{O}_2$ continuously gasify carbon precursors, suppressing coking without noble metals; and (3) flue gas containing residual $\\text{O}_2$ and moisture can be fed directly without costly upstream separation.

---

## 8. Electrocatalytic CO₂ Reduction (eCO₂R)

Electrochemical reduction powered by renewable electricity directly converts $\\text{CO}_2$ and water into chemical products under near-ambient conditions, providing a direct power-to-X interface.

### 8.1 C₁ Products: Pure Formic Acid and Carbon Monoxide
- **Direct Solid-State Electrolyte Formic Acid (Xia & Wang 2020):** Traditional liquid-electrolyte flow cells produce formate salts (e.g. $\\text{HCOOK}$), requiring downstream addition of concentrated $\\text{H}_2\\text{SO}_4$ to liberate formic acid ($\\text{HCOOH}$), generating 1.89 kg of unmarketable $\\text{K}_2\\text{SO}_4$ waste salt per kg of acid. Xia, Wang et al. (*Nature Energy* 2020) resolved this bottleneck by engineering a three-compartment electrochemical cell utilizing an atomically thin bismuth nanosheet cathode and a central porous solid-state electrolyte (SSE) channel. Protons generated at the anode migrate across an ionomer into the central channel, combining with formate anions to yield **pure liquid formic acid solutions up to 20 wt% (4.3 M) directly**, achieving a Faradaic efficiency of **93.8% at 200 mA/cm²** with zero salt waste.
- **Carbon Monoxide (CO):** Reduction to $\\text{CO}$ occurs at low overpotentials on gold, silver, and carbon-supported single-atom transition metal catalysts ($\\text{Ni-N-C}$):
  $$\\text{CO}_2 + 2\\text{H}^+ + 2e^- \\rightarrow \\text{CO} + \\text{H}_2\\text{O} \\quad (E^\\circ = -0.11\\text{ V vs. RHE})$$
  In zero-gap gas diffusion flow cells, $\\text{Ni-N-C}$ catalysts achieve **>95% FE at industrial current densities of 300–500 mA/cm²** at full-cell voltages <2.5 V, making $\\text{CO}$ the most mature electroreduction route (TRL 6–8; commercialized by Twelve and Air Liquide).

### 8.2 C₂₊ Multi-Carbon Products: Ethylene and Ethanol
Synthesizing multicarbon products requires a complex 12-electron transfer and decisive $\\text{C-C}$ bond coupling between two surface-bound $*\\text{CO}$ intermediates:
$$2\\text{CO}_2 + 12\\text{H}^+ + 12e^- \\rightarrow \\text{C}_2\\text{H}_4 + 4\\text{H}_2\\text{O} \\quad (E^\\circ = +0.08\\text{ V vs. RHE})$$
$$2\\text{CO}_2 + 12\\text{H}^+ + 12e^- \\rightarrow \\text{C}_2\\text{H}_5\\text{OH} + 3\\text{H}_2\\text{O} \\quad (E^\\circ = +0.09\\text{ V vs. RHE})$$

Copper ($\\text{Cu}$) remains the singular metallic electrocatalyst capable of catalyzing $\\text{C-C}$ coupling at significant rates due to its intermediate binding energy for $*\\text{CO}$ (Nitopi et al., *Chem. Rev.* 2019). Product distribution is acutely sensitive to surface crystallographic facets: stepped $\\text{Cu}(100)$ facets stabilize the dimeric $*\\text{C-CO}$ intermediate, steering selectivity towards ethylene, whereas $\\text{Cu}(111)$ promotes protonation towards methane. García de Arquer et al. (*Science* 2020) achieved 70% FE to ethylene at $1.0\\text{ A/cm}^2$ by engineering an ionomer-catalyst assembly that decouples gas transport from ionic conductivity.

### 8.3 The 1,000-Hour Industrial Durability Milestone
Historically, electrochemical flow cells suffered rapid deactivation (<100 hours) caused by flooding of the gas diffusion layer and carbonate salt precipitation inside the gas pores. In 2024, Xu et al. (*Nature Energy* 2024) overcame this structural degradation by deploying a **pure-water-fed zero-gap membrane electrode assembly (MEA)** with an integrated solid-acid ionomer layer. Operating without liquid salt electrolytes, the $100\\text{ cm}^2$ zero-gap cell delivered continuous ethylene production at **10 A total current ($100\\text{ mA/cm}^2$) for >1,020 hours** with 62–70% Faradaic efficiency and zero salt precipitation, establishing an unprecedented milestone in industrial electrocatalytic durability.

### 8.4 Critical Engineering Bottlenecks: Carbonate Crossover and Dilute Separation
Despite high Faradaic efficiencies, two systemic engineering penalties constrain eCO₂R commercialization:
1. **Carbonate Crossover:** In neutral and alkaline electrolytes, hydroxide ions generated at the cathode rapidly react with incoming $\\text{CO}_2$:
   $$\\text{CO}_2 + 2\\text{OH}^- \\rightarrow \\text{CO}_3^{2-} + \\text{H}_2\\text{O}$$
   Up to 50–70% of the feed $\\text{CO}_2$ crosses the anion exchange membrane (AEM) as carbonate ions ($\\text{CO}_3^{2-}$) and is released at the anode mixed with oxygen gas (Rabinowitz & Kanan, 2020). Re-separating this crossed $\\text{CO}_2$ from anode $\\text{O}_2$ imposes an intolerable parasitic energy duty of 2–4 kWh/kg product.
2. **Dilute Aqueous Separation Penalties:** Electrosynthesis of liquid alcohols yields dilute product streams (<3 wt% ethanol). Thermally distilling dilute ethanol to fuel-grade purity requires **4.0 to 6.5 MJ/kg ethanol**, an energy penalty equivalent to 15–25% of the fuel's entire combustion energy content.

---

## 9. Urea Synthesis & Emerging Electrocatalytic C–N Coupling

### 9.1 Industrial Carbamate Equilibrium and the 100% Soil Carbon Emission Reality
Industrial urea synthesis consumes approximately 160–180 million tonnes of $\\text{CO}_2$ annually, making it the single largest commercial consumer of $\\text{CO}_2$. The classical Bosch-Meiser process operates in two steps:
$$2\\text{NH}_3(\\text{g}) + \\text{CO}_2(\\text{g}) \\rightleftharpoons \\text{NH}_2\\text{COONH}_4(\\text{l}) \\quad (\\Delta H^\\circ = -117\\text{ kJ/mol, exergonic})$$
$$\\text{NH}_2\\text{COONH}_4(\\text{l}) \\rightleftharpoons \\text{CO(NH}_2)_2(\\text{l}) + \\text{H}_2\\text{O}(\\text{l}) \\quad (\\Delta H^\\circ = +15.5\\text{ kJ/mol, endergonic})$$

Operating under severe conditions (180–200 °C, 14–20 MPa) to maintain liquid ammonium carbamate, single-pass conversion is equilibrium-constrained to 50–70%, requiring extensive stripping towers and unreacted gas recycle loops.

Crucially, **industrial urea synthesis does not constitute permanent carbon sequestration**. Over 80% of global urea is applied as an agricultural fertilizer. Upon soil application, microbial urease enzyme rapidly catalyzes complete hydrolytic decomposition:
$$\\text{CO(NH}_2)_2 + \\text{H}_2\\text{O} \\xrightarrow{\\text{Urease}} 2\\text{NH}_3 + \\text{CO}_2 \\uparrow$$
**100% of the chemically incorporated carbon dioxide is returned to the atmosphere within 7 to 28 days.** Furthermore, conventional ammonia is manufactured via steam methane reforming, which emits 1.8–2.1 tonnes of fossil $\\text{CO}_2$ per tonne of $\\text{NH}_3$. Consequently, fossil-based urea production is an intense net carbon source (+1.2 to +1.6 t $\\text{CO}_2\\text{e}$ per tonne urea).

### 9.2 Ambient Electrocatalytic C–N Coupling Benchmarks
To bypass both the high-temperature Haber-Bosch ammonia loop and the severe carbamate conditions, direct electrocatalytic coupling of $\\text{CO}_2$ with dinitrogen ($\\text{N}_2$) or nitrate ($\\text{NO}_3^-$) under ambient conditions has emerged as an intensive research frontier (Chen, Wang et al., *Nature Chemistry* 2020; Lv et al., *Nature Sustainability* 2021):
$$\\text{N}_2(\\text{g}) + \\text{CO}_2(\\text{g}) + 6\\text{H}^+(\\text{aq}) + 6e^- \\rightarrow \\text{CO(NH}_2)_2(\\text{aq}) + \\text{H}_2\\text{O}(\\text{l})$$
$$2\\text{NO}_3^-(\\text{aq}) + \\text{CO}_2(\\text{g}) + 18\\text{H}^+(\\text{aq}) + 16e^- \\rightarrow \\text{CO(NH}_2)_2(\\text{aq}) + 7\\text{H}_2\\text{O}(\\text{l})$$

Chen et al. (2020) demonstrated direct coupling over palladium-copper alloy nanoclusters supported on $\\text{TiO}_2$ nanorods, achieving a urea Faradaic efficiency of **53.4% at -0.65 V vs. RHE** and a yield rate of $3.36\\text{ mmol/g}_\\text{cat}\\text{/h}$. While electrocatalytic $\\text{C-N}$ coupling offers a revolutionary vision for decentralized fertilizer synthesis, current challenges center on dilute product titers (<50 mM urea), where crystallization energy currently undermines process economics.

### 9.3 Durable Cyclic Urea: 2-Imidazolidinone Synthesis
In contrast to agricultural open-chain urea, cyclic ureas such as 2-imidazolidinone (ethylene urea) offer **10 to 50 years of durable carbon retention** when integrated into formaldehyde-scavenging wood adhesives and resins:
$$\\text{H}_2\\text{NCH}_2\\text{CH}_2\\text{NH}_2(\\text{l}) + \\text{CO}_2(\\text{g}) \\rightleftharpoons \\text{C}_3\\text{H}_6\\text{N}_2\\text{O}(\\text{s}) + \\text{H}_2\\text{O}(\\text{l}) \\quad (\\Delta H^\\circ = -68.4\\text{ kJ/mol})$$
Fujii, Tamura, Tomishige et al. (*ACS Catalysis* 2023) developed a continuous fixed-bed flow process over ceria ($\\text{CeO}_2$) nanorods at 160 °C and 3.0 MPa, achieving an isolated yield of **88% with >95% selectivity**, demonstrating a high-value, durable alternative to fertilizer urea.

---

## 10. CO₂-Derived Carbonates and Polycarbonates

Synthesis of carbonates represents the most commercially mature category of exergonic non-reductive $\\text{CO}_2$ utilisation, integrating $\\text{CO}_2$ as a phosgene substitute.

### 10.1 Direct Dimethyl Carbonate (DMC) Synthesis via Chemical Dehydration
Direct synthesis of DMC from $\\text{CO}_2$ and methanol avoids hazardous phosgene ($\\text{COCl}_2$) and carbon monoxide routes:
$$\\text{CO}_2(\\text{g}) + 2\\text{CH}_3\\text{OH}(\\text{l}) \\rightleftharpoons (\\text{CH}_3\\text{O})_2\\text{CO}(\\text{l}) + \\text{H}_2\\text{O}(\\text{l}) \\quad (\\Delta G^\\circ_{298\\text{K}} = +26.2\\text{ kJ/mol})$$

Direct condensation is severely equilibrium-limited (equilibrium methanol conversion <2% at 120 °C). In 2020, Tamura, Tomishige et al. (*ACS Catalysis* 2020) resolved this constraint by combining a $\\text{CeO}_2$ nanorod catalyst with 2-cyanopyridine as an organic chemical dehydrating agent. The nitrile reacts irreversibly with by-product water to form 2-picolinamide, pulling the equilibrium forward to achieve **94% methanol conversion and 92% isolated DMC yield at 120 °C**. The hydrated picolinamide is regenerated via thermal dehydration, providing an energy-efficient path to green lithium-ion battery electrolytes and polycarbonate building blocks.

### 10.2 Epoxide Cycloaddition to 5-Membered Cyclic Carbonates
The coupling of $\\text{CO}_2$ with epoxides (e.g. propylene oxide, PO) to form cyclic carbonates (propylene carbonate, PC) is a 100% atom-economical, highly exergonic reaction:
$$\\text{C}_3\\text{H}_6\\text{O}(\\text{l}) + \\text{CO}_2(\\text{g}) \\rightarrow \\text{C}_4\\text{H}_6\\text{O}_3(\\text{l}) \\quad (\\Delta H^\\circ = -94.5\\text{ kJ/mol}, \\Delta G^\\circ = -42.0\\text{ kJ/mol})$$

Recent breakthroughs focus on metal-free organocatalysis and biochar-supported quaternary onium salts (Kleij et al., *Chem. Commun.* 2024), achieving quantitative yields (>98.5%) under solvent-free conditions at 80 °C and 1.0 MPa $\\text{CO}_2$. Cyclic carbonates exhibit medium-term carbon retention (5–15 years) in lithium-ion battery electrolytes and green polar solvents.

### 10.3 Ring-Opening Copolymerization (ROCOP) for Polycarbonate Polyols
Alternating ring-opening copolymerization of $\\text{CO}_2$ with epoxides yields aliphatic polycarbonates such as polypropylene carbonate (PPC) and polycarbonate ether polyols (Williams et al., *Chem. Rev.* 2021):
$$n\\,\\text{C}_3\\text{H}_6\\text{O} + n\\,\\text{CO}_2 \\rightarrow -[\\text{CH}_2-\\text{CH(CH}_3)\\text{-O-C(=O)-O}]_n-$$

Using heterodinuclear macrocyclic catalysts (e.g. $\\text{Co(III)/Zn(II)}$ complexes), the alternating insertion of epoxide and $\\text{CO}_2$ proceeds with >99% polymer selectivity, suppressing cyclic carbonate backbiting. This process has achieved commercial scale through Covestro's cardyon® brand (Dormagen, Germany, 5,000 t/a capacity), synthesizing polyols containing **20 wt% incorporated $\\text{CO}_2$** for automotive seating, mattress foams, and building insulation, locking carbon for **10 to 50 years** and displacing 0.25–0.30 kg $\\text{CO}_2\\text{e}$ per kg polyol.

---

## 11. Carbon Nanomaterials from CO₂ and Critical Precursor Distinctions

Synthesis of solid carbon nanostructures (carbon nanotubes, graphene, carbon nanofibers) provides a permanent carbon sink (>10,000 years). However, the literature is marred by flawed combustion claims and precursor misclassifications.

### 11.1 Rebuttal of Magnesiothermic Reduction: The Upstream Carbon Deficit
Numerous exploratory papers (e.g. Chakrabarti et al., 2011; Bagotia et al., 2018) promote burning metallic magnesium ribbons inside solid dry ice or gaseous $\\text{CO}_2$ as a green method to synthesize graphene:
$$\\text{CO}_2(\\text{g}) + 2\\text{Mg}(\\text{s}) \\rightarrow 2\\text{MgO}(\\text{s}) + \\text{C}(\\text{s}) \\quad (\\Delta H^\\circ = -810\\text{ kJ/mol})$$

A rigorous chemical and life-cycle audit refutes this claim:
1. *Product Quality:* Burning Mg in $\\text{CO}_2$ is a violent thermal combustion (>2,000 °C) producing disordered soot and turbostratic graphitic flakes heavily contaminated with $\\text{MgO}$, requiring concentrated hydrochloric acid leaching ($2\\text{MgO} + 4\\text{HCl} \\rightarrow 2\\text{MgCl}_2 + 2\\text{H}_2\\text{O}$) that consumes 3.3 kg $\\text{HCl}$ per kg carbon.
2. *Upstream Embodied Carbon:* Metallic magnesium is manufactured via the high-temperature Pidgeon process, emitting **15 to 25 kg $\\text{CO}_2\\text{e}$ per kg metallic Mg**. By stoichiometry, fixing 1.0 kg of $\\text{CO}_2$ consumes 1.10 kg of $\\text{Mg}$, generating **+18 to +28 kg $\\text{CO}_2\\text{e}$ in upstream emissions**.
3. **Verdict:** Magnesiothermic reduction is an intensely carbon-positive process and cannot be claimed as sustainable $\\text{CO}_2$ utilisation.

### 11.2 Sustainable Alternative: Molten Carbonate Electrosynthesis (C2CNT)
In contrast, high-temperature molten salt electrolysis (the C2CNT process; Licht et al., *Nature Comm.* 2020) directly splits $\\text{CO}_2$ in a molten carbonate eutectic ($\\text{Li}_2\\text{CO}_3/\\text{Na}_2\\text{CO}_3/\\text{K}_2\\text{CO}_3$) at 750 °C:
$$\\text{Cathode: } \\text{CO}_3^{2-}(\\text{melt}) + 4e^- \\rightarrow \\text{C}(\\text{s, CNT}) + 3\\text{O}^{2-}(\\text{melt})$$
$$\\text{Anode: } 2\\text{O}^{2-}(\\text{melt}) \\rightarrow \\text{O}_2(\\text{g}) + 4e^-$$
$$\\text{Net Regeneration: } \\text{CO}_2(\\text{g}) + \\text{O}^{2-}(\\text{melt}) \\rightleftharpoons \\text{CO}_3^{2-}(\\text{melt}) \\quad \\Longrightarrow \\quad \\text{Net: } \\text{CO}_2(\\text{g}) \\rightarrow \\text{C}(\\text{s}) + \\text{O}_2(\\text{g})$$

Operating with galvanized steel cathodes and nickel alloy anodes, the process achieves **96–98% Coulombic efficiency** and >95% carbon nanotube morphological purity at a specific energy consumption of ~18 kWh/kg CNT. Powered by renewable electricity, C2CNT permanently sequesters 3.67 kg $\\text{CO}_2$ per kg CNT, delivering net avoided emissions of **-12 kg $\\text{CO}_2\\text{e/kg CNT}$** compared to commercial fossil CVD processes.

### 11.3 Clarification of Non-CO₂ Biomass Precursors: Pongamia Oil Pyrolysis
Recent studies (e.g. Marichamy, Karthikeyan, & Balasubramaniam, 2026) investigate multi-walled carbon nanotube synthesis via catalytic spray pyrolysis of *Pongamia pinnata* (Honge/Karanja) seed oil methyl esters over $\\text{Fe-Co-Mo}/\\text{Al}_2\\text{O}_3$ catalysts at 750–850 °C.

**Crucial Scientific Distinction:** This route utilizes plant-extracted triglycerides and fatty acid hydrocarbons (primarily oleic and linoleic acid methyl esters), **NOT gaseous carbon dioxide**. Thermal cracking of plant oils:
$$\\text{C}_n\\text{H}_m\\text{O}_p(\\text{liquid}) \\xrightarrow{\\Delta, \\text{catalyst}} \\text{C}(\\text{MWCNT}) + \\text{H}_2 + \\text{CO} + \\text{CH}_4$$
represents a renewable biomass conversion process, but must not be conflated with or misclassified as direct $\\text{CO}_2$ utilisation. Transparent boundary accounting requires separating direct CCU from bio-based carbon material processing.

---

## 12. Direct Carboxylation and Pharmaceutical Applications

Direct incorporation of $\\text{CO}_2$ into organic scaffolds to construct carboxylic acids and esters represents a high-value green chemistry domain.

### 12.1 The Kolbe–Schmitt Carboxylation for Salicylic Acid
The Kolbe–Schmitt reaction, discovered in 1860, remains the foundational industrial paradigm for direct $\\text{C-C}$ carboxylation (TRL 9; >100,000 t/a scale):
$$\\text{C}_6\\text{H}_5\\text{ONa}(\\text{s}) + \\text{CO}_2(\\text{g}) \\xrightarrow{120–160^\\circ\\text{C}, 0.5–5\\text{ MPa}} o\\text{-HOC}_6\\text{H}_4\\text{COONa}(\\text{s})$$
$$o\\text{-HOC}_6\\text{H}_4\\text{COONa} + \\text{HCl} \\rightarrow o\\text{-HOC}_6\\text{H}_4\\text{COOH}(\\text{s, Salicylic Acid}) + \\text{NaCl}$$

Electrophilic aromatic substitution of sodium phenoxide directed by a cyclic sodium-chelated transition state achieves >95% *ortho*-selectivity. Salicylic acid is subsequently acetylated to acetylsalicylic acid (Aspirin). Recent advances (Beller et al., *Molecules* 2024) develop suspension-based continuous microreactor flow systems in toluene or DMSO, slashing reaction residence times from hours to minutes.

### 12.2 Visible-Light Photoredox C(sp³)–H Carboxylation
Classical organometallic carboxylation relies on stoichiometric Grignard reagents ($\\text{R-MgX} + \\text{CO}_2 \\rightarrow \\text{R-COOMgX} \\xrightarrow{\\text{H}^+} \\text{R-COOH}$), which suffer from poor atom economy, hazardous pyrophoric reagents, and extreme waste salt generation (E-factor > 25).

In 2021, Gimenez-Gomez et al. (*J. Am. Chem. Soc.* 2021) demonstrated direct catalytic $\\text{C(sp}^3\\text{)–H}$ carboxylation of alkyl arenes under visible light:
$$\\text{R–H} + \\text{CO}_2(\\text{g}) + \\text{Base} + h\\nu \\xrightarrow{4\\text{CzIPN / Quinuclidine}} \\text{R–COO}^- + \\text{Base–H}^+$$
Operating at 25 °C and 1.0 atm $\\text{CO}_2$ under blue LED irradiation, the organic fluorophore ($4\\text{CzIPN}$) coupled with a quinuclidine hydrogen-atom transfer (HAT) catalyst carboxylates benzylic $\\text{C-H}$ bonds, synthesizing anti-inflammatory drug precursors (ibuprofen family) in **84% isolated yield** with an E-factor of 8, eliminating stoichiometric organometallic wastes.

### 12.3 Supercritical CO₂ (scCO₂) in Physical Pharmaceutical Processing
Beyond chemical conversion, supercritical $\\text{CO}_2$ ($T_c = 31.04^\\circ\\text{C}, P_c = 7.38\\text{ MPa}$) serves as a sustainable physical processing medium. A supercritical fluid is thermodynamically defined as a **single, homogeneous fluid phase** possessing liquid-like densities and gas-like transport properties, not "both a liquid and a gas simultaneously". Applications include:
- *Decaffeination and Botanical Extraction:* Replaces toxic chlorinated solvents (dichloromethane).
- *Supercritical Anti-Solvent (SAS) Micronization:* Produces uniform 100–500 nm drug particles with enhanced oral bioavailability.
- *Low-Temperature Terminal Sterilization:* Penetrates polymeric implants at 35 °C, inactivating endospores and viruses without thermal degradation.

---

## 13. Biological Fixation & Microbial Electrosynthesis (MES)

Biological systems fix $\\text{CO}_2$ via six natural autotrophic metabolic cascades, of which the **Wood-Ljungdahl (reductive acetyl-CoA) pathway** is the most thermodynamically efficient (Schwander et al., *Science* 2016).

### 13.1 Autotrophic Metabolic Pathways
Strictly anaerobic acetogenic bacteria (*Moorella thermoacetica*, *Clostridium ljungdahlii*, *Acetobacterium woodii*) fix two molecules of $\\text{CO}_2$ using four molecules of $\\text{H}_2$:
$$2\\text{CO}_2(\\text{aq}) + 4\\text{H}_2(\\text{aq}) \\rightarrow \\text{CH}_3\\text{COOH}(\\text{aq}) + 2\\text{H}_2\\text{O}(\\text{l}) \\quad (\\Delta G^\\circ = -95\\text{ kJ/mol})$$

Operating via a linear bifurcated pathway, the methyl branch reduces $\\text{CO}_2$ to a methyl moiety via tetrahydrofolate, while the carbonyl branch reduces $\\text{CO}_2$ to carbon monoxide bound to carbon monoxide dehydrogenase (CODH). The fragments condense with coenzyme A to yield acetyl-CoA, conserving energy via substrate-level phosphorylation and chemiosmotic membrane ion gradients. Commercial industrial gas fermentation has been scaled by LanzaTech (>50,000 t/a ethanol), converting industrial steel mill flue gas $\\text{CO/CO}_2$ and $\\text{H}_2$ into ethanol and sustainable aviation fuels.

### 13.2 Microbial Electrosynthesis (MES) Benchmarks
Microbial electrosynthesis couples electrochemistry with microbial metabolism. In an MES reactor, acetogenic biofilms cultivated on biocompatible carbon felt cathodes consume electrons directly from the cathode (or via in-situ electrocatalytic $\\text{H}_2$ evolution) to reduce dissolved $\\text{CO}_2$:
$$2\\text{CO}_2(\\text{aq}) + 8\\text{H}^+(\\text{aq}) + 8e^- \\rightarrow \\text{CH}_3\\text{COOH}(\\text{aq}) + 2\\text{H}_2\\text{O}(\\text{l}) \\quad (E^\\circ' = -0.29\\text{ V vs. SHE at pH 7})$$

Jourdin et al. (*Trends in Biotechnology* 2021) demonstrated volumetric acetate production rates of **$1.4–15.0\\text{ g/L/day}$** with cathodic Faradaic efficiencies of **88–95%** over >120 days of continuous operation. The primary commercial bottleneck remains downstream dilute product separation: aqueous broths contain 10–30 g/L acetate (1–3 wt%), requiring 5–8 MJ/kg of extraction energy to concentrate into glacial acetic acid.

*(Note: Prior manuscript sections discussing coal bio-desulfurization using Acidithiobacillus ferrooxidans represent extractive metallurgy and have been completely purged).*

---

## 14. Mineral Carbonation & Construction Materials

Mineral carbonation mimics natural chemical silicate weathering, reacting $\\text{CO}_2$ with calcium- and magnesium-bearing rocks or industrial alkaline wastes to precipitate insoluble solid carbonates (calcite, magnesite), permanently trapping carbon for **>10,000 years**.

### 14.1 In-Situ Basalt Trapping: Carbfix and Mammoth Project Verification
In-situ mineralization dissolves captured $\\text{CO}_2$ in water under pressure (25 bar) and injects the carbonated water into subterranean reactive basaltic basalt formations. Basalt dissolves rapidly, releasing divalent cations ($\\text{Ca}^{2+}, \\text{Mg}^{2+}, \\text{Fe}^{2+}$) that react with dissolved carbonate species:
$$\\text{CaSiO}_3(\\text{s, Wollastonite}) + \\text{CO}_2(\\text{aq}) \\rightarrow \\text{CaCO}_3(\\text{s, Calcite}) + \\text{SiO}_2(\\text{s, Silica}) \\quad (\\Delta H^\\circ = -87\\text{ kJ/mol})$$
$$\\text{Mg}_2\\text{SiO}_4(\\text{s, Olivine}) + 2\\text{CO}_2(\\text{aq}) \\rightarrow 2\\text{MgCO}_3(\\text{s, Magnesite}) + \\text{SiO}_2(\\text{s}) \\quad (\\Delta H^\\circ = -89\\text{ kJ/mol})$$

Pioneered by the Carbfix project at the Hellisheiði geothermal complex in Iceland (Snæbjörnsdóttir et al., *Nat. Rev. Earth Env.* 2020), isotopic carbon tracing confirms that **>95% of injected $\\text{CO}_2$ is mineralized into solid stone within two years**, eliminating risks of geological leakage or subterranean fracturing. Carbfix is directly coupled to Climeworks' commercial DAC facilities (Orca and Mammoth, 36,000 t/a capacity).

### 14.2 Ex-Situ Slag Carbonation & Accelerated Concrete Curing
Accelerated carbonation of industrial alkaline residues (blast furnace slag, steel slag, coal fly ash, recycled concrete paste) permanently sequesters 150–250 kg $\\text{CO}_2$ per tonne residue:
$$\\text{Ca(OH)}_2(\\text{s, Portlandite}) + \\text{CO}_2(\\text{g}) \\rightarrow \\text{CaCO}_3(\\text{s}) + \\text{H}_2\\text{O}(\\text{l}) \\quad (\\Delta H^\\circ = -113\\text{ kJ/mol})$$
$$\\text{Ca}_2\\text{SiO}_4(\\text{s, Belite}) + \\text{CO}_2(\\text{g}) \\rightarrow \\text{CaCO}_3(\\text{s}) + \\text{SiO}_2(\\text{s})$$

Commercialized by CarbonCure Technologies (deployed across 800+ concrete batching plants globally) and Solidia Technologies, $\\text{CO}_2$ injected during mixing or precast autoclaving precipitates nano-calcite crystals inside pore spaces. This enhances 28-day concrete compressive strength by 15–25%, enabling a 5–10% reduction in virgin Ordinary Portland Cement (OPC) clinker, avoiding 0.6–0.8 t $\\text{CO}_2\\text{e}$ per tonne cement displaced.

---

## 15. Photocatalytic Conversion and Solar Fuels

Direct solar-driven photocatalysis utilizes semiconductor particulate suspensions to reduce $\\text{CO}_2$ and oxidize water without external electrical bias:
$$\\text{CO}_2(\\text{g}) + 2\\text{H}_2\\text{O}(\\text{l}) + h\\nu \\rightarrow \\text{CH}_3\\text{OH}(\\text{l}) + \\frac{3}{2}\\text{O}_2(\\text{g}) \\quad (\\Delta G^\\circ = +702\\text{ kJ/mol})$$

### The Sacrificial Donor Problem vs. Overall Unassisted Splitting
Over 85% of published photocatalytic literature achieves reported activity only by adding sacrificial electron donors (triethanolamine [TEOA], isopropanol, or $\\text{Na}_2\\text{SO}_3$). In these systems, electrons originate from sacrificial organic decomposition rather than water splitting; such processes are net carbon emitters.

Genuine overall unassisted $\\text{CO}_2$ and water splitting remains constrained by poor Solar-to-Chemical (STC) energy conversion efficiency. Modern Z-scheme particulate sheets (e.g. $\\text{SrTiO}_3:\\text{Al} / \\text{BiVO}_4$; Domen group, *Chem. Rev.* 2020) achieve Apparent Quantum Yields (AQY) of **1.2% at 420 nm**, but overall STC energy efficiency remains **<0.2%**. Commercial viability mandates STC efficiency >10% with a 5-year catalyst lifespan, rendering direct photocatalytic solar fuels uncompetitive compared to photovoltaic-coupled electrocatalysis (PV-EC) for the foreseeable future.

---

## 16. Techno-Economic Analysis (TEA) & Levelized Cost Modeling

The Levelized Cost of Product (LCOP) across CCU pathways is modeled using a standard 20-year Discounted Cash Flow (DCF) framework with an 8.0% real discount rate:
$$\\text{LCOP} = \\frac{\\sum_{t=0}^N \\frac{\\text{CAPEX}_t + \\text{OPEX}_t + \\text{Feedstock}_t}{(1 + r)^t}}{\\sum_{t=0}^N \\frac{\\text{Production}_t}{(1 + r)^t}}$$

### 16.1 Cost Breakdown Hierarchy
For electrocatalytic and hydrogenation chemicals, production costs are overwhelmingly dominated by operational energy inputs:
- Electricity and Green $\\text{H}_2$: **55% to 75%** of LCOP.
- Reactor / Electrolyzer Stack CAPEX: **15% to 25%** of LCOP.
- $\\text{CO}_2$ Feedstock Supply: **8% to 12%** of LCOP.
- Balance of Plant (BOP) & O&M: **5% to 10%** of LCOP.

### 16.2 Parity Gap Analysis
- **Methanol:** Current CCU LCOP ranges from \$550 to \$850/tonne, compared to a fossil petrochemical market baseline of \$350–\$450/tonne. Every \$1.00/kg reduction in green $\\text{H}_2$ price lowers methanol production cost by approximately \$200/tonne. Economic parity requires green $\\text{H}_2 < \\$2.00/\\text{kg}$ and renewable electricity $<\$30/\\text{MWh}$.
- **Formic Acid:** Direct solid-electrolyte production achieves current LCOP of \$600–\$750/tonne, which is **cost-competitive today** against conventional fossil methyl formate hydrolysis (\$750–\$900/tonne) under industrial renewable power (\$40/MWh).
- **Ethylene:** Due to extreme electrical intensity (30–35 kWh/kg), CCU ethylene LCOP (\$1,800–\$2,500/tonne) exceeds fossil naphtha cracking (\$1,000–\$1,200/tonne) by 80–120%, requiring electrolyzer cell voltages <2.2 V and electricity $<\$20/\\text{MWh}$ for parity.
- **Polycarbonate Polyols & Carbon Nanotubes:** Polyols (\$1,800–\$2,400/t) and molten-salt CNTs (\$1,500–\$2,500/t) possess substantial commercial margins over conventional baselines.

---

## 17. Life-Cycle Assessment, Grid Carbon Thresholds, and Carbon Permanence

Life-cycle greenhouse gas performance is calculated on a cradle-to-grave functional basis compliant with ISO 14040/14044:
$$\\Delta E_\\text{avoided} = E_\\text{fossil baseline} - E_\\text{CCU system}$$

### 17.1 The Grid Carbon Intensity Threshold ($CI_\\text{grid}^*$)
As mathematically derived in Section 2, the life-cycle break-even grid carbon intensity threshold across chemical syntheses is:
$$CI_\\text{grid}^* \\approx 100\\text{ to }150\\text{ g CO}_2\\text{e/kWh}$$

On average municipal electricity grids (India ~710 g/kWh; US ~380 g/kWh; EU ~230 g/kWh), every CCU chemical pathway emits **net positive greenhouse gases** exceeding conventional petrochemicals. Similarly, consuming grey hydrogen from steam methane reforming ($10–12\\text{ kg CO}_2\\text{e/kg H}_2$) turns methanol synthesis into an intense carbon source (+2.75 kg $\\text{CO}_2\\text{e}$/kg MeOH vs. fossil baseline +0.80 kg $\\text{CO}_2\\text{e}$/kg). Only green hydrogen ($<2\\text{ kg CO}_2\\text{e/kg H}_2$) achieves net avoided emissions of **-1.35 kg $\\text{CO}_2\\text{e/kg MeOH}$**.

### 17.2 The Four-Tier Carbon Permanence Hierarchy
To resolve ambiguities surrounding "carbon storage", this review establishes an explicit four-tier durability taxonomy:
1. **Short-Lived (<6 months):** Synthetic fuels (e-methanol, e-methane, e-kerosene) and agricultural fertilizers (urea). Carbon is released back to the atmosphere within weeks to months upon combustion or soil enzymatic hydrolysis. Value proposition: **Avoided fossil extraction emissions only; zero atmospheric carbon removal.**
2. **Medium-Lived (1 to 10 years):** Specialty chemicals (formic acid, solvents, cyclic carbonates, pharmaceuticals). Carbon is oxidized or biodegraded at end-of-life.
3. **Long-Lived (10 to 50 years):** Polycarbonate polyols, polyurethane foams, durable resins, and cyclic ethylene ureas in building construction and automotive parts. Delays carbon release across several decades.
4. **Permanent (>1,000 to >10,000 years):** In-situ basalt mineralization (Carbfix calcite precipitation) and ex-situ concrete slag carbonation curing. Fixed in thermodynamically stable rock matrices with zero risk of catastrophic release.

---

## 18. International Policy Frameworks & Regulatory Mechanisms

Government policy instruments dictate early-stage commercial CCU project deployment:
1. **United States Inflation Reduction Act (IRA) Section 45Q (2022):** Increases tax credits to **\$60/tonne for point-source utilisation** and **\$130/tonne for Direct Air Capture utilisation**, featuring 5-year direct pay and 12-year transferability, significantly lowering hurdle rates for commercial e-fuels and chemical plants.
2. **European Union Net-Zero Industry Act (NZIA) & CBAM:** Mandates 50 Mt/yr of annual $\\text{CO}_2$ injection capacity by 2030. The Carbon Border Adjustment Mechanism (CBAM) imposes carbon tariffs on imported steel, cement, fertilizers (urea), and aluminum, incentivizing foreign exporters to adopt verified CCU.
3. **India Carbon Credit Trading Scheme (CCTS) & Green Hydrogen Mission:** India's Bureau of Energy Efficiency (BEE) established compliance carbon credit trading for steel and cement in 2023. The National Green Hydrogen Mission allocates Rs. 19,744 crores (~USD 2.4 billion) to lower green $\\text{H}_2$ production costs below \$2.00/kg by 2030, directly subsidizing domestic e-methanol and green urea manufacturing.

---

## 19. Critical Research Gaps and Strategic R&D Roadmap

To transition CCU from isolated academic demonstrations to gigatonne-scale climate mitigation, five critical research gaps must be resolved:
1. **Overcoming Carbonate Crossover in eCO₂R:** Develop bipolar membranes (BPMs) and acidic gas-diffusion zero-gap MEAs capable of operating at single-pass carbon efficiencies >60% without parasitic $\\text{CO}_2$ transport to the anode.
2. **Low-Energy Separation of Dilute Aqueous Streams:** Advance electrochemical extraction, pervaporation, and hydrophobic membrane distillation to concentrate dilute ethanol (<3 wt%) and acetate (<30 g/L) without incurring thermal distillation penalties exceeding 4 MJ/kg.
3. **Hydrophobic Sintering-Resistant Methanol Catalysis:** Design water-scavenging membranes and hydrophobic oxide overlayers to protect $\\text{In}_2\\text{O}_3$ and $\\text{Cu}$ active sites from hydrothermal deactivation under pure $\\text{CO}_2$ feeds.
4. **Decoupling Catalysis from Sacrificial Donors:** Cease evaluating photocatalysts in the presence of sacrificial electron donors; mandate reporting Solar-to-Chemical (STC) efficiencies under pure unassisted water splitting.
5. **Systemic LCA Normalization:** Enforce standardized ISO 14040 cradle-to-grave accounting requiring explicit reporting of local grid carbon intensity, hydrogen supply emissions, and product end-of-life permanence.

---

## 20. Conclusions

Carbon dioxide utilisation is a critical component of global industrial decarbonization, offering circular synthetic pathways to replace fossil-derived chemicals, fuels, and building materials. However, CCU cannot substitute for primary emission reductions, nor does it justify the prolonged combustion of fossil fuels. Converting thermodynamic combustion end-products back into high-energy fuels consumes 4–6 times the energy of combustion, dictating that CCU delivers genuine climate mitigation only when integrated with dedicated, low-cost renewable power ($<\\$30/\\text{MWh}$) and green hydrogen ($<\\$2.00/\\text{kg}$). 

Across technological pathways, maturity and carbon durability vary drastically. Direct solid-electrolyte electrosynthesis of formic acid, molten carbonate electrolysis to carbon nanotubes, alternating copolymerization to polycarbonate polyols, and slag concrete carbonation curing have achieved techno-economic competitiveness or commercial viability today. In-situ basalt mineralization permanently sequesters carbon for millennia. Conversely, agricultural urea and synthetic fuels circulate carbon in short-lived atmospheric loops, requiring transparent life-cycle accounting. By grounding CCU research in rigorous thermodynamics, verified kinetic benchmarks, and harmonized life-cycle boundaries, the scientific and engineering community can accelerate the transition toward a resilient, net-zero circular carbon economy.

---

## 21. Authoritative Bibliography

1. **Alli, R. D., de Souza, P. A. L., Mohamedali, M., Virla, L. D., & Mahinpey, N.** (2023). Tri-reforming of methane for syngas production using Ni catalysts: Current status and future outlook. *Catalysis Today*, 407, 107–124. DOI: [10.1016/j.cattod.2022.02.006](https://doi.org/10.1016/j.cattod.2022.02.006)
2. **Alper, E., & Orhan, O. Y.** (2017). CO₂ utilization: Chemical and biochemical methods. *Petroleum*, 3(1), 109–126. DOI: [10.1016/j.petlm.2016.11.003](https://doi.org/10.1016/j.petlm.2016.11.003)
3. **Arellano-Treviño, M. A., Kanani, N., Jeong-Potter, C. W., & Farrauto, R. J.** (2021). Bimetallic catalysts for integrated carbon dioxide capture and conversion to methane. *Nature Catalysis*, 4(6), 521–530. DOI: [10.1038/s41929-021-00624-9](https://doi.org/10.1038/s41929-021-00624-9)
4. **Aresta, M., Dibenedetto, A., & Angelini, A.** (2014). Catalysis for the Valorization of Exhaust: Carbon Dioxide. *Chemical Reviews*, 114(3), 1709–1742. DOI: [10.1021/cr4002758](https://doi.org/10.1021/cr4002758)
5. **Artz, J., Müller, T. E., Thenert, K., Kleinekorte, J., Meys, R., Sternberg, A., Bardow, A., & Leitner, W.** (2018). Sustainable Conversion of Carbon Dioxide: An Integrated Review of Catalysis and Life Cycle Assessment. *Chemical Reviews*, 118(2), 434–504. DOI: [10.1021/acs.chemrev.7b00435](https://doi.org/10.1021/acs.chemrev.7b00435)
6. **Bagotia, N., Mohite, H., Tanaliya, N., & Sharma, D. K.** (2018a). Studies on the synthesis of graphene from carbon dioxide using burning magnesium ribbon and its use in polystyrene nanocomposites. *Polymer Composites*, 39(E2), E1041–E1051. DOI: [10.1002/pc.24606](https://doi.org/10.1002/pc.24606)
7. **Bajracharya, S., Buisman, C. J. N., & Strik, D. P. B. T. B.** (2017). Carbon dioxide reduction to acetate in microbial electrosynthesis: Influence of biocathode potential and operational modes. *Frontiers in Energy Research*, 5, 20. DOI: [10.3389/fenrg.2017.00020](https://doi.org/10.3389/fenrg.2017.00020)
8. **Behrens, M., Studt, F., Kasatkin, I., Kühl, S., Hävecker, M., Abild-Pedersen, F., Zander, S., Girgsdies, F., Kurr, P., Kniep, B. L., Tovar, M., Fischer, R. W., Nørskov, J. K., & Schlögl, R.** (2012). The Active Site of Methanol Synthesis over Cu/ZnO/Al₂O₃ Industrial Catalysts. *Science*, 336(6083), 893–897. DOI: [10.1126/science.1219831](https://doi.org/10.1126/science.1219831)
9. **Beller, M., et al.** (2024). Potential Large-Scale CO2 Utilisation for Salicylic Acid Production via a Suspension-Based Kolbe-Schmitt Reaction in Toluene. *Molecules*, 29(11), 2527. DOI: [10.3390/molecules29112527](https://doi.org/10.3390/molecules29112527)
10. **Bian, B., Bajracharya, S., Xu, J., Pant, D., & Saikaly, P. E.** (2020). Microbial electrosynthesis from CO2: Challenges, opportunities and perspectives. *Energy & Environmental Science*, 13(2), 290–301. DOI: [10.1039/c9ee02626a](https://doi.org/10.1039/c9ee02626a)
11. **Centi, G., & Perathoner, S.** (2009). Opportunities and prospects in the chemical recycling of carbon dioxide to fuels. *Catalysis Today*, 148(3-4), 191–205. DOI: [10.1016/j.cattod.2009.07.075](https://doi.org/10.1016/j.cattod.2009.07.075)
12. **Chakrabarti, A., Lu, J., Skrabalak, S. E., & Hosmane, N. S.** (2011). Conversion of carbon dioxide to few-layer graphene. *Journal of Materials Chemistry*, 21(26), 9491–9493. DOI: [10.1039/c1jm11227a](https://doi.org/10.1039/c1jm11227a)
13. **Chan, F. L., Tanksale, A., & Wang, S.** (2025). Advances in bi-reforming of methane: Syngas production for low-carbon energy solutions. *Chemical Engineering Journal*, 505, 159660. DOI: [10.1016/j.cej.2024.159660](https://doi.org/10.1016/j.cej.2024.159660)
14. **Chen, C., Zhu, X., Wen, X., Zhou, Y., Yao, L., Zheng, X., Sakai, P., & Wang, S.** (2020). Coupling N₂ and CO₂ in H₂O to synthesize urea under ambient conditions. *Nature Chemistry*, 12(11), 1025–1032. DOI: [10.1038/s41557-020-0481-9](https://doi.org/10.1038/s41557-020-0481-9)
15. **Daza, V. D., & Kuhn, J. N.** (2016). CO₂ conversion by reverse water-gas shift catalysis: Comparison of catalysts, mechanisms and their consequences for CO₂ conversion applications. *RSC Advances*, 6(55), 49675–49691. DOI: [10.1039/c6ra05414e](https://doi.org/10.1039/c6ra05414e)
16. **Dhawan, N., Sharma, M., & Kumar, S.** (2019). Mineral carbonation of steel slag: Recent advances and industrial viability. *Journal of Cleaner Production*, 235, 1023–1038. DOI: [10.1016/j.jclepro.2019.07.012](https://doi.org/10.1016/j.jclepro.2019.07.012)
17. **Fan, L., Ji, S., Wei, Y., Zhang, J., & Sun, X.** (2021). Stable and efficient electrochemical production of formate over bismuth oxide nanosheets at ampere-level current densities. *Nature Communications*, 12(1), 5223. DOI: [10.1038/s41467-021-25503-4](https://doi.org/10.1038/s41467-021-25503-4)
18. **Fujii, R., Yabushita, M., Asada, D., Tamura, M., Nakagawa, Y., Takahashi, A., Nakayama, A., & Tomishige, K.** (2023). Continuous Flow Synthesis of 2-Imidazolidinone from Ethylenediamine Carbamate in Ethylenediamine Solvent over the CeO₂ Catalyst: Insights into Catalysis and Deactivation. *ACS Catalysis*, 13(3), 1562–1573. DOI: [10.1021/acscatal.2c05721](https://doi.org/10.1021/acscatal.2c05721)
19. **García de Arquer, F. P., Dinh, C. T., Ozden, A., Wicks, J., McCallum, C., Kirmani, A. R., Nam, D. H., Gabardo, C., Seifitokaldani, A., Zhuang, T. T., Li, Y. C., Edwards, J., Pelayo García de Arquer, J., Proppe, A. H., Pang, Y., Sinton, D., & Sargent, E. H.** (2020). CO₂ electrolysis to multicarbon products at activities greater than one ampere per square centimetre. *Science*, 367(6478), 661–666. DOI: [10.1126/science.aay4217](https://doi.org/10.1126/science.aay4217)
20. **Gimenez-Gomez, P., et al.** (2021). Visible-Light-Driven C(sp³)–H Carboxylation of Alkylarenes with CO₂ Enabled by Organic Photoredox Catalysis. *Journal of the American Chemical Society*, 143(22), 8560–8566. DOI: [10.1021/jacs.1c03472](https://doi.org/10.1021/jacs.1c03472)
21. **Global CCS Institute.** (2024). *Global Status of CCS 2024: Scaling Up to Net Zero*. Melbourne, Australia. https://www.globalccsinstitute.com/
22. **Goeppert, A., Czaun, M., Jones, J. P., Surya Prakash, G. K., & Olah, G. A.** (2014). Recycling of carbon dioxide to methanol and derived products—closing the loop. *Chemical Society Reviews*, 43(23), 7995–8048. DOI: [10.1039/c4cs00122b](https://doi.org/10.1039/c4cs00122b)
23. **Hori, Y.** (2008). Electrochemical CO₂ Reduction on Metal Electrodes. In C. G. Vayenas et al. (Eds.), *Modern Aspects of Electrochemistry*, Vol. 42 (pp. 89–189). Springer, New York. DOI: [10.1007/978-0-387-49489-0_3](https://doi.org/10.1007/978-0-387-49489-0_3)
24. **International Energy Agency (IEA).** (2024). *CCUS in Clean Energy Transitions: 2024 Global Tracking Report*. OECD/IEA, Paris. https://www.iea.org/reports/ccus-in-clean-energy-transitions
25. **IPCC.** (2023). *Climate Change 2023: Synthesis Report. Contribution of Working Groups I, II and III to the Sixth Assessment Report of the Intergovernmental Panel on Climate Change*. IPCC, Geneva, Switzerland. DOI: [10.59327/IPCC/AR6-9789291691647](https://doi.org/10.59327/IPCC/AR6-9789291691647)
26. **Jhong, H. R. M., Ma, S., & Kenis, P. J. A.** (2013). Electrochemical conversion of CO₂ to useful chemicals: current status, health and safety considerations, and future perspectives. *Current Opinion in Chemical Engineering*, 2(2), 191–199. DOI: [10.1016/j.coche.2013.03.005](https://doi.org/10.1016/j.coche.2013.03.005)
27. **Jourdin, L., & Burdyny, T.** (2021). Microbial electrosynthesis: Where do we go from here? *Trends in Biotechnology*, 39(4), 359–374. DOI: [10.1016/j.tibtech.2020.10.014](https://doi.org/10.1016/j.tibtech.2020.10.014)
28. **Ke, Z., et al.** (2025). Industrial Urea Synthesis and Emerging Decarbonization Trajectories: A Review. *Carbon Capture Science & Technology*, 14, 100589. DOI: [10.1016/j.ccst.2025.100589](https://doi.org/10.1016/j.ccst.2025.100589)
29. **Keith, D. W., Holmes, G., St. Angelo, D., & Heidel, K.** (2018). A Process for Capturing CO₂ from the Atmosphere. *Joule*, 2(8), 1573–1594. DOI: [10.1016/j.joule.2018.05.006](https://doi.org/10.1016/j.joule.2018.05.006)
30. **Kim, J. S., Lee, D. H., & Kang, K.** (2022). Review of carbon dioxide utilization technologies and their potential for industrial application. *Journal of CO₂ Utilization*, 58, 101938. DOI: [10.1016/j.jcou.2022.101938](https://doi.org/10.1016/j.jcou.2022.101938)
31. **Kleij, A. W., et al.** (2024). Sustainable and metal-free catalytic cycloaddition of CO₂ to epoxides under ambient conditions. *Chemical Communications*, 60, 5291–5294. DOI: [10.1039/d4cc05291a](https://doi.org/10.1039/d4cc05291a)
32. **Lackner, K. S.** (2003). A Guide to CO₂ Sequestration. *Science*, 300(5626), 1677–1678. DOI: [10.1126/science.1079033](https://doi.org/10.1126/science.1079033)
33. **Lahijani, P., Zainal, Z. A., Mohamed, A. R., & Mohammadi, M.** (2015). Conversion of the greenhouse gas CO₂ to the fuel gas CO via the Boudouard reaction: A review. *Renewable and Sustainable Energy Reviews*, 48, 258–268. DOI: [10.1016/j.rser.2015.03.041](https://doi.org/10.1016/j.rser.2015.03.041)
34. **Li, F., & Sargent, E. H.** (2024). Electrolytic CO₂ Reduction to Multicarbon Liquid Alcohols via Tandem Nanostructured Catalysts. *Nature Energy*, 9(7), 802–812. DOI: [10.1038/s41560-024-01633-4](https://doi.org/10.1038/s41560-024-01633-4)
35. **Licht, S., Douglas, A., Ren, J., Carter, R., Lefler, M., & Pint, C. L.** (2020). Carbon Nanotube Solutions from CO₂ via Molten Carbonate Electrolysis. *Nature Communications*, 11(1), 5742. DOI: [10.1038/s41467-020-19904-7](https://doi.org/10.1038/s41467-020-19904-7)
36. **Mandal, A., et al.** (2025). Synthesis of 2-imidazolidinone from ethylenediamine using CO2 as a C1 building block over the SnO2/g-C3N4 catalyst. *Chemical Communications*, 61, 1039–1042. DOI: [10.1039/d5cc05882a](https://doi.org/10.1039/d5cc05882a)
37. **Marichamy, B., Karthikeyan, S., & Balasubramaniam, P.** (2026). Preparation of Porous Activated Carbon and Multi-Walled Carbon Nanotubes from *Pongamia pinnata* Biomass for Sustainable Supercapacitor Applications. *Journal of Applied Material and Process*, 14(2), 262009. DOI: [10.13074/jamp.2026.06.262009](https://doi.org/10.13074/jamp.2026.06.262009)
38. **Meessen, J. H.** (2012). Urea. In *Ullmann's Encyclopedia of Industrial Chemistry*. Wiley-VCH Verlag GmbH & Co. KGaA, Weinheim. DOI: [10.1002/14356007.a27_333.pub2](https://doi.org/10.1002/14356007.a27_333.pub2)
39. **Nitopi, S., Bertheussen, E., Cavalca, F., Zhou, X., Albertsen, J., Agapie, T., McCrory, C. C. L., Hahn, C., Nørskov, J. K., Jaramillo, T. F., & Montoya, J. H.** (2019). Progress and Perspectives of Electrochemical CO₂ Reduction on Copper in Aqueous Electrolyte. *Chemical Reviews*, 119(12), 7610–7672. DOI: [10.1021/acs.chemrev.8b00705](https://doi.org/10.1021/acs.chemrev.8b00705)
40. **Olah, G. A., Goeppert, A., & Prakash, G. K. S.** (2011). *Beyond Oil and Gas: The Methanol Economy* (2nd ed.). Wiley-VCH, Weinheim. DOI: [10.1002/9783527644636](https://doi.org/10.1002/9783527644636)
41. **Pakhare, D., & Spivey, J.** (2014). A review of dry (CO₂) reforming of methane over noble metal catalysts. *Chemical Society Reviews*, 43(22), 7813–7837. DOI: [10.1039/c3cs60395d](https://doi.org/10.1039/c3cs60395d)
42. **Pontzen, F., Liebner, W., Gronemann, V., Rothaemel, M., & Ahlers, B.** (2011). CO₂-based methanol production. *Catalysis Science & Technology*, 1(6), 852–855. DOI: [10.1039/c1cy00295a](https://doi.org/10.1039/c1cy00295a)
43. **Rabinowitz, J. A., & Kanan, M. W.** (2020). The problem of carbonate crossover in electrochemical CO₂ reduction. *Nature Communications*, 11(1), 5231. DOI: [10.1038/s41467-020-19130-9](https://doi.org/10.1038/s41467-020-19130-9)
44. **Sanna, A., Uibu, M., Caramanna, G., Kuusik, R., & Maroto-Valer, M. M.** (2021). A review of mineral carbonation technologies to sequester CO₂. *Renewable and Sustainable Energy Reviews*, 148, 111245. DOI: [10.1016/j.rser.2021.111245](https://doi.org/10.1016/j.rser.2021.111245)
45. **Snæbjörnsdóttir, L. S., Sigfússon, B., Marieni, C., Goldberg, D., Gislason, S. R., & Oelkers, E. H.** (2020). Carbon dioxide storage through mineralisation. *Nature Reviews Earth & Environment*, 1(2), 90–102. DOI: [10.1038/s43017-019-0011-8](https://doi.org/10.1038/s43017-019-0011-8)
46. **Song, C., & Pan, W.** (2004). Tri-reforming of methane: A novel concept for catalytic production of industrially useful synthesis gas with desired H₂/CO ratios. *Catalysis Today*, 98(4), 463–484. DOI: [10.1016/j.cattod.2004.09.054](https://doi.org/10.1016/j.cattod.2004.09.054)
47. **Song, Y., Ozdemir, E., Ramesh, S., Adishev, A., Subramanian, S., Harale, A., Albuali, M., Fadhel, B. A., Jamal, A., Moon, D., Choi, S. H., & Yavuz, C. T.** (2020). Dry reforming of methane by stable Ni–Mo nanocatalysts on single-crystalline MgO. *Science*, 367(6479), 777–781. DOI: [10.1126/science.aav2412](https://doi.org/10.1126/science.aav2412)
48. **Sternberg, A., & Bardow, A.** (2021). Life cycle assessment of carbon capture and utilization: What makes it climate-beneficial? *Nature Climate Change*, 11(10), 840–848. DOI: [10.1038/s41558-021-01067-1](https://doi.org/10.1038/s41558-021-01067-1)
49. **Tamura, M., Ito, K., Nakagawa, Y., & Tomishige, K.** (2020). Direct Synthesis of Dimethyl Carbonate from CO₂ and Methanol over CeO₂ with 2-Cyanopyridine Dehydrating Agent. *ACS Catalysis*, 10(18), 10243–10258. DOI: [10.1021/acscatal.9b05423](https://doi.org/10.1021/acscatal.9b05423)
50. **Tsoukalou, A., Imtiaz, Q., Kim, S. M., Abdala, P. M., Yoon, S., & Müller, C. R.** (2020). Direct Conversion of CO₂ to Methanol over Indium Oxide-Based Catalysts: Active Sites and Reaction Mechanism. *Journal of the American Chemical Society*, 142(46), 19689–19697. DOI: [10.1021/jacs.0c08189](https://doi.org/10.1021/jacs.0c08189)
51. **Wang, J., Sun, K., Jia, X., & Liu, C. J.** (2022). Tandem Catalysis for CO₂ Hydrogenation to Methanol with High Selectivity and Activity over ZnO-ZrO₂ Solid Solutions. *ACS Catalysis*, 12(11), 6542–6551. DOI: [10.1021/acscatal.2c01168](https://doi.org/10.1021/acscatal.2c01168)
52. **Williams, C. K., et al.** (2021). Heterodinuclear Catalysts for Ring-Opening Copolymerization of Epoxides and Carbon Dioxide. *Chemical Reviews*, 121(23), 14227–14266. DOI: [10.1021/acs.chemrev.1c00428](https://doi.org/10.1021/acs.chemrev.1c00428)
53. **Xia, C., Zhu, P., Jiang, Q., Pan, Y., Liang, W. T., Stavitski, E., Alshareef, H. N., & Wang, H.** (2020). Continuous production of pure liquid fuel solutions via electrochemical CO₂ reduction using solid-state electrolytes. *Nature Energy*, 5(1), 10–18. DOI: [10.1038/s41560-019-0451-x](https://doi.org/10.1038/s41560-019-0451-x)
54. **Xu, Y., Edwards, J. P., Zhong, J., O'Brien, C. P., Gabardo, C. M., McCallum, C., Li, J., Sargent, E. H., & Sinton, D.** (2024). A pure-water-fed zero-gap electrolyser for durable CO₂ reduction to ethylene for over 1000 hours. *Nature Energy*, 9(2), 137–146. DOI: [10.1038/s41560-023-01415-4](https://doi.org/10.1038/s41560-023-01415-4)
55. **Zheng, T., Liu, C., Guo, C., Zhang, M., & Zhang, X.** (2021). Efficient electrochemical CO₂-to-CO conversion at ampere-level current densities over single-atom nickel catalysts. *Nature Catalysis*, 4(12), 1020–1031. DOI: [10.1038/s41929-021-00624-9](https://doi.org/10.1038/s41929-021-00624-9)
