# Research Gaps & Unresolved Scientific Challenges in CO₂ Utilisation

**Document:** `research/gaps/RESEARCH_GAPS.md`  
**Execution Date:** October 2026

---

## 1. Cross-Pathway Critical Research Gaps

### Gap 1: The Disconnect Between Catalyst-Level Overpotential and Cell Energy Efficiency
- **Problem:** Literature predominantly reports Faradaic Efficiency (FE) measured in three-electrode H-cells or high-flow alkaline cells. However, in zero-gap membrane electrode assemblies (MEAs) or pure-water stacks required for industrial scale, cell overpotential spikes by 0.8–1.5 V due to membrane resistance, mass transport limits, and bubble resistance.
- **Unresolved Challenge:** Developing catalysts that maintain high selectivity ($>80\%$) at cell voltages $<2.2\text{ V}$ and industrial current densities ($>300\text{ mA/cm}^2$).

### Gap 2: The Parasitic Carbonate Crossover in Electrochemical Systems
- **Problem:** In neutral or alkaline electrolytes, every 1 mole of $\text{CO}_2$ converted generates 1–2 moles of $\text{OH}^-$, which spontaneously reacts with fresh $\text{CO}_2$ to form bicarbonate/carbonate:
  $$\text{CO}_2 + 2\text{OH}^- \rightarrow \text{CO}_3^{2-} + \text{H}_2\text{O}$$
  Up to 70% of inlet $\text{CO}_2$ is lost across the anion exchange membrane, releasing mixed $\text{CO}_2/\text{O}_2$ gas at the anode.
- **Unresolved Challenge:** Operating at high single-pass carbon efficiency ($>60\%$) without costly acid-neutralization cycles or unviable parasitic power penalties.

### Gap 3: Downstream Separation Penalties from Dilute Product Streams
- **Problem:** Many emerging pathways yield highly dilute products:
  - Electrochemical ethanol: $<3\text{ wt%}$ in water.
  - Microbial electrosynthesis: $10–30\text{ g/L}$ acetate.
  - Electrochemical urea: $<50\text{ mM}$ aqueous concentration.
- **Unresolved Challenge:** The thermal distillation or electrodialysis energy required to concentrate dilute liquid products often exceeds the entire chemical energy content of the product itself ($4–8\text{ MJ/kg}$).

### Gap 4: Water-Induced Sintering under Pure CO₂ Hydrogenation Feeds
- **Problem:** Pure $\text{CO}_2$ hydrogenation generates 1 mole of $\text{H}_2\text{O}$ per mole of methanol. Unlike syngas ($\text{CO/CO}_2/\text{H}_2$), pure $\text{CO}_2$ creates high water partial pressure that accelerates Ostwald ripening of $\text{Cu}$ and oxidizes $\text{Zn}$ promoter sites.
- **Unresolved Challenge:** Designing sintering-resistant, hydrophobic, or in-situ membrane water-scavenging reactors that maintain $>5,000\text{ h}$ continuous stability.

### Gap 5: Upstream Embodied Carbon in "Exotic" Reduction Routes
- **Problem:** As demonstrated by our audit of magnesiothermic combustion ($\text{CO}_2 + 2\text{Mg} \rightarrow 2\text{MgO} + \text{C}$), reduction routes requiring metallic reductants ($\text{Mg}, \text{Al}, \text{Na}$) or stoichiometric organometallics (Grignard reagents) consume materials whose upstream smelting emits far more $\text{CO}_2$ than the reaction sequesters.
- **Unresolved Challenge:** Eliminating stoichiometric sacrificial metal reagents in favor of direct electrochemical, photoredox, or green $\text{H}_2$ reduction.
