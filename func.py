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
        # for item in self.__products:
        #     if item[0] == product.name:  # Проверяем наименование товара есть ли в списке продуктов
        #         item[3] += product.quantity  # Обновляем количество товаров в продукте который уже есть
        #         break
        #     else:
        #         self.__products.append([product.name, product.description, product.price, product.quantity])
        #         Category.all_quantity_unique_product += 1
        return self.__products.append([product])

    # @property
    # def counting_products(self):
    #     count = 0
    #     for i in self.__products:
    #         count += i[3]
    #
    #     return count

    @property
    def display(self):
        """
        функция возвращает список продуктов
        :return: list ['Samsung s-23']
        """
        return self.__products

    def __repr__(self):
        """
        функция возвращает экземпляр категории в формате:
        Продукт, цена, остаток.
        :return: str
        """
        return f'{self.name}, {self.description}, {self.__products}'

    @property
    def get_products(self):
        """
        геттер-функция выводит список товаров в необходимом формате:
        Продукт, 80 руб. Остаток: 15 шт.
        :return:
        """
        result = ''
        for product in self.__products:
            result += f'\n{product.name},{product.price}руб. Остаток: {product.quantity} шт.'
        return result

    @property
    def counting_products(self):
        """
        функция возвращает количество товаров на складе
        :return: int
        """
        return len(self.__products)


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
            if self.__price > new_price:
                input_user = input("Подтвердите понижение стоимости (y/n):\n").strip()
                if input_user == "y":
                    self.__price = new_price
                else:
                    print("Цена не изменилась")
            self.__price = new_price

    def __repr__(self):
        # Добавлено отображение результата
        return f'{self.name}, {self.description}, {self.__price}, {self.quantity}'

    def __str__(self):
        # Добавлено строковое отображение
        return f'\n{self.name}, {self.__price} руб. Остаток: {self.quantity} шт.'


if __name__ == '__main__':
    # Создание словаря для дальнейшего добавления в экземпляры класса
    new_product_3 = {
        'name': 'Nokia',
        'description': 'smth',
        'price': 1000,
        'quantity': 10
    }

    product_3 = Product.add_product(new_product_3)  # Добавление нового продукта
    print(product_3)  # Вывод добавленного словаря

    product_1 = Product('Samsung', 'smth', 90_000, 2)
    print(product_1)
    product_2 = Product('iPhone', 'smth', 100_000, 3)  # Экземпляр класса Product
    print(product_2)
    # print(f'Метод add для 2х экземпляров класса Product: {product_1} + {product_2}')


# работа с категориями и продуктами
    category_1 = Category('Телефоны', 'мобильные телефоны')  # Экземпляр класса Category
    product_1 = Product('Samsung', 'smth', 80_000, 8)  # Экземпляр класса Product
    product_2 = Product('iPhone', 'smth', 130_000, 12)  # Экземпляр класса Product

    category_1.add_products(product_1)  # Добавление продукта в приватный список товаров
    category_1.add_products(product_2)  # Добавление продукта в приватный список товаров
    # print(category_1.add_products)

    product_3 = Product('iPhone', 'smth', 130_000, 34)
    category_1.add_products(product_3)  # Добавление продукта в приватный список товаров если такой продукт существует
    # print(category_1.add_products)  # Отображение приватного списка товаров

    # print(f'\nУникальных продуктов: {category_1.all_quantity_unique_product}')  # Кол-во уник-х товаров в прив. списке
    # print(category_1.get_products)  # Получение перечня товаров в определенном формате
    # print(str(category_1))  # Отображение строкового представления

    # print(f'Общее количество продуктов категории: {category_1.all_quantity_unique_product}')
