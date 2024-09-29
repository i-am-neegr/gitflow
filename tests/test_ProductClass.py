import pytest

from src.ProductClass import Product


@pytest.fixture
def product_example() -> Product:
    return Product(name="iphone", price=5.99, quantity=5, description="iphone11")


def test_product(product_example):
    assert product_example.name == "iphone"
    assert product_example.price == 5.99
    assert product_example.quantity == 5
    assert product_example.description == "iphone11"


def test_product_quantity(product_example):
    assert product_example.quantity == 5
    product_example.quantity += 1
    assert product_example.quantity == 6
