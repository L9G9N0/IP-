# Scientific Metric Normalisation Guide: Quantitative Standards for CCU Evaluation

**Document:** `research/evidence/METRIC_NORMALIZATION.md`  
**Execution Date:** October 2026  
**Purpose:** Establish standardized mathematical definitions, calculation boundaries, units, and comparability rules across thermocatalytic, electrochemical, biological, and mineral carbonation pathways.

> [!CAUTION]
> **Cardinal Metric Comparability Rule:**  
> **Never compare Faradaic Efficiency (FE) directly with Single-Pass Thermal Conversion or Yield.**  
> - **Faradaic efficiency** measures the selectivity of electron transfer in an electrochemical circuit. An electrolyzer can operate at 95% FE while only converting 10% of the input $\text{CO}_2$ per pass.  
> - **Single-pass thermal conversion** measures the fraction of $\text{CO}_2$ molecules transformed across a catalyst bed in one transit.  
> Conflating these two metrics is a severe scientific error that distorts technology readiness comparisons.

---

## 1. Primary Performance Metrics & Mathematical Definitions

### 1.1 $\text{CO}_2$ Conversion ($X_{\text{CO}_2}$)

#### A. Single-Pass Conversion ($X_{\text{SP}}$)
- **Definition:** The molar percentage of carbon dioxide converted into all reaction products during a single transit through the reactor.
- **Formula:**
  $$X_{\text{SP}} = \frac{F_{\text{CO}_2,\text{in}} - F_{\text{CO}_2,\text{out}}}{F_{\text{CO}_2,\text{in}}} \times 100\%$$
  where $F_{\text{CO}_2,\text{in}}$ and $F_{\text{CO}_2,\text{out}}$ are the inlet and outlet molar flow rates of $\text{CO}_2$.
- **Unit:** Percentage ($\%$)
- **Context & Bounds:** In thermocatalytic methanol synthesis and DRM, $X_{\text{SP}}$ is constrained by chemical equilibrium (typically 8–20% for methanol at 250°C/50 bar). In electrochemical flow cells, $X_{\text{SP}}$ is typically 15–35% due to gas-liquid boundary layer mass transfer limits.

#### B. Overall / Plant Conversion ($X_{\text{overall}}$)
- **Definition:** The fraction of fresh $\text{CO}_2$ feedstock converted across the entire plant loop, including unreacted gas recycling.
- **Formula:**
  $$X_{\text{overall}} = \frac{F_{\text{CO}_2,\text{fresh}} - F_{\text{CO}_2,\text{purge}}}{F_{\text{CO}_2,\text{fresh}}} \times 100\%$$
- **Unit:** Percentage ($\%$)
- **Context:** Commercial plants achieve $>95–98\%$ overall conversion by recycling unreacted $\text{CO}_2$ and $\text{H}_2$ with a small purge stream to prevent inert gas buildup.

---

### 1.2 Product Selectivity ($S_i$)

- **Definition:** The molar fraction of converted $\text{CO}_2$ that appears in target product $i$, normalized by carbon stoichiometry.
- **Formula:**
  $$S_i = \frac{n_i \cdot F_{i,\text{out}}}{\sum_j \left(n_j \cdot F_{j,\text{out}}\right)} \times 100\% = \frac{n_i \cdot F_{i,\text{out}}}{F_{\text{CO}_2,\text{in}} - F_{\text{CO}_2,\text{out}}} \times 100\%$$
  where $n_i$ is the number of carbon atoms in target molecule $i$ (e.g., $n=1$ for $\text{CH}_3\text{OH}$, $n=2$ for $\text{C}_2\text{H}_4$).
- **Unit:** Percentage ($\%$)
- **Distinction:** Selectivity is strictly defined relative to *converted carbon*, not total feed carbon. A catalyst can have 99% selectivity to methanol at 5% conversion.

---

### 1.3 Product Yield ($Y_i$)

- **Definition:** The total fraction of fed $\text{CO}_2$ transformed into target product $i$.
- **Formula:**
  $$Y_i = \frac{X_{\text{CO}_2} \times S_i}{100\%} = \frac{n_i \cdot F_{i,\text{out}}}{F_{\text{CO}_2,\text{in}}} \times 100\%$$
