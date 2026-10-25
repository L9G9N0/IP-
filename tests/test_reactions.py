"""Automated Chemical Stoichiometry and Thermodynamic Tests."""

from __future__ import annotations

import csv
from pathlib import Path
import unittest

REPO_ROOT = Path(__file__).resolve().parent.parent


class TestReactions(unittest.TestCase):
    """Test suite validating chemical reaction equations and thermodynamics."""

    def test_reaction_thermodynamic_sanity(self) -> None:
        """Validate that reaction thermodynamic values are parseable floats and match sanity bounds."""
        path = REPO_ROOT / "research" / "chemistry" / "REACTION_DATABASE.csv"
        self.assertTrue(path.exists(), "REACTION_DATABASE.csv not found")

        with open(path, mode="r", encoding="utf-8") as f:
            reader = list(csv.DictReader(f))

            for row in reader:
                rxn_id = row["Reaction_ID"]
                dh0_str = row["Thermodynamic_Enthalpy_dH0_kJ_mol"].strip()
                dg0_str = row["Thermodynamic_Gibbs_dG0_kJ_mol"].strip()

                try:
                    dh0 = float(dh0_str)
                    dg0 = float(dg0_str)
                except ValueError as e:
                    self.fail(f"Non-numeric thermodynamic constant in {rxn_id}: {e}")

                # Physical sanity check: reaction enthalpies are generally between -2000 and +2000 kJ/mol
                self.assertTrue(-2000.0 <= dh0 <= 2000.0, f"Unrealistic dH0 in {rxn_id}: {dh0} kJ/mol")
                self.assertTrue(-2000.0 <= dg0 <= 2000.0, f"Unrealistic dG0 in {rxn_id}: {dg0} kJ/mol")

    def test_cross_pathway_table_sanity(self) -> None:
        """Validate that cross-pathway matrix contains all 13 recognized technological pathways."""
        path = REPO_ROOT / "research" / "tables" / "CROSS_PATHWAY_TABLE.csv"
        self.assertTrue(path.exists(), "CROSS_PATHWAY_TABLE.csv not found")

        with open(path, mode="r", encoding="utf-8") as f:
            reader = list(csv.DictReader(f))
            self.assertEqual(len(reader), 13, f"Expected exactly 13 pathways in CROSS_PATHWAY_TABLE.csv, found {len(reader)}")

            pathway_ids = [row["Pathway_ID"] for row in reader]
            expected_ids = [f"P{i:02d}" for i in range(1, 14)]
            self.assertEqual(pathway_ids, expected_ids, f"Pathway ID mismatch: expected {expected_ids}, got {pathway_ids}")


if __name__ == "__main__":
    unittest.main()
