import json

get_data_products = "products.json"


def load_data_products():
    """
    функция выводит список словарей продуктов:
    :return:list
    """
    with open(get_data_products, "rt", encoding="utf-8") as file:
        data_products = json.load(file)
    return data_products
# print(load_data_products())


# class Category:
#     name: str # название категории
#     description: str # описание категории
#     products: str # товары
#
#     def __init__(self, name, description, products):
#         self.name = name
#         self.description = description
#         self.products = products
#
# class Product:
#     name: str # название товара
#     description: str # описание товара
#     price:  float # цена товара
#     quantity: int # количество в наличии
#
#     def __init__(self, name, description, price, quantity):
#         self.name = name
#         self.description = description
#         self.price = price
#         self.amount_available = quantity
