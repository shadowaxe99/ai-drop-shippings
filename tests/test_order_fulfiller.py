
import unittest
from src.order_fulfillment.order_fulfiller import OrderFulfiller

class TestOrderFulfiller(unittest.TestCase):

    def setUp(self):
        self.order_fulfiller = OrderFulfiller()

    def test_fulfill_order(self):
        order_id = 123
        result = self.order_fulfiller.fulfill_order(order_id)
        self.assertEqual(result, True)

    def test_handle_failed_order(self):
        order_id = 456
        result = self.order_fulfiller.handle_failed_order(order_id)
        self.assertEqual(result, True)

if __name__ == '__main__':
    unittest.main()

