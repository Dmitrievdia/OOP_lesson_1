class Category:
    all_quantity_category = 0  # общее количество всех категорий
    all_quantity_unique_product = 0  # количество уникальных продуктов
    name: str  # название категории
    description: str  # описание категории
    products: list  # товары
    # quantity_of_categories = 0  # счетчик категорий

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.__products = []  # список продуктов делаем приватным
        Category.all_quantity_category += 1
        Category.all_quantity_unique_product += len(self.__products)

    def add_products(self, product):
        """
        функция добавления продукта в список
        :param product: str (Samsung s-23)
        :return: list ['Samsung s-23']
        """
        self.__products.append(product)

    @property
    def display(self):
        """
        функция возвращает список продуктов
        :return: list ['Samsung s-23']
        """
        return self.__products

    @property
    def counting_products(self):
        """
        функция возвращает количество товаров
        :return: int
        """
        return len(self.__products)

    def __repr__(self):
        """
        функция возвращает список товаров в формате:
        Продукт, цена, остаток.
        :return: str
        """
        return f'{self.name}, {self.description}, {self.__products}'

    @property
    def get_products(self):
        """
        функция выводит список товаров в формате:
        Продукт, 80 руб. Остаток: 15 шт.
        :return:
        """
        result = ''
        for product in self.__products:
            result += f'\n{product.name},{product.price}руб. Остаток: {product.quantity} шт.'
        return result


class Product:
    name: str  # название товара
    description: str  # описание товара
    price: float  # цена товара
    quantity: int  # количество в наличии
    quantity_of_product = 0  # счетчик количества продуктов

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        self.amount_available = quantity  # доступное количество
        Product.quantity_of_product += 1

    def __repr__(self):
        return f'{self.name}, {self.description}, {self.__price}, {self.quantity}'

    @classmethod
    def add_product(cls, new_product):
        """
        класс-метод для добавления нового товара
        :param new_product: str
        :return:
        """
        return cls(**new_product)

    @property
    def price(self):  # геттер для установки цены
        return self.__price

    @price.setter
    def price(self, new_price):  # сеттер для изменения цены
        """
        сеттер если цена <= 0 то "введена некорректная цена" иначе вывод цены
        :param new_price: float
        :return: float
        """
        if new_price <= 0:
            print("Введена некорректная цена")
        else:
            self.__price = new_price


category = Category("Категория1", "qwerty")
product = Product("Продукт1", "йцукен", 18000, 5)
product1 = Product("Продукт2", "йцукен", 12000, 77)
category.add_products(product1)
category.add_products(product)


print(product)
print(product1)
