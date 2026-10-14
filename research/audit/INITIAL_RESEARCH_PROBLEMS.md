# Initial Research Problems & Critical Scientific Audit

**Document:** `research/audit/INITIAL_RESEARCH_PROBLEMS.md`  
**Focus:** Foundational scientific, thermodynamic, chemical, and methodological errors identified in the original manuscript.  
**Audit Date:** October 2026

---

## Executive Summary of Identified Problems

The baseline manuscript (*"Advancements in Carbon Dioxide Utilisation: Pathways to Sustainable Chemicals, Fuels, and Materials for a Net-Zero Future"*) provides a broad topical overview of CO₂ utilisation pathways. However, a rigorous scientific and peer-review level evaluation reveals severe foundational flaws across five major categories:
1. **Thermodynamic & Conceptual Fallacies** (justifying unabated fossil power generation through CCU; misunderstanding energy conservation and net-zero accounting).
2. **Chemical Inaccuracies & Mechanistic Gaps** (confusing absorption solvents with catalysts, incorrect chemical formulas, incomplete reaction steps, ignoring side reactions).
3. **Misrepresentation of Physical Phenomena & Materials** (misdefining supercritical fluid phase; portraying violent magnesium combustion as direct pristine graphene synthesis without upstream/downstream balances).
4. **Methodological Deficiencies** (absence of reproducible search protocols, unquantified tables, arbitrary timeline framing).
5. **Bibliographic & Editorial Anomalies** (severe author self-citation bias, search-and-replace corruptions, media URL citations, typographical errors in numerical market values).

---

## 1. Thermodynamic & Conceptual Fallacies

### 1.1 The "Fossil-Fuel Justification" Fallacy
- **Manuscript Text:**  
  - *Abstract (Page 1):* "...supports global efforts to achieve net-zero emissions and increase possibilities of continued use of fossil fuels such as coal, petroleum and natural gas."  
  - *Introduction (Pages 2–3):* "...enabling the continued use of fossil fuels by converting CO₂ into value-added products... Since there are extensive reserves of coal, a cheaper source of energy available in the world, therefore, there is a grave need for exploring economical possibilities of their continued use for power generation."  
  - *Conclusion (Page 22):* "If the cost-effective CCSU technologies become available then it may become environmentally cleaner to use coal and future generations may not have to depend only on renewable energy sources which have their own issues."
- **Scientific Reality & Rebuttal:**  
  - **Thermodynamic Impossibility:** Coal combustion releases chemical energy by converting reduced carbon to fully oxidized carbon ($\text{C} + \text{O}_2 \rightarrow \text{CO}_2, \Delta H^\circ = -393.5\text{ kJ/mol}$). To convert $\text{CO}_2$ back into a chemical fuel (e.g., methanol: $\text{CO}_2 + 3\text{H}_2 \rightarrow \text{CH}_3\text{OH} + \text{H}_2\text{O}$), the energetic input required to generate the stoichiometric $H_2$ via water electrolysis ($\Delta H^\circ = +285.8\text{ kJ/mol } \text{H}_2$, or $3 \times 285.8 = +857.4\text{ kJ/mol } \text{CO}_2$) is more than **double** the energy originally released by coal combustion.
  - **Systemic Efficiency:** Generating electricity from coal (thermal efficiency 33–38%), capturing CO₂ (25–35% parasitic energy penalty), electrolyzing water to generate green $H_2$, and synthesizing synthetic fuel results in an overall round-trip efficiency of **<15%**. Using coal to produce synthetic fuel via CCU produces vastly higher emissions and consumes vastly more resources than direct electrification or direct renewable energy deployment.
  - **Uncaptured Residual Emissions:** State-of-the-art post-combustion capture achieves 90–95% capture efficiency under steady-state conditions; transient load changes reduce this further. The remaining 5–10% of emissions, coupled with upstream methane leaks from coal mining, continue to accumulate in the atmosphere.
  - **Peer-Review Risk:** Any review claiming that CCU justifies burning coal and avoids the need for renewable energy will face immediate rejection by reputable energy and environmental journals (e.g., *Energy & Environmental Science*, *Chemical Reviews*, *Nature Energy*).
  - **Mandatory Action:** Completely purge all assertions that CCU enables unabated coal combustion. Frame CCU strictly in its scientifically validated role: a circular carbon tool to supply non-fossil carbon feedstocks to essential chemical and aviation sectors that cannot be decarbonized by direct electrification alone.

---

## 2. Chemical Inaccuracies & Mechanistic Errors

### 2.1 Misattribution of KS-21 Solvent as a Hydrogenation Catalyst
- **Manuscript Text (Table 2, Page 8):** Under *Hydrogenation / Recent Advances*, the manuscript lists: *"KS-21 solvent; 88% CO₂ conversion"*.
- **Scientific Reality:**  
  - **KS-21** is a proprietary sterically hindered amine solvent developed jointly by Mitsubishi Heavy Industries (MHI) and Kansai Electric Power for **post-combustion chemical absorption capture** (commercialized in the KM CDR Process™ / Advanced KM CDR Process™).
  - KS-21 has **zero** catalytic function in thermocatalytic or electrochemical hydrogenation. Attributing it as a hydrogenation advance is a severe technical error that reveals an uncritical blending of capture and conversion literature.
