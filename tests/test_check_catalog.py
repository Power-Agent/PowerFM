import sys
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from check_catalog import check_catalog


class CatalogLinkChecks(unittest.TestCase):
    def setUp(self):
        self.temp = TemporaryDirectory()
        self.root = Path(self.temp.name)
        (self.root / "assets").mkdir()
        (self.root / "assets" / "figure.png").write_bytes(b"test")
        self.readme = self.root / "README.md"

    def tearDown(self):
        self.temp.cleanup()

    def check(self, text):
        self.readme.write_text(text, encoding="utf-8")
        return check_catalog(self.readme, self.root)

    def test_valid_local_asset_and_https_link(self):
        errors = self.check(
            "[asset](assets/figure.png) [project](https://example.org/project)\n"
        )
        self.assertEqual(errors, [])

    def test_missing_local_target_fails(self):
        errors = self.check("[missing](assets/not-there.png)\n")
        self.assertEqual(len(errors), 1)
        self.assertIn("local link target does not exist", errors[0])

    def test_non_http_external_scheme_fails(self):
        errors = self.check("[unsafe](javascript:alert(1))\n")
        self.assertEqual(len(errors), 1)
        self.assertIn("unsupported or malformed URL", errors[0])

    def test_local_link_cannot_escape_repository_root(self):
        errors = self.check("[outside](../secret.txt)\n")
        self.assertEqual(len(errors), 1)
        self.assertIn("escapes repository root", errors[0])

    def test_fragment_only_link_is_ignored(self):
        self.assertEqual(self.check("[section](#contributing)\n"), [])


if __name__ == "__main__":
    unittest.main()
