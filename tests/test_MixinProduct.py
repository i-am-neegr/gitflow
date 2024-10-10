from _pytest.capture import CaptureFixture

from src.ProductClass import Product


def test__init__(capsys: CaptureFixture):
    Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    console_log = capsys.readouterr()
    assert (
        console_log.out.strip() == "Product(Iphone 15, 512GB, Gray space, 210000.0, 8)"
    )
