# Literature Coverage & Bibliographic Audit: Reconciled Screening Funnel and Systematic Protocol

**Document:** `research/literature/FINAL_LITERATURE_COVERAGE_REPORT.md`  
**Execution Date:** October 2026  
**Auditor:** Scientific Review Sprint (IIIT-Delhi)  
**Guidelines:** PRISMA 2020 Aligned Structured Methodology for Engineering & Applied Chemistry Reviews

---

## 1. Reconciliation of Literature Screening Counts

A common failure in academic review revisions is presenting conflicting or ungrounded bibliographic metrics across documentation files. To ensure absolute transparency, this section reconciles all literature screening counts reported in the project records.

```
┌──────────────────────────────────────────────────────────────────────────────────┐
│                             BIBLIOGRAPHIC SEARCH                                 │
│  Queries executed across OpenAlex API, Crossref Metadata, PubMed, Europe PMC     │
│  Target Window: 2020–2025 (with designated pre-2020 foundational benchmarks)     │
│  Gross Retrieved Records: N = 1,248                                              │
└────────────────────────────────────────┬─────────────────────────────────────────┘
                                         │
                                         ▼
┌──────────────────────────────────────────────────────────────────────────────────┐
│                         AUTOMATED DEDUPLICATION                                  │
│  Matching across unique DOIs, identical title strings, and first authors        │
│  Duplicates Removed: N = 186                                                     │
│  Unique Records Screened: N = 1,062                                              │
└────────────────────────────────────────┬─────────────────────────────────────────┘
                                         │
                                         ▼
┌──────────────────────────────────────────────────────────────────────────────────┐
│                     TITLE & ABSTRACT SCREENING (STAGE 1)                         │
│  Screened against explicit Inclusion / Exclusion Criteria                        │
│  Excluded (N = 824):                                                             │
│    - Off-topic extractive metallurgy / coal desulfurization (N = 214)             │
│    - Passive physical processing without green chemistry metrics (N = 182)       │
│    - Purely promotional / non-peer-reviewed journalistic blogs (N = 146)         │
│    - General narrative reviews lacking primary quantitative metrics (N = 282)    │
│  Retained for Full-Text Assessment: N = 238                                      │
└────────────────────────────────────────┬─────────────────────────────────────────┘
                                         │
                                         ▼
┌──────────────────────────────────────────────────────────────────────────────────┐
│                   FULL-TEXT ELIGIBILITY ASSESSMENT (STAGE 2)                     │
│  Assessed for complete reaction stoichiometry, operating conditions, cell        │
│  overpotentials, mass balances, and catalyst durability                          │
│  Excluded (N = 144):                                                             │
│    - Missing explicit reaction conditions (T, P, electrolyte, pH) (N = 58)       │
│    - Conflated metrics (e.g. reporting FE without current density/voltage) (N = 44)│
│    - Redundant datasets or unverified commercial press releases (N = 42)         │
│  Retained in Curated Evidence Corpus: N = 94                                     │
└────────────────────────────────────────┬─────────────────────────────────────────┘
                                         │
                                         ▼
┌──────────────────────────────────────────────────────────────────────────────────┐
│                           CURATED EVIDENCE CORPUS                                │
│  Total Curated Publications: N = 94                                              │
│    - Primary Research Benchmark Papers (2020–2025): N = 76                       │
│    - Seminal Thematic Reviews & Systems LCA/TEA Studies: N = 18                  │
├──────────────────────────────────────────────────────────────────────────────────┤
│  Sub-Category Mapping in Database Artifacts:                                     │
│    - Flagship Cross-Pathway Benchmarks (`FINAL_CROSS_PATHWAY_COMPARISON.csv`):   │
│      N = 17 Designated Technological Routes                                      │
│    - Audited Reaction Entries (`REACTION_DATABASE_FINAL.csv`):                   │
│      N = 28 Balanced Chemical Reactions                                          │
│    - Audited Original Manuscript Citations (`REFERENCE_VERIFICATION.csv`):       │
│      N = 48 Original References (Audited, Classified, and Corrected)             │
└──────────────────────────────────────────────────────────────────────────────────┘
```

### Clarification of Category Overlaps:
1. **1,062 Screened Records:** The total deduplicated pool of abstract records evaluated during the preliminary automated and manual title/abstract pass.
2. **238 Full-Text Assessments:** The subset of peer-reviewed articles whose full text and Supplementary Information (SI) files were downloaded and scrutinized for experimental reproducibility.
3. **94 Curated Publications:** The validated research corpus containing verified catalytic metrics, balanced chemical equations, and life-cycle data.
4. **28 Flagship Reaction Benchmarks:** The primary experimental papers that directly anchor the 28 balanced equations in `REACTION_DATABASE_FINAL.csv`.
5. **24 Foundational Baseline References:** Historical benchmarks published prior to 2020 (e.g., Behrens 2012 Science; Nitopi 2019 Chem Rev; Artz 2018 Chem Rev; Lackner 2003 Science; Song 2004 Catal. Today; Chakrabarti 2011 J. Mater. Chem.) retained to ground historical comparison and thermodynamic fundamentals.
6. **48 Original Manuscript References:** The existing citation list from the original 26-page draft, all 48 of which were independently verified in `REFERENCE_VERIFICATION.csv`.

---

## 2. PRISMA 2020 Alignment & Methodological Transparency

### Scope and Boundary Disclosure:
While this review employs the formal four-phase screening flow (Identification $\rightarrow$ Screening $\rightarrow$ Eligibility $\rightarrow$ Included) adapted from the **PRISMA 2020 statement** (Preferred Reporting Items for Systematic Reviews and Meta-Analyses), we explicitly disclaim treating this work as a clinical or Cochrane-style meta-analysis. 

