from abc import ABC, abstractmethod

from src.MixinProduct import MixinProduct


class BaseProduct(ABC):

    @abstractmethod
    def __init__(
        self, name: str, description: str, price: float, quantity: int
    ) -> None:
        pass

    @abstractmethod
    def __add__(self, other):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @classmethod
    @abstractmethod
    def new_product(cls, data):
        pass

    @property
    @abstractmethod
    def price(self):
        pass

    @price.setter
    @abstractmethod
    def price(self, value):
        pass


class Product(MixinProduct, BaseProduct):
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
        super().__init__(name, description, price, quantity)

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт.\n"

    def __add__(self, other):
        return self.price * self.quantity + other.price * other.quantity

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


class Smartphone(Product):

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        if type(other) is self.__class__:
            res = super().__add__(other)
            return res
        else:
            raise TypeError


class LawnGrass(Product):

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        if type(other) is self.__class__:
            res = super().__add__(other)
            return res
        else:
            raise TypeError
