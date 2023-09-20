
import json
from lib.gpt3.gpt3_api import GPT3API

class ProductPicker:
    def __init__(self):
        self.gpt3_api = GPT3API()

    def load_products(self):
        with open('data/products.json') as f:
            self.products = json.load(f)

    def pick_products(self):
        self.load_products()
        picked_products = []
        for product in self.products:
            prompt = f"Should we include {product['name']} in our drop shipping business? {product['description']}"
            response = self.gpt3_api.generate_text(prompt)
            if 'yes' in response.lower():
                picked_products.append(product)
        return picked_products

if __name__ == "__main__":
    picker = ProductPicker()
    picked_products = picker.pick_products()
    print(f"Picked Products: {picked_products}")
