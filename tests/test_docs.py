"""Automated Documentation Structure and Heading Hierarchy Tests."""

from __future__ import annotations

import glob
from pathlib import Path
import unittest

REPO_ROOT = Path(__file__).resolve().parent.parent

CANONICAL_DOCS = [
    "README.md",
    "LICENSE",
    "CHANGELOG.md",
    "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md",
    "SECURITY.md",
    "SUPPORT.md",
    "ROADMAP.md",
    "ARCHITECTURE.md",
    "API.md",
    "PROJECT_STRUCTURE.md",
    "DEVELOPMENT.md",
    "RELEASE.md",
]

PATHWAY_DOSSIERS = [
    "Biotechnology_and_MES.md",
    "Carbon_Nanomaterials.md",
    "Dry_and_Bi_Reforming.md",
    "Electrochemical_Reduction.md",
    "Integrated_Capture_Conversion.md",
    "Methanol.md",
    "Mineralisation_and_Construction.md",
    "Pharmaceutical_Applications.md",
    "Photocatalytic_Conversion.md",
    "Policy_and_Market_Analysis.md",
    "Polycarbonates_and_DMC.md",
    "Sustainability_LCA_TEA.md",
    "Urea_and_CN_Coupling.md",
]


class TestDocs(unittest.TestCase):
    """Test suite validating documentation completeness and markdown structure."""

    def test_canonical_root_docs_exist(self) -> None:
        """Verify that all enterprise root governance documents exist and are non-empty."""
        for doc in CANONICAL_DOCS:
            path = REPO_ROOT / doc
            self.assertTrue(path.exists(), f"Required root document missing: {doc}")
            self.assertGreater(path.stat().st_size, 50, f"Root document is empty or trivially small: {doc}")

    def test_pathway_dossiers_exist(self) -> None:
        """Verify that all 13 pathway research reports exist in research/pathways/."""
        for dossier in PATHWAY_DOSSIERS:
            path = REPO_ROOT / "research" / "pathways" / dossier
            self.assertTrue(path.exists(), f"Pathway dossier missing: {dossier}")
            self.assertGreater(path.stat().st_size, 500, f"Pathway dossier is suspiciously small: {dossier}")

    def test_markdown_encoding_and_headings(self) -> None:
        """Verify that all markdown documents use UTF-8 and contain valid top-level headers."""
        md_files = glob.glob(str(REPO_ROOT / "**" / "*.md"), recursive=True)

        for md_file in md_files:
            if ".venv" in md_file:
                continue
            path = Path(md_file)
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
                self.assertTrue(content.strip(), f"Markdown file {path.name} is empty")
                lines = content.splitlines()
                top_headers = [l for l in lines if l.startswith("# ")]
                self.assertGreaterEqual(len(top_headers), 1, f"Markdown file {path.name} missing top-level '# ' heading")


if __name__ == "__main__":
    unittest.main()
