import json

get_data_products = "products.json"


def load_data_products():
    """
    функция выводит список словарей продуктов:
    :return:list
    """
    # with open(get_data_products, "rt", encoding="utf-8") as file:
    #     data_products = json.load(file)
    # return data_products
# print(load_data_products())


class Category:
    all_quantity_category = 0  # общее количество всех категорий
    all_quantity_unique_product = 0  # количество уникальных продуктов
    name: str  # название категории
    description: str  # описание категории
    products: list  # товары
    quantity_of_categories = 0
    own_products = set()

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
        Category.quantity_of_categories += 1
        Category.own_products.union(set(products))


class Product:
    name: str  # название товара
    description: str  # описание товара
    price:  float  # цена товара
    quantity: int  # количество в наличии
    quantity_of_product = 0

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        self.amount_available = quantity
        Product.quantity_of_product += 1
