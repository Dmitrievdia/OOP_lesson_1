import func
import pytest


# @pytest.fixture
# def products():
#     return [
#         {
#             "name": "Смартфоны",
#             "description": "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
#             "products": [
#                 {
#                     "name": "Samsung Galaxy C23 Ultra",
#                     "description": "256GB, Серый цвет, 200MP камера",
#                     "price": 180000.0,
#                     "quantity": 5
#                 },
#             ]
#         },
#         {
#             "name": "Телевизоры",
#             "description": "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
#             "products": [
#                 {
#                     "name": "55\" QLED 4K",
#                     "description": "Фоновая подсветка",
#                     "price": 123000.0,
#                     "quantity": 7
#                 }
#             ]
#         }
#     ]


@pytest.fixture
def test_init_category():
    return func.Category("Смартфоны", "Cмартфоны, как средство не только коммуникации, "
                                      "но и получения дополнительных функций для удобства жизни", ['Apple, Samsung'])


@pytest.fixture
def test_init_product():
    return func.Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


def test_init_1(test_init_category):
    assert test_init_category.name == 'Смартфоны'
    assert test_init_category.description == ("Cмартфоны, как средство не только коммуникации, "
                                              "но и получения дополнительных функций для удобства жизни")
    assert test_init_category.products == ['Apple, Samsung']
    assert test_init_category.quantity_of_categories == 1
    # assert test_init_category.number_of_products == {'Apple, Samsung'}


def test_init_2(test_init_product):
    assert test_init_product.name == 'Samsung Galaxy S23 Ultra'
    assert test_init_product.description == '256GB, Серый цвет, 200MP камера'
    assert test_init_product.price == 180000.0
    assert test_init_product.quantity == 5
    assert test_init_product.quantity_of_product == 1




