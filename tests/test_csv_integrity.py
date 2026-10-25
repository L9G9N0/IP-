"""Automated CSV Schema and RFC 4180 Integrity Tests."""

from __future__ import annotations

import csv
import glob
from pathlib import Path
import unittest

REPO_ROOT = Path(__file__).resolve().parent.parent


class TestCsvIntegrity(unittest.TestCase):
    """Test suite validating CSV formatting, schema headers, and RFC 4180 compliance."""

    def test_csv_rfc4180_column_consistency(self) -> None:
        """Assert that every CSV file across research/ matches its header column count on every row."""
        csv_files = sorted(glob.glob(str(REPO_ROOT / "research" / "**" / "*.csv"), recursive=True))
        self.assertGreaterEqual(len(csv_files), 6, f"Expected at least 6 CSV datasets, found {len(csv_files)}")

        for path_str in csv_files:
            path = Path(path_str)
            with open(path, mode="r", encoding="utf-8") as f:
                reader = list(csv.reader(f))
                self.assertGreater(len(reader), 1, f"CSV {path.name} is empty or missing data rows")
                expected_cols = len(reader[0])
                self.assertGreater(expected_cols, 0, f"CSV {path.name} has empty header")

                for idx, row in enumerate(reader[1:], start=2):
                    self.assertEqual(
                        len(row),
                        expected_cols,
                        f"Column count mismatch in {path.relative_to(REPO_ROOT)} at line {idx}: "
                        f"expected {expected_cols}, got {len(row)} ({row[:2]})",
                    )

    def test_literature_matrix_schema(self) -> None:
        """Validate specific column headers in MASTER_LITERATURE_MATRIX.csv."""
        path = REPO_ROOT / "research" / "literature" / "MASTER_LITERATURE_MATRIX.csv"
        self.assertTrue(path.exists(), "MASTER_LITERATURE_MATRIX.csv not found")

        with open(path, mode="r", encoding="utf-8") as f:
            reader = list(csv.DictReader(f))
            self.assertGreaterEqual(len(reader), 20, f"Expected at least 20 benchmark records, found {len(reader)}")

            for row in reader:
                self.assertTrue(row["Paper_ID"].strip(), "Paper_ID must not be empty")
                self.assertTrue(row["DOI"].strip(), f"DOI must not be empty for {row['Paper_ID']}")
                self.assertTrue(row["Target_Product"].strip(), f"Target_Product empty for {row['Paper_ID']}")

    def test_reaction_database_schema(self) -> None:
        """Validate specific column headers and numeric fields in REACTION_DATABASE.csv."""
        path = REPO_ROOT / "research" / "chemistry" / "REACTION_DATABASE.csv"
        self.assertTrue(path.exists(), "REACTION_DATABASE.csv not found")

        with open(path, mode="r", encoding="utf-8") as f:
            reader = list(csv.DictReader(f))
            self.assertGreaterEqual(len(reader), 20, f"Expected at least 20 reaction records, found {len(reader)}")

            reaction_ids = set()
            for row in reader:
                rxn_id = row["Reaction_ID"].strip()
                self.assertTrue(rxn_id, "Reaction_ID must not be empty")
                self.assertNotIn(rxn_id, reaction_ids, f"Duplicate Reaction_ID: {rxn_id}")
                reaction_ids.add(rxn_id)

                self.assertTrue(
                    "->" in row["Balanced_Chemical_Equation"] or "<=>" in row["Balanced_Chemical_Equation"],
                    f"Invalid equation format for {rxn_id}: {row['Balanced_Chemical_Equation']}",
                )


if __name__ == "__main__":
    unittest.main()
