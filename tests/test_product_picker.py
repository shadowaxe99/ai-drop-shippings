
import unittest
from src.product_selection.product_picker import ProductPicker

class TestProductPicker(unittest.TestCase):

    def setUp(self):
        self.product_picker = ProductPicker()

    def test_pick_product(self):
        product = self.product_picker.pick_product()
        self.assertIsNotNone(product, "Product should not be None")

    def test_pick_product_with_criteria(self):
        criteria = {"category": "Electronics", "price_range": (50, 200)}
        product = self.product_picker.pick_product(criteria)
        self.assertIsNotNone(product, "Product should not be None")
        self.assertEqual(product["category"], criteria["category"], "Product category should match criteria")
        self.assertTrue(criteria["price_range"][0] <= product["price"] <= criteria["price_range"][1], "Product price should be within criteria range")

if __name__ == '__main__':
    unittest.main()

