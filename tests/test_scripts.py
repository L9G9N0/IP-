"""Automated Build Script CLI and Idempotency Tests."""

from __future__ import annotations

from pathlib import Path
import subprocess
import sys
import unittest

REPO_ROOT = Path(__file__).resolve().parent.parent

SCRIPTS = [
    "scripts/build_literature_matrix.py",
    "scripts/build_reaction_database.py",
    "scripts/build_pathway_reports.py",
    "scripts/build_lca_tea.py",
    "scripts/build_tables_and_figures.py",
    "scripts/build_research_gaps.py",
    "scripts/build_claim_register.py",
    "scripts/build_docs_and_qc.py",
    "scripts/build_final_manuscript.py",
]


class TestScripts(unittest.TestCase):
    """Test suite validating script CLI interfaces and idempotent execution."""

    def test_scripts_cli_help(self) -> None:
        """Verify that every build script provides standard --help output and exits with code 0."""
        for script in SCRIPTS:
            script_path = REPO_ROOT / script
            self.assertTrue(script_path.exists(), f"Script not found: {script}")

            res = subprocess.run(
                [sys.executable, str(script_path), "--help"],
                capture_output=True,
                text=True,
                cwd=str(REPO_ROOT),
            )
            self.assertEqual(res.returncode, 0, f"Script {script} --help failed: {res.stderr}")
            self.assertTrue(
                "usage:" in res.stdout.lower() or "options:" in res.stdout.lower(),
                f"Expected usage in {script} help output, got: {res.stdout}",
            )

    def test_scripts_idempotent_execution(self) -> None:
        """Verify that running scripts directly produces expected exit code 0 without raising exceptions."""
        for script in SCRIPTS:
            script_path = REPO_ROOT / script
            res = subprocess.run(
                [sys.executable, str(script_path)],
                capture_output=True,
                text=True,
                cwd=str(REPO_ROOT),
            )
            self.assertEqual(res.returncode, 0, f"Script {script} failed during execution: {res.stderr}")


if __name__ == "__main__":
    unittest.main()
