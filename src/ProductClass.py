class Product:
    """
    Product Class. Attributes: name, price, description, quantity
    """

    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.__price = price
        self.description = description
        self.quantity = quantity

    @classmethod
    def new_product(cls, data: dict):
        return cls(
            data.get("name", "No name"),
            data.get("description", "No description"),
            data.get("price", 0.0),
            data.get("quantity", 0),
        )

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price must be greater than or equal to 0")
        else:
            self.__price = value
