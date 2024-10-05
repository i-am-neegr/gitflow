import pytest

from src.ProductClass import Product


@pytest.fixture
def product_example() -> Product:
    return Product(name="iphone", price=5.99, quantity=1, description="iphone11")


def test_product(product_example):
    assert product_example.name == "iphone"
    assert product_example.price == 5.99
    assert product_example.quantity == 1
    assert product_example.description == "iphone11"


def test_product_quantity(product_example):
    assert product_example.quantity == 1
    product_example.quantity += 1
    assert product_example.quantity == 2


def test__str__(product_example):
    assert str(product_example) == "iphone, 5.99 руб. Остаток: 1 шт.\n"


def test__add__(product_example):
    assert product_example + product_example == 11.98
