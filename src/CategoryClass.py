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
        self.product_count += len(products)
        Category.category_count += 1

    @property
    def products(self):
        product_list = ""
        for product in self.__products:
            product_list += (
                f"{product.name}, {product.price}. остаток: {product.quantity}.\n"
            )
        return product_list

    def add_product(self, product: Product):
        self.__products.append(product)
        Category.product_count += 1


cat = Category(
    name="phones",
    description="бытовая техника",
    products=[
        Product(name="iphone11", price=5.99, quantity=5, description="iphone11"),
        Product(name="iphone13", price=53.99, quantity=53, description="iphone13"),
        Product(name="iphone16", price=6, quantity=6, description="iphone16"),
    ],
)
cat.add_product(
    Product(name="iphone19", price=5.99, quantity=9, description="iphone19")
)
print(cat.products)
