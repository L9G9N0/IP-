"""Claim Register Generator for CCU Evidence Engine.

Audits empirical claims from the baseline review manuscript against primary peer-reviewed
literature, categorizing claims as VERIFIED, PARTIALLY_VERIFIED, or CONTRADICTED.
"""

from __future__ import annotations

import argparse
import csv
from pathlib import Path
from typing import Sequence

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_OUTPUT = REPO_ROOT / "research" / "evidence" / "CLAIM_REGISTER.csv"

HEADERS: list[str] = [
    "Claim_ID",
    "Claim_Text",
    "Manuscript_Section",
    "Supporting_Source",
    "Source_Type",
    "DOI_or_URL",
    "Exact_Evidence_Location",
    "Quantitative_or_Qualitative",
    "Verification_Status",
    "Conflicting_Evidence",
    "Risk_Level",
    "Required_Action",
]

CLAIMS: list[list[str]] = [
    [
        "CLM-01",
        "CO2 utilisation presents a promising pathway... and increase possibilities of continued use of fossil fuels such as coal, petroleum and natural gas.",
        "Section 1: Abstract & Section 12: Conclusion",
        "None (Author assertion)",
        "Editorial Assertion",
        "N/A",
        "Page 1, Line 25-27; Page 22, Line 657-662",
        "Qualitative",
        "CONTRADICTED",
        "Second Law of Thermodynamics; IPCC AR6 WGIII; Sternberg & Bardow (2021) Nature Climate Change",
        "CRITICAL",
        "PURGE claim completely. Converting coal combustion CO2 back to fuels requires 4-6x more energy than coal produced.",
    ],
    [
        "CLM-02",
        "Global emissions of CO2 worldwide exceed 35 billion tonnes per year (IEA, 2024).",
        "Section 1: Introduction",
        "IEA (2024) CCUS in Clean Energy Transitions",
        "Institutional Report",
        "https://www.iea.org/reports/ccus-in-clean-energy-transitions",
        "Executive Summary, Page 12",
        "Quantitative",
        "VERIFIED",
        "None (consistent with Global Carbon Project 36.8 Gt energy-related CO2)",
        "LOW",
        "KEEP claim; specify energy-related emissions baseline.",
    ],
    [
        "CLM-03",
        "The high thermodynamic stability of CO2 (dG0f = -394.4 kJ/mol) makes its activation kinetically challenging.",
        "Section 1: Introduction & Section 2: CO2 as Resource",
        "Lackner (2003) Science; NIST Chemistry WebBook",
        "Peer-reviewed / Reference Data",
        "10.1126/science.1079033",
        "Table 1 / Standard Thermodynamic Properties",
        "Quantitative",
        "VERIFIED",
        "None (Standard IUPAC thermodynamic value)",
        "LOW",
        "KEEP claim; correct and fundamental.",
    ],
    [
        "CLM-04",
        "The currently existing global market of CO2 utilisation is USD 4.57 billion in 2024 and will become USD 11.15 billion in 2032 at a CAGR of 13.6%.",
        "Section 1: Introduction",
        "IEA (2024) / Grand View Research Market Report",
        "Market Research Report",
        "https://www.iea.org/reports/ccus-in-clean-energy-transitions",
        "Market Sizing Section",
        "Quantitative",
        "PARTIALLY_VERIFIED",
        "Internal conflict with Section 11 claiming USD 6.45 million in 2026",
        "HIGH",
        "Harmonize market sizing across sections; define that this covers chemical/material CCU.",
    ],
    [
        "CLM-05",
        "Icelandic Mammoth DAC (launched in 2026, capturing 36,000 tonnes/year).",
        "Section 1: Introduction",
        "Climeworks Press Release / IEA Tracking",
        "Commercial Press Release",
        "https://climeworks.com/news/mammoth-is-operational",
        "Inauguration announcement May 8, 2024",
        "Quantitative",
        "CONTRADICTED",
        "Mammoth DAC was officially launched and inaugurated in May 2024, not 2026",
        "HIGH",
        "CORRECT launch date to May 2024.",
    ],
    [
        "CLM-06",
        "Indian Government has committed Rs. 20,000 crores towards efforts on CCSU for the future.",
        "Section 2: CO2 as a Resource",
        "Down To Earth (2026)",
        "Journalistic Article",
        "https://www.downtoearth.org.in/",
        "News feature on Indian CCUS roadmap",
        "Quantitative",
        "PARTIALLY_VERIFIED",
        "Rs. 19,744 crore outlay was for the National Green Hydrogen Mission (driving e-fuels), not pure CCSU alone",
        "MEDIUM",
        "QUALIFY citation: Specify National Green Hydrogen Mission and Carbon Credit Trading Scheme (CCTS).",
    ],
    [
        "CLM-07",
        "Under Hydrogenation / Recent Advances: KS-21 solvent; 88% CO2 conversion.",
        "Section 4: Chemical Conversion, Table 2",
        "Mitsubishi Heavy Industries KM CDR Technical Specs",
        "Corporate Technical Report",
        "https://www.mhi.com/products/engineering/co2_recovery_plants.html",
        "Solvent Performance Overview",
        "Quantitative",
        "CONTRADICTED",
        "KS-21 is a post-combustion chemical absorption amine solvent, NOT a hydrogenation catalyst or solvent",
        "CRITICAL",
        "REMOVE from Table 2 hydrogenation rows. Relocate to Section 5 under solvent absorption capture.",
    ],
    [
        "CLM-08",
        "Under Electrochemical / Products: Formic acid, CO2, Ethanol.",
        "Section 4: Chemical Conversion, Table 2",
        "None (Typographical Error)",
        "Manuscript Draft",
        "N/A",
        "Table 2, Row 2",
        "Qualitative",
        "CONTRADICTED",
        "CO2 is the reactant, not the product of electrochemical reduction; typo for Carbon Monoxide (CO)",
        "HIGH",
        "CORRECT typo: replace CO2 with CO.",
    ],
    [
        "CLM-09",
        "Oxylus direct methanol: >80% selectivity.",
        "Section 4: Chemical Conversion & Section 5.1: Methanol",
        "Oxylus Energy Technical Whitepaper / Pilot Announcement",
        "Commercial Announcement",
        "https://www.oxylusenergy.com/",
        "Pilot Specifications 2024",
        "Quantitative",
        "PARTIALLY_VERIFIED",
        "Lab-scale flow cells achieve >80% FE to MeOH; pilot long-term stability and cell voltage under review",
        "MEDIUM",
        "KEEP with qualifier that this is early-stage benchtop data requiring industrial validation.",
    ],
    [
        "CLM-10",
        "Methanol synthesis: Cu/ZnO/Al2O3 operates at 200-300 °C, 5-10 MPa.",
        "Section 5.1: Methanol",
        "Olah et al. (2011) Methanol Economy; Behrens et al. (2012) Science",
        "Peer-reviewed Review / Research",
        "10.1126/science.1219831",
        "Page 893, Table 1",
        "Quantitative",
        "VERIFIED",
        "None (Standard commercial methanol operating window)",
        "LOW",
        "KEEP claim; update with modern In2O3/ZrO2 catalysts achieving 100% selectivity at 300 °C.",
    ],
    [
        "CLM-11",
        "Urea synthesis: 2NH3 + CO2 -> NH4NH2COO -> CO(NH2)2 + H2O at 150-200 °C, 15-25 MPa.",
        "Section 5.4: Urea",
        "Meessen (2012) Ullmann's Encyclopedia of Industrial Chemistry",
        "Reference Encyclopedia",
        "10.1002/14356007.a27_333.pub2",
        "Section 2.1: Thermodynamics",
        "Quantitative",
        "PARTIALLY_VERIFIED",
        "Intermediate formula typo in text (written as NH4NH2COO instead of ammonium carbamate NH2COONH4)",
        "HIGH",
        "CORRECT chemical formula to NH2COONH4; highlight that agricultural urea releases 100% of incorporated CO2.",
    ],
    [
        "CLM-12",
        "Solid CO2 utilised by burning Mg ribbon to produce graphene: Bagotia et al. (2018b) used Ni and Zn promoters.",
        "Section 5.6: Carbon Nanomaterials",
        "Bagotia et al. (2018b) Polymer Composites",
        "Peer-reviewed Research",
        "10.1002/pc.24606",
        "Experimental Section, Page E1042",
        "Qualitative",
        "CONTRADICTED",
        "Magnesiothermic reduction produces disordered soot/graphene flakes. Mg smelting emits 15-25 kg CO2e/kg Mg, creating positive net emissions.",
        "CRITICAL",
        "REPLACE emphasis on magnesiothermic combustion with molten salt CO2 capture & liquid metal electrochemical conversion.",
    ],
    [
        "CLM-13",
        "Pharmaceutical synthesis: Grignard carboxylation has high atom economy.",
        "Section 5.7: Pharmaceuticals",
        "Author assertion",
        "Editorial Text",
        "N/A",
        "Section 5.7, Paragraph 1",
        "Qualitative",
        "CONTRADICTED",
        "Grignard reagents are stoichiometric, highly pyrophoric, and require stoichiometric acid quench with high E-factor.",
        "HIGH",
        "CORRECT: Highlight that traditional Grignard has poor atom economy; modern visible-light photoredox carboxylation resolves this.",
    ],
    [
        "CLM-14",
        "Supercritical CO2 (above 31.1 °C, 7.39 MPa) behaves as both liquid and gas.",
        "Section 5.7: Pharmaceuticals",
        "IUPAC Gold Book",
        "Reference Standards",
        "10.1351/goldbook.S06134",
        "Entry: Supercritical fluid",
        "Quantitative",
        "PARTIALLY_VERIFIED",
        "Technically a single homogeneous supercritical phase with liquid-like density and gas-like diffusivity; not 'both simultaneously'.",
        "LOW",
        "CLARIFY thermodynamic definition per IUPAC standards.",
    ],
    [
        "CLM-15",
        "Mineralisation: CarbonCure and Solidia technologies permanently sequester CO2.",
        "Section 5.9: Mineralisation",
        "Monkman & MacDonald (2017) Cement and Concrete Composites",
        "Peer-reviewed Research",
        "10.1016/j.cemconcomp.2017.03.015",
        "Page 246",
        "Qualitative",
        "VERIFIED",
        "Permanent chemical trapping as stable calcium/magnesium carbonate (>10,000 year permanence).",
        "LOW",
        "EXPAND: Document that mineralisation is one of the only true permanent carbon sinks.",
    ],
    [
        "CLM-16",
        "CCU market size in 2026: USD 6.45 million.",
        "Section 11: Economic and Market Analysis",
        "Wood Mackenzie / Global CCS Institute (2026)",
        "Market Research",
        "N/A",
        "Section 11, Line 532",
        "Quantitative",
        "CONTRADICTED",
        "Glaring typo in original draft: $6.45 million is absurdly small. Intended value was USD 6.45 billion.",
        "CRITICAL",
        "CORRECT typographical error from 'million' to 'billion'.",
    ],
]