- **Unit:** Percentage ($\%$)
- **Validation Rule:** By mass conservation, $Y_i \le X_{\text{CO}_2}$ and $Y_i \le S_i$ always.

---

### 1.4 Faradaic Efficiency ($\text{FE}_i$)

- **Definition:** The fraction of total electrical charge (electrons) passed through an electrochemical cell that is consumed to synthesize target product $i$.
- **Formula:**
  $$\text{FE}_i = \frac{z_i \cdot n_i \cdot F}{Q} \times 100\% = \frac{z_i \cdot \dot{n}_i \cdot F}{I} \times 100\%$$
  where:
  - $z_i$ = number of electrons required per molecule of product $i$ ($z=2$ for $\text{CO}$ and $\text{HCOOH}$; $z=8$ for $\text{CH}_4$; $z=12$ for $\text{C}_2\text{H}_4$ and $\text{C}_2\text{H}_5\text{OH}$).
  - $\dot{n}_i$ = molar production rate ($\text{mol/s}$).
  - $F$ = Faraday constant ($96,485\text{ C/mol } e^-$).
  - $I$ = total measured electric current ($\text{A}$).
  - $Q$ = total integrated charge ($\text{C}$).
- **Unit:** Percentage ($\%$)
- **Significance:** Measures electrical selectivity. Does **not** indicate single-pass $\text{CO}_2$ conversion, cell voltage, or overall energy efficiency.

---

### 1.5 Current Density ($j$) & Partial Current Density ($j_i$)

- **Definition:** Total electric current normalized by geometric electrode surface area ($j$), and the specific portion driving product $i$ ($j_i$).
- **Formula:**
  $$j = \frac{I}{A_\text{geometric}} \quad (\text{mA/cm}^2 \text{ or } \text{A/cm}^2)$$
  $$j_i = j \times \frac{\text{FE}_i}{100\%}$$
- **Industrial Threshold:** Commercial viability requires $j_i \ge 200–300\text{ mA/cm}^2$ (to limit stack capital costs).

---

### 1.6 Electrochemical Energy Efficiency ($\text{EE}_\text{cell}$)

- **Definition:** The ratio of chemical energy stored in the product to the total electrical energy consumed by the electrolyzer.
- **Formula:**
  $$\text{EE}_{\text{cell},i} = \frac{E^\circ_i}{V_\text{cell}} \times \text{FE}_i$$
  where $E^\circ_i$ is the thermodynamic equilibrium cell voltage under standard conditions, and $V_\text{cell}$ is the actual operating cell voltage (including overpotentials and ohmic losses).
- **Unit:** Percentage ($\%$)
- **Context:** An electrolyzer operating at $\text{FE} = 90\%$ but requiring $V_\text{cell} = 3.5\text{ V}$ for a reaction with $E^\circ = 1.2\text{ V}$ has a real energy efficiency of only:
  $$\text{EE}_\text{cell} = \frac{1.2}{3.5} \times 90\% = 30.8\%$$

---

### 1.7 Solar-to-Chemical Efficiency ($\text{STC}$) & Apparent Quantum Yield ($\text{AQY}$)

- **Apparent Quantum Yield (Photocatalysis):**
  $$\text{AQY} = \frac{z \cdot \text{moles of product formed}}{\text{moles of incident photons}} \times 100\%$$
- **Solar-to-Chemical Efficiency (STC):**
  $$\text{STC} = \frac{\sum_i \left(r_i \cdot \Delta G^\circ_i\right)}{P_\text{solar} \cdot A_\text{illum}} \times 100\%$$
  where $r_i$ is the production rate ($\text{mol/s}$), $\Delta G^\circ_i$ is Gibbs free energy ($\text{J/mol}$), and $P_\text{solar} \cdot A_\text{illum}$ is incident radiant solar power ($\text{W}$).
- **Benchmark:** Most lab reports boast high $\text{AQY}$ at UV wavelengths, but $\text{STC}$ under full-spectrum sunlight remains $<0.2\%$ for pure water systems (commercial threshold $>10\%$).

