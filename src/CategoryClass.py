from src.ProductClass import Product


class Category:
    """
    Category class. Attributes: name, description, products, count_category, count_products
    """

    name: str
    description: str
    products: list
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: list[Product]):
        self.name = name
        self.description = description
        self.products = products
        self.product_count += len(products)
        Category.category_count += 1
