# Rebuilt Publication Figure Plans: Conceptual Specifications & Diagram Code

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
