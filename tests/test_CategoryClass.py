import pytest

from src.CategoryClass import Category


@pytest.fixture
def category_example() -> Category:
    return Category(
        name="бытовая техника",
        description="телефоны и электроника",
        products=["iphone", "samsung"],
    )


def test_category(category_example):
    assert category_example.name == "бытовая техника"
    assert category_example.description == "телефоны и электроника"
    assert category_example.products == ["iphone", "samsung"]


def test_category_quantity(category_example):
    assert len(category_example.products) == 2
    category_example.products.append(
        "xiaomi redmi bomba plomba 12221 super puper red blue white edition"
    )
    assert len(category_example.products) == 3
