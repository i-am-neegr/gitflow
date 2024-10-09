import pytest

from src.ProductClass import LawnGrass, Product, Smartphone


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


@pytest.fixture
def smartphone_example() -> Smartphone:
    return Smartphone(
        "Xiaomi Redmi Note 11",
        "1024GB, Синий",
        31000.0,
        1,
        90.3,
        "Note 11",
        1024,
        "Синий",
    )


def test__init__smartphone(smartphone_example):
    assert smartphone_example.name == "Xiaomi Redmi Note 11"
    assert smartphone_example.description == "1024GB, Синий"
    assert smartphone_example.price == 31000.0
    assert smartphone_example.quantity == 1
    assert smartphone_example.efficiency == 90.3
    assert smartphone_example.model == "Note 11"
    assert smartphone_example.memory == 1024
    assert smartphone_example.color == "Синий"


def test__add__smartphone(smartphone_example):
    assert smartphone_example + smartphone_example == 62000.0


def test__add__smartphone_error(smartphone_example, product_example):
    with pytest.raises(TypeError):
        smartphone_example + product_example


@pytest.fixture
def lawngrass_example() -> LawnGrass:
    return LawnGrass(
        "Газонная трава 2",
        "Выносливая трава",
        450.0,
        1,
        "США",
        "5 дней",
        "Темно-зеленый",
    )


def test__init__lawngrass(lawngrass_example):
    assert lawngrass_example.name == "Газонная трава 2"
    assert lawngrass_example.description == "Выносливая трава"
    assert lawngrass_example.price == 450.0
    assert lawngrass_example.quantity == 1
    assert lawngrass_example.country == "США"
    assert lawngrass_example.germination_period == "5 дней"
    assert lawngrass_example.color == "Темно-зеленый"


def test__add__lawngrass(lawngrass_example):
    assert lawngrass_example + lawngrass_example == 900.0


def test__add__lawngrass_error(lawngrass_example, product_example):
    with pytest.raises(TypeError):
        lawngrass_example + product_example
