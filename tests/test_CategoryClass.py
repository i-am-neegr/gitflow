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
    assert len(category_example.products) == 3
    assert category_example.category_count == 1
    assert category_example.product_count == 3
