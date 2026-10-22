import copy
import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "validate_project_catalog.py"
CATALOG_PATH = ROOT / "catalog" / "projects.json"
SPEC = importlib.util.spec_from_file_location("validate_project_catalog", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class ProjectCatalogValidationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalog = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))

    def test_repository_catalog_is_valid(self):
        self.assertEqual(MODULE.validate_catalog(self.catalog), [])

    def test_root_must_be_object(self):
        self.assertIn("catalog root must be a JSON object",
                      MODULE.validate_catalog([]))

    def test_empty_project_list_fails(self):
        data = copy.deepcopy(self.catalog)
        data["projects"] = []
        self.assertIn("projects must be a non-empty list",
                      MODULE.validate_catalog(data))

    def test_duplicate_project_ids_fail(self):
        data = copy.deepcopy(self.catalog)
        data["projects"].append(copy.deepcopy(data["projects"][0]))
        self.assertTrue(any("duplicates" in error for error in MODULE.validate_catalog(data)))

    def test_missing_project_field_fails(self):
        data = copy.deepcopy(self.catalog)
        del data["projects"][0]["description"]
        self.assertTrue(any("missing required fields" in error
                            for error in MODULE.validate_catalog(data)))

    def test_http_homepage_is_rejected(self):
        data = copy.deepcopy(self.catalog)
        data["projects"][0]["homepage"] = "http://example.org"
        self.assertTrue(any("homepage must be an absolute HTTPS URL" in error
                            for error in MODULE.validate_catalog(data)))

    def test_credentials_in_resource_url_are_rejected(self):
        data = copy.deepcopy(self.catalog)
        data["projects"][0]["resources"][0]["url"] = "https://user:pass@example.org/x"
        self.assertTrue(any("resources[0].url must be an absolute HTTPS URL" in error
                            for error in MODULE.validate_catalog(data)))

    def test_empty_task_list_is_rejected(self):
        data = copy.deepcopy(self.catalog)
        data["projects"][0]["tasks"] = []
        self.assertTrue(any(".tasks must be a non-empty list" in error
                            for error in MODULE.validate_catalog(data)))

    def test_duplicate_task_labels_are_rejected(self):
        data = copy.deepcopy(self.catalog)
        data["projects"][0]["tasks"].append(data["projects"][0]["tasks"][0])
        self.assertTrue(any(".tasks must not contain duplicates" in error
                            for error in MODULE.validate_catalog(data)))

    def test_resource_requires_https_url(self):
        data = copy.deepcopy(self.catalog)
        data["projects"][0]["resources"][0]["url"] = "javascript:alert(1)"
        self.assertTrue(any("resources[0].url must be an absolute HTTPS URL" in error
                            for error in MODULE.validate_catalog(data)))

    def test_cli_passes_for_repository_catalog(self):
        result = subprocess.run(
            [sys.executable, str(SCRIPT), str(CATALOG_PATH)],
            capture_output=True, text=True, check=False)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("5 projects", result.stdout)

    def test_cli_returns_nonzero_for_invalid_json(self):
        from tempfile import TemporaryDirectory
        with TemporaryDirectory() as directory:
            path = Path(directory) / "invalid.json"
            path.write_text("{broken", encoding="utf-8")
            result = subprocess.run(
                [sys.executable, str(SCRIPT), str(path)],
                capture_output=True, text=True, check=False)
        self.assertEqual(result.returncode, 2)
        self.assertIn("invalid JSON", result.stderr)


if __name__ == "__main__":
    unittest.main()
