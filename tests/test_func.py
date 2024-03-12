import func
import pytest


@pytest.fixture
def test_init_category():
    return func.Category("Смартфоны", "Cмартфоны, как средство не только коммуникации, "
                                      "но и получения дополнительных функций для удобства жизни")


@pytest.fixture
def test_init_product():
    return func.Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


def test_init_1(test_init_category):
    assert test_init_category.name == 'Смартфоны'
    assert test_init_category.description == ("Cмартфоны, как средство не только коммуникации, "
                                              "но и получения дополнительных функций для удобства жизни")
    assert test_init_category.all_quantity_category == 2


def test_init_2(test_init_product):
    assert test_init_product.name == 'Samsung Galaxy S23 Ultra'
    assert test_init_product.description == '256GB, Серый цвет, 200MP камера'
    assert test_init_product.price == 180000.0
    assert test_init_product.quantity == 5
    assert test_init_product.quantity_of_product == 3
