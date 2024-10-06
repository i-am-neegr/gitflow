from src.ProductClass import Product


class Category:
    """
    Category class. Attributes: name, description, products, count_category, count_products
    """

    name: str
    description: str
    __products: list
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: list[Product]):
        self.name = name
        self.description = description
        self.__products = products
        Category.product_count += len(products)
        Category.category_count += 1

    def __str__(self) -> str:
        return f"{self.name}, количество продуктов: {Category.product_count} шт.\n"

    @property
    def products(self):
        product_list = ""
        for product in self.__products:
            product_list += str(product)
        return product_list

    def add_product(self, product: Product):
        self.__products.append(product)
        Category.product_count += 1