- **Mandatory Action:** Remove KS-21 from Table 2 hydrogenation rows. Relocate KS-21 to Section 5 under solvent absorption capture technologies.

### 2.2 Typo in Ammonium Carbamate Chemical Formula
- **Manuscript Text (Section 5.2, Page 10):** Writes the intermediate for urea synthesis as:
  $$2\text{NH}_3 + \text{CO}_2 \rightarrow \text{NH}_4\text{NH}_2\text{COO} \rightarrow \text{CO(NH}_2)_2 + \text{H}_2\text{O}$$
- **Scientific Reality:**  
  - Ammonium carbamate is the ionic salt of carbamic acid: $[\text{NH}_4]^+[\text{NH}_2\text{COO}]^-$, conventionally written as $\text{NH}_2\text{COONH}_4$.
  - "$\text{NH}_4\text{NH}_2\text{COO}$" is an erroneous chemical formula.
- **Mandatory Action:** Correct formula to $\text{NH}_2\text{COONH}_4$ and detail the thermodynamics of the two-step synthesis:
  1. Carbamate formation: $2\text{NH}_3(\text{g}) + \text{CO}_2(\text{g}) \rightleftharpoons \text{NH}_2\text{COONH}_4(\text{s}) \quad (\Delta H^\circ_{298\text{K}} = -117\text{ kJ/mol, exergonic})$
  2. Dehydration: $\text{NH}_2\text{COONH}_4(\text{l}) \rightleftharpoons \text{CO(NH}_2)_2(\text{l}) + \text{H}_2\text{O}(\text{l}) \quad (\Delta H^\circ_{298\text{K}} = +15.5\text{ kJ/mol, endergonic})$

### 2.3 Table 2 Typographical Error (Product of Electrochemical Reduction)
- **Manuscript Text (Table 2, Page 8):** Under *Electrochemical / Products*, lists: *"Formic acid, CO₂, Ethanol"*.
- **Scientific Reality:** Listing $\text{CO}_2$ as a product of electrochemical $\text{CO}_2$ reduction is an obvious typo for Carbon Monoxide ($\text{CO}$).
- **Mandatory Action:** Correct to $\text{CO}$.

### 2.4 Incomplete Grignard Reaction Equation
- **Manuscript Text (Section 7.1, Page 14):** Writes:
  $$\text{R-MgX} + \text{CO}_2 - \text{R-COOH}$$
- **Scientific Reality:**  
  - Grignard addition to $\text{CO}_2$ produces a magnesium carboxylate salt: $\text{R-COOMgX}$.
  - The reaction requires a separate, stoichiometric aqueous acidic protonation step: $\text{R-COOMgX} + \text{H}_3\text{O}^+ \rightarrow \text{R-COOH} + \text{Mg}^{2+} + \text{X}^- + \text{H}_2\text{O}$.
  - Without aqueous acid quenching, carboxylic acid cannot be isolated.
  - Furthermore, claiming this is an environmentally benign "green" reaction because of "high atom economy" ignores that Grignard reagents require pyrophoric metallic magnesium, flammable dry ethers (THF/diethyl ether), and generate equimolar stoichiometric magnesium halide wastes ($E\text{-factor} \gg 10$).
- **Mandatory Action:** Write both steps accurately; balance the equation; critically discuss modern catalytic non-organometallic carboxylations (photoredox C–H carboxylation).

### 2.5 Magnesiothermic Reduction Exaggeration
- **Manuscript Text (Section 6, Pages 11–13):** Claims burning magnesium ribbon in solid $\text{CO}_2$ selectively synthesizes graphene and carbon nanotubes for advanced composites.
- **Scientific Reality:**  
  - The reaction $\text{CO}_2 + 2\text{Mg} \rightarrow 2\text{MgO} + \text{C}$ is a violent, uncontrolled exothermic combustion ($\Delta H^\circ = -810\text{ kJ/mol}$, temperatures exceeding 2000°C).
  - The resulting solid is a heterogeneous mixture of MgO and highly defective disordered graphitic carbon, requiring severe acid washing ($\text{HCl}$ or $\text{HF}$) to extract the carbon.
  - Upstream magnesium extraction (e.g., Pidgeon thermal reduction of dolomite) emits 15–25 kg $\text{CO}_2\text{e}$ per kg Mg produced. Consuming 2.02 kg of Mg to fix 1.0 kg of $\text{CO}_2$ generates ~30–50 kg of upstream $\text{CO}_2$ emissions!
- **Mandatory Action:** Include mass and life-cycle emission balances for magnesiothermic reduction; highlight newer, more sustainable approaches such as molten salt electrochemical reduction to CNTs.

---

## 3. Misrepresentation of Physical Phenomena & Speciation