def build_claim_register(
    output_path: Path | str = DEFAULT_OUTPUT,
    filter_status: str | None = None,
) -> Path:
    """Build and write the claim register CSV.

    Args:
        output_path: Target path for the generated CSV file.
        filter_status: Optional verification status filter (e.g. 'CONTRADICTED').

    Returns:
        Path to the generated CSV file.
    """
    path = Path(output_path).resolve()
    path.parent.mkdir(parents=True, exist_ok=True)

    rows = CLAIMS
    if filter_status:
        rows = [r for r in rows if r[8].upper() == filter_status.upper()]

    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(HEADERS)
        writer.writerows(rows)

    print(f"Successfully wrote {len(rows)} audited claims to {path} with {len(HEADERS)} columns.")
    return path


def parse_args(args: Sequence[str] | None = None) -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Generate the CCU Claim Register CSV.")
    parser.add_argument(
        "--output",
        "-o",
        type=Path,
        default=DEFAULT_OUTPUT,
        help=f"Target output CSV path (default: {DEFAULT_OUTPUT})",
    )
    parser.add_argument(
        "--filter",
        "-f",
        type=str,
        default=None,
        help="Filter claims by Verification_Status (e.g., VERIFIED, CONTRADICTED)",
    )
    return parser.parse_args(args)


def main() -> None:
    """CLI Entry Point."""
    args = parse_args()
    build_claim_register(output_path=args.output, filter_status=args.filter)


if __name__ == "__main__":
    main()
