
import sys
sys.path.append('../lib/gpt3')

from gpt3_api import GPT3API
from product_selection.product_picker import ProductPicker
from business_start.business_starter import BusinessStarter
from marketing.marketing_automator import MarketingAutomator
from order_fulfillment.order_fulfiller import OrderFulfiller

def main():
    gpt3_api = GPT3API()

    # Start a new business
    business_starter = BusinessStarter(gpt3_api)
    business_starter.start_business()

    # Pick products
    product_picker = ProductPicker(gpt3_api)
    product_picker.pick_products()

    # Market products
    marketing_automator = MarketingAutomator(gpt3_api)
    marketing_automator.market_products()

    # Fulfill orders
    order_fulfiller = OrderFulfiller(gpt3_api)
    order_fulfiller.fulfill_orders()

if __name__ == "__main__":
    main()