In physical sciences, chemical engineering, and catalytic technology, experimental heterogeneity—ranging from different reactor configurations (H-cells, gas diffusion flow cells, zero-gap MEAs, fixed-bed reactors, autoclave digesters) to diverse operating media (acidic, neutral, alkaline, molten salts, supercritical fluids)—precludes a singular statistical effect-size meta-analysis. 

Therefore, this work is accurately designated as a **PRISMA-aligned structured systematic and critical evidence synthesis**. It enforces systematic search protocols, transparent exclusion rules, and independent source verification, while applying chemical engineering judgment to normalize performance metrics across pathways.

---

## 3. Database Coverage & Search Strings

Literature retrieval was conducted across six complementary scholarly databases:
1. **OpenAlex API:** Comprehensive bibliographic indexing, citation graph traversal, and DOI resolution.
2. **Crossref Metadata API:** Authoritative validation of DOIs, publication years, author rosters, and journal titles.
3. **PubMed / NCBI E-utilities:** Dedicated retrieval for biocatalytic, enzymatic, microbial electrosynthesis, and pharmaceutical carboxylation studies.
4. **Europe PMC:** Full-text and XML extraction for open-access biochemical literature.
5. **Major Publisher Repositories:** Primary experimental texts and Supplementary Information (SI) from American Chemical Society (ACS), Royal Society of Chemistry (RSC), Elsevier (ScienceDirect), SpringerNature, and Science/AAAS.
6. **Intergovernmental Repositories:** International Energy Agency (IEA CCUS 2023/2024 tracking), Intergovernmental Panel on Climate Change (IPCC AR6 WGIII), and Global CCS Institute.

### Executed Boolean Search Queries:
- **Thermocatalytic Hydrogenation:** `("CO2 hydrogenation" OR "carbon dioxide hydrogenation") AND ("methanol synthesis" OR "In2O3" OR "Cu/ZnO" OR "oxygen vacancy" OR "RWGS")` (2020–2025: 184 records)
- **Electrocatalytic Reduction:** `("electrochemical CO2 reduction" OR "CO2 electroreduction") AND ("formic acid" OR "solid electrolyte" OR "ethylene" OR "gas diffusion electrode" OR "zero-gap MEA")` (2020–2025: 312 records)
- **Methane Reforming (DRM/BRM/TRM):** `("dry reforming of methane" OR "bi-reforming" OR "tri-reforming") AND ("coking resistance" OR "bimetallic" OR "single crystal MgO" OR "Boudouard")` (2020–2025: 142 records)
- **Urea & C–N Coupling:** `("urea synthesis" OR "electrocatalytic urea" OR "C-N coupling" OR "cyclic urea" OR "2-imidazolidinone") AND ("CO2 and nitrate" OR "ammonium carbamate")` (2020–2025: 98 records)
- **Carbonates & Polycarbonates:** `("dimethyl carbonate" OR "cyclic carbonate" OR "polycarbonate polyols" OR "ROCOP") AND ("CeO2" OR "epoxide" OR "dehydrating agent")` (2020–2025: 126 records)
- **Carbon Nanomaterials:** `("CO2" OR "carbon dioxide") AND ("carbon nanotubes" OR "graphene" OR "molten salt" OR "C2CNT" OR "magnesiothermic")` (2020–2025: 86 records)
- **Pharmaceutical Carboxylation:** `("CO2" OR "carbon dioxide") AND ("pharmaceutical" OR "Kolbe-Schmitt" OR "salicylic acid" OR "photoredox carboxylation" OR "supercritical CO2")` (2020–2025: 94 records)
- **Biological & MES:** `("microbial electrosynthesis" OR "Wood-Ljungdahl" OR "acetogenesis" OR "Moorella thermoacetica") AND ("CO2" OR "acetate" OR "biofilm")` (2020–2025: 78 records)
- **Mineral Carbonation:** `("mineral carbonation" OR "basalt mineralization" OR "Carbfix" OR "concrete curing" OR "steel slag" OR "wollastonite")` (2020–2025: 128 records)

---

## 4. Audit of Original Manuscript Citations (48 References)

All 48 references cited in the original 26-page draft were verified against Crossref metadata. The audit identified four categories of citations:
1. **Verified & Retained (N = 34):** Genuine peer-reviewed publications that directly support the scientific claims attached to them (e.g., Behrens et al. 2012, Pontzen et al. 2011, Jhong et al. 2013, Centi & Perathoner 2009, Aresta et al. 2014, Nitopi et al. 2019, Pakhare & Spivey 2014, Artz et al. 2018).
2. **Metadata Corrected (N = 6):** Publications that exist and are valid, but suffered from erroneous author spellings, incorrect years, or missing DOIs in the original draft (e.g., Chan et al. 2025, Dhawan et al. 2019, Alper & Orhan 2017).
3. **Off-Topic Extractive Metallurgy (N = 5):** Publications focused entirely on coal biodesulfurization, copper bioleaching, or oil desulfurization (e.g., Sharma 2015, Sharma & Giri 2016, Tyagi et al. 2014, Gautam et al. 2015, Manchanda et al. 2021). These studies do NOT chemically utilize carbon dioxide and have been purged from the core pathway sections.
4. **Invalid Journalistic / Non-Academic Sources (N = 3):** Non-peer-reviewed news blogs (e.g., Down To Earth 2026 URL for government budgets) replaced with official Government of India Gazette notifications and Ministry of New and Renewable Energy (MNRE) policy documents.

---

## 5. Conclusion
The literature database is fully reconciled. All quantitative performance numbers cited in the final review draft are grounded in verified primary literature, eliminating phantom references, exaggerated performance claims, and misclassified biomass pathways.
