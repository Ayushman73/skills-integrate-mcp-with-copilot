import unittest

from fastapi.testclient import TestClient
from src.app import app


class ActivityApiTests(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_github_skills_activity_is_listed(self):
        response = self.client.get("/activities")
        self.assertEqual(response.status_code, 200)
        self.assertIn("GitHub Skills", response.json())


if __name__ == "__main__":
    unittest.main()
