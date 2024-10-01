import json

import pytest

from src.utils import get_categories

from unittest.mock import patch


@pytest.fixture
def data_example():
    data = [
        {
            "name": "Смартфоны",
            "description": "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
            "products": [
                {
                    "name": "Xiaomi Redmi Note 11",
                    "description": "1024GB, Синий",
                    "price": 31000.0,
                    "quantity": 14,
                }
            ],
        },
        {
            "name": "Телевизоры",
            "description": "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
            "products": [
                {
                    "name": '55" QLED 4K',
                    "description": "Фоновая подсветка",
                    "price": 123000.0,
                    "quantity": 7,
                }
            ],
        },
    ]
    return data


@patch('builtins.open')
def test_get_categories(mock_open, data_example):
    mock_file = mock_open.return_value.__enter__.return_value
    mock_file.read.return_value = json.dumps(data_example)
    result = get_categories()
    for i in range(len(data_example)):
        assert result[i].name == data_example[i]['name']
        assert result[i].description == data_example[i]['description']
        assert result[i].products[0].name == data_example[i]['products'][0]['name']
        assert result[i].products[0].price == data_example[i]['products'][0]['price']