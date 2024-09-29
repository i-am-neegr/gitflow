class Product:
    """
    Product Class. Attributes: name, price, description, quantity
    """

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.description = description
        self.quantity = quantity
