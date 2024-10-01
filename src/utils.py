import json

from src.CategoryClass import Category
from src.ProductClass import Product


def get_categories(path: str = "..\\data\\products.json"):
    with open(path, "r") as f:
        data = json.load(f)
        categories = [
            Category(
                name=category["name"],
                description=category["description"],
                products=[
                    Product(
                        name=product["name"],
                        price=product["price"],
                        description=product["description"],
                        quantity=product["quantity"],
                    )
                    for product in category["products"]
                ],
            )
            for category in data
        ]
    return categories