### 3.1 Supercritical CO₂ Definition Error
- **Manuscript Text (Section 7.3, Page 14):** States that supercritical $\text{CO}_2$ is *"a dual solvent, both liquid and gas"*.
- **Scientific Reality:** A supercritical fluid is **not** a mixture of liquid and gas simultaneously. Beyond the critical temperature ($T_c = 31.04^\circ\text{C}$) and critical pressure ($P_c = 7.38\text{ MPa}$), the phase boundary between liquid and vapor vanishes entirely. It is a single, homogeneous thermodynamic phase possessing gas-like diffusivity and low viscosity combined with liquid-like density and solvation power.
- **Mandatory Action:** Accurately define supercritical fluid thermodynamics using IUPAC definitions.

### 3.2 Formic Acid vs Formate Speciation
- **Manuscript Text (Section 5.3, Pages 10–11):** Treats formic acid and formate interchangeably without discussing pH speciation or downstream product separation.
- **Scientific Reality:**  
  - Formic acid has a $\text{p}K_a$ of 3.75.
  - At neutral or alkaline cathode conditions (e.g., in $\text{KHCO}_3$ or $\text{KOH}$ electrolytes), the reduction yields formate anions ($\text{HCOO}^-$) neutralized by electrolyte cations ($\text{K}^+$), yielding dilute potassium formate ($\text{HCOOK}$).
  - Converting $\text{HCOOK}$ to pure market-grade formic acid ($\text{HCOOH}$) requires acidification with mineral acids (generating stoichiometric sulfate waste) or energy-intensive bipolar membrane electrodialysis.
  - Only recent advances using solid-electrolyte flow cells (porous solid ion-exchange resins between cathode and anode) can produce concentrated, pure liquid $\text{HCOOH}$ directly without salt byproducts.
- **Mandatory Action:** Explicitly differentiate molecular formic acid from formate salts; evaluate downstream separation energetics.

---

## 4. Methodological & Bibliographic Shortcomings

### 4.1 Lack of a Reproducible Search Methodology
- **Current Defect:** Section 2 ("Material and Methods") consists of 7 lines lacking databases, boolean queries, inclusion/exclusion thresholds, or document counts.
- **Required Fix:** Establish a PRISMA-compliant literature review protocol with pathway-specific search queries across OpenAlex, Crossref, and PubMed.

### 4.2 Severe Author Self-Citation Skew & Peripheral Scope Drift
- **Current Defect:** 11 of 48 references (~23%) are self-citations to a single author (D.K. Sharma), heavily emphasizing non-CCU topics such as:
  - Coal organo-refining (Dhawan et al., 2020)
  - Coal chemical/bio-leaching and desulfurization (Dhawan & Sharma, 2019; Sharma, 2023)
  - Copper and uranium bacterial metallurgy (Section 9, Page 16)
  - Fruit waste fermentation to bioethanol (Jahid et al., 2018)
- **Scientific Assessment:** Coal mining, fruit fermentation, and uranium extraction are completely out of scope for a review on carbon dioxide utilisation. They dilute the scientific authority and focus of the review.
- **Required Fix:** Remove off-topic coal leaching and fruit fermentation discussions; replace with verified high-impact 2020–2025 CCU literature.

### 4.3 Search-and-Replace Corruptions
- **Manuscript Text (Reference 29, Page 24):** Cites *"BotryocoCCSU braunii"*.
- **Cause:** Global text replacement of "cc" or "CC" with "CCSU" corrupted the scientific name of the microalgae *Botryococcus braunii*.
- **Required Fix:** Revert and clean all taxonomic designations.

### 4.4 Inaccurate Historical & Commercial Milestones
- **Manuscript Text (Page 3, Line 74):** Cites Climeworks' *"Icelandic Mammoth DAC (launched in 2026, capturing 36,000 tonnes/year)"*.
- **Reality:** Climeworks' Mammoth commercial DAC plant was officially inaugurated in **May 2024** in Hellisheiði, Iceland. (Naming 2026 was speculative based on older press releases).
- **Required Fix:** Correct commercial operational dates to 2024.

### 4.5 Numerical Discrepancies in Economic Data
- **Manuscript Text:**
  - Page 3: Global CO₂ utilisation market is USD 4.57 billion in 2024, reaching USD 11.15 billion in 2032.
  - Page 20: "...market will reach USD 6.45 million and reach USD 20.4 billion at a CAGR of 13.5 by 2035".
- **Identified Defect:** "USD 6.45 million" in 2026 is an egregious unit transcription error (should be billion). Furthermore, the disparate market sources (IEA, Wood Mackenzie, WEF) are cited without defining functional scopes.
- **Required Fix:** Correct units to USD 6.45 billion; clearly define product scopes.

---

## Conclusion of Phase 0 Audit
The identified errors require a comprehensive, evidence-based overhaul. The subsequent phases will build the traceable literature database, verify chemical reactions and mechanisms, and establish a rigorous, publishable framework for the revised review.
