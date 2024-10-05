import pytest

from src.CategoryClass import Category
from src.ProductClass import Product


@pytest.fixture
def category_example() -> Category:
    phones = [
        Product(name="iphone11", price=5.99, quantity=5, description="iphone11"),
        Product(name="iphone13", price=53.99, quantity=53, description="iphone13"),
        Product(name="iphone16", price=6, quantity=6, description="iphone16"),
    ]
    return Category(name="phones", description="бытовая техника", products=phones)


def test_category(category_example):
    assert category_example.name == "phones"
    assert category_example.description == "бытовая техника"
    assert category_example.products == (
        "iphone11, 5.99 руб. Остаток: 5 шт.\niphone13, 53.99 руб. Остаток: 53 шт.\niphone16, 6 руб. Остаток: 6 шт.\n"
    )
    assert category_example.category_count == 1
    assert category_example.product_count == 3


def test_add_product(category_example):
    category_example.add_product(
        Product(name="iphone19", price=5.99, quantity=9, description="iphone19")
    )
    assert category_example.products == (
        "iphone11, 5.99 руб. Остаток: 5 шт.\niphone13, 53.99 руб. Остаток: 53 шт.\n"
        "iphone16, 6 руб. Остаток: 6 шт.\niphone19, 5.99 руб. Остаток: 9 шт.\n"
    )

def test__str__(category_example: Category) -> None:
    assert str(category_example) == "phones, количество продуктов: 4 шт.\n"
