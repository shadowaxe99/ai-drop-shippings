
import unittest
from src.business_start.business_starter import BusinessStarter

class TestBusinessStarter(unittest.TestCase):

    def setUp(self):
        self.business_starter = BusinessStarter()

    def test_start_business(self):
        result = self.business_starter.start_business()
        self.assertIsNotNone(result)
        self.assertEqual(result['status'], 'success')

    def test_handle_complex_scenarios(self):
        result = self.business_starter.handle_complex_scenarios()
        self.assertIsNotNone(result)
        self.assertEqual(result['status'], 'success')

if __name__ == '__main__':
    unittest.main()