---

### 1.8 Carbon Efficiency & Carbon Crossover

- **Definition:** The fraction of inlet $\text{CO}_2$ carbon atoms successfully converted into products vs. lost to unreacted emissions, side products, or carbonate crossover.
- **Electrochemical Carbonate Crossover Loss:**
  $$\eta_\text{C,crossover} = \frac{\text{Moles of }\text{CO}_2\text{ reacted with }\text{OH}^-\text{ to form }\text{CO}_3^{2-}}{\text{Total inlet }\text{CO}_2} \times 100\%$$
  In alkaline cells, up to 2 moles of $\text{CO}_2$ are lost as $\text{CO}_3^{2-}$ for every 1 mole of $\text{CO}$ produced, cutting carbon efficiency to $<33\%$.

---

### 1.9 Catalyst Productivity: STY, TON, and TOF

| Metric | Full Name | Definition | Unit | Application |
|---|---|---|---|---|
| **STY** | Space-Time Yield | Mass or moles of target product produced per unit catalyst mass (or reactor volume) per unit time | $\text{g}/(\text{g}_\text{cat}\cdot\text{h})$ or $\text{kg}/(\text{m}^3\cdot\text{h})$ | Reactor sizing & CAPEX |
| **TON** | Turnover Number | Total molecules of product generated per active site over catalyst lifetime before deactivation | Dimensionless | Catalyst economic lifetime |
| **TOF** | Turnover Frequency | Molecules of product generated per active catalytic site per unit time | $\text{s}^{-1}$ or $\text{h}^{-1}$ | Intrinsic kinetic activity |

---

### 1.10 Life-Cycle Avoided Emissions ($\Delta E_\text{net}$)

- **Definition:** Net greenhouse gas emissions avoided by substituting conventional fossil production with a CCU pathway, evaluated across identical system boundaries.
- **Formula:**
  $$\Delta E_\text{net} = E_\text{conventional,cradle-to-grave} - E_{\text{CCU},\text{cradle-to-grave}}$$
- **Rule:** $\Delta E_\text{net} > 0$ denotes genuine climate mitigation. If $\Delta E_\text{net} \le 0$, the CCU process increases net atmospheric carbon emissions despite utilizing $\text{CO}_2$ as a feedstock.

---

## 2. Standardized Cross-Pathway Normalisation Matrix

| Parameter / Metric | Thermocatalytic Hydrogenation | Electrochemical Reduction | Mineral Carbonation | Copolymerization (ROCOP) | Microbial Electrosynthesis |
|---|---|---|---|---|---|
| **Primary Selectivity Metric** | Carbon Selectivity ($S_i, \%$) | Faradaic Efficiency ($\text{FE}_i, \%$) | Mineral Selectivity ($100\%$) | Carbonate Linkage ($>99\%$) | Metabolic Selectivity ($S_\text{acetate}, \%$) |
| **Primary Rate Metric** | Space-Time Yield ($\text{g/g}_\text{cat}/\text{h}$) | Current Density ($j_i, \text{mA/cm}^2$) | Carbonation Rate ($\text{kg CO}_2/\text{t}/\text{h}$) | TON / TOF ($\text{s}^{-1}$) | Volumetric Rate ($\text{g/L}_\text{reactor}/\text{d}$) |
| **Conversion Basis** | Single-pass $X_\text{SP}$ (8–20%) | Single-pass $X_\text{SP}$ (15–35%) | Mineral conversion ($>90\%$) | Monomer conversion ($>95\%$) | Gas uptake efficiency (65–85%) |
| **Primary Energy Metric** | Thermal efficiency ($\%$) + $\text{MWh/t H}_2$ | Full-cell $\text{EE}_\text{cell} (\%)$ + $\text{kWh/kg}$ | Pumping energy ($\text{MWh/t CO}_2$) | Exothermic polymerization | Cathodic energy efficiency ($\%$) |
| **Permanence Metric** | Days to months (Fuels) | Months to years (Chemicals) | $>10,000$ years (Calcite) | 10–50 years (Polyurethanes) | Days to months (Biochemicals) |
