
import unittest
from src.marketing.marketing_automator import MarketingAutomator

class TestMarketingAutomator(unittest.TestCase):
    def setUp(self):
        self.marketing_automator = MarketingAutomator()

    def test_generate_ad(self):
        product = {"name": "Test Product", "description": "This is a test product"}
        ad = self.marketing_automator.generate_ad(product)
        self.assertIn(product['name'], ad)
        self.assertIn(product['description'], ad)

    def test_schedule_ad(self):
        schedule = self.marketing_automator.schedule_ad("Test Ad", "2022-01-01 00:00:00")
        self.assertEqual(schedule, "Ad scheduled for 2022-01-01 00:00:00")

if __name__ == '__main__':
    unittest.main()
