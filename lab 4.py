class Vehicle:
    """
    Базовый класс Автомобиль
    """

    def __init__(self, brand: str, model: str, year_release: str, equipment: str, price: (int, float),
                 factory_price: (int, float)):
        self.brand = brand
        self.model = model
        self.year_release = year_release
        self.equipment = equipment
        self.price = price
        self.__factory_price = factory_price

    def __str__(self):
        """
        Определние функции __str__
        :return: возвращает f-строку с перечислением значений атрибутов экземпляра класса
        """
        return (f"Марка: {self.brand},\nМодель: {self.model},\nгод выпуска: {self.year_release},\n"
                f"комплектация: {self.equipment},\nцена: {self.price},\nцена завода: {self.__factory_price}$")

    def __repr__(self):
        """
        Определние функции __repr__
        :return: возвращает f-строку с указанием принадлежности к классу и перечислением атрибутов со значениями
        """
        return (f"{self.__class__.__name__}(brand={self.brand}, model={self.model}, year_release={self.year_release},"
                f"equipment={self.equipment}, price={self.price}, factory_price={self.__factory_price})")

    def show_factory_price(self):
        """
        Функция отображения приватного атрибута класса __factory_price
        :return: возвращает f-строку с ценой завода изготовителя без наценки
        """
        return f"Цена завода-изготовителя: {self.__factory_price}$"


class Car(Vehicle):
    """
    Класс легковых автомибилей - дочерний класс базового класса Vehicle
    """

    def __init__(self, brand, model, year_release, equipment, price, factory_price, body_type: str):
        """
        Функция инициализации экземпляра класса с наследованием параметров базового класса и
        расширена локальными атрибутами
        :param brand: унаследовано от базового класса
        :param model: унаследовано от базового класса
        :param year_release: унаследовано от базового класса
        :param equipment: унаследовано от базового класса
        :param price: унаследовано от базового класса
        :param factory_price: унаследовано от базового класса
        :param body_type: тип кузова
        """
        super().__init__(brand, model, year_release, equipment, price, factory_price)
        self.body_type = body_type

    def __str__(self):
        """
        Переопределение функции __str__ базового класса
        :return: возвращает f-строку с перечислением значений атрибутов экземпляра класса унаследованных
        от базового класса + собственных
        """
        super().__str__()
        return (f"Марка: {self.brand},\nМодель: {self.model},\nгод выпуска: {self.year_release},\n"
                f"комплектация: {self.equipment},\nцена: {self.price}$,\nтип кузова: {self.body_type}")

    def __repr__(self):
        """
        Переопределение функции __repr__ базового класса
        :return: возвращает f-строку с указанием принадлежности к классу и перечислением атрибутов
         (базового класса + собственных) со значениями
        """
        super().__repr__()
        return (f"{self.__class__.__name__}(brand={self.brand}, model={self.model}, year_release={self.year_release},"
                f"equipment={self.equipment}, price={self.price}, body_type={self.body_type})")

    def show_factory_price(self):
        """
        Функция отображения приватного атрибута класса __factory_price, унаследованная от базового класса
        :return: возвращает f-строку с ценой завода изготовителя без наценки
        """
        return super().show_factory_price()


class Truck(Vehicle):
    """
    Класс грузовых автомобилей - дочерний класс базового класса Vehicle
    """

    def __init__(self, brand, model, year_release, equipment, price, factory_price, lifting_capacity: int,
                 body_length: float, body_height: float):
        """
        Функция инициализации экземпляра класса с наследованием параметров базового класса и
        расширена локальными атрибутами
        :param brand: унаследовано от базового класса
        :param model: унаследовано от базового класса
        :param year_release: унаследовано от базового класса
        :param equipment: унаследовано от базового класса
        :param price: унаследовано от базового класса
        :param factory_price: унаследовано от базового класса
        :param lifting_capacity: грузоподъемность
        :param body_length: длина кузова
        :param body_height: высота кузова
        """
        super().__init__(brand, model, year_release, equipment, price, factory_price)
        self.lifting_capacity = lifting_capacity
        self.body_length = body_length
        self.body_height = body_height

    def __str__(self):
        """
        Переопределение функции __str__ базового класса
        :return: возвращает f-строку с перечислением значений атрибутов экземпляра класса унаследованных
        от базового класса + собственных
        """
        return (f"Марка: {self.brand},\nМодель: {self.model},\nгод выпуска: {self.year_release},\n"
                f"комплектация: {self.equipment},\nцена: {self.price}$,\nгрузоподъемность: {self.lifting_capacity} тонн,\n"
                f"длина кузова: {self.body_length} м,\nвысота кузова: {self.body_height} м")

    def __repr__(self):
        """
        Переопределение функции __repr__ базового класса
        :return: возвращает f-строку с указанием принадлежности к классу и перечислением атрибутов
         (базового класса + собственных) со значениями
        """
        return (f"{self.__class__.__name__}(brand={self.brand}, model={self.model}, year_release={self.year_release},"
                f"equipment={self.equipment}, price={self.price}, lifting_capacity={self.lifting_capacity},"
                f"body_length={self.body_length}, body_height={self.body_height})")

    def show_factory_price(self):
        """
        Функция отображения приватного атрибута класса __factory_price, унаследованная от базового класса
        :return: возвращает f-строку с ценой завода изготовителя без наценки
        """
        return super().show_factory_price()


if __name__ == "__main__":
    car1 = Vehicle('WV', 'Jetta', '2023', 'comfort', 10000, 9500)
    print(car1)
    print(repr(car1))

    my_car = Car('Volvo', 'XC-90', '2021', 'comfort', 21000, 19000, 'crossover')
    print(my_car)
    print(repr(my_car))
    print(my_car.show_factory_price())

    my_truck = Truck('Scania', 'SC-120', '2020', 'havy', 46000, 41000, 12, 12.2, 2.2)
    print(my_truck)
    print(repr(my_truck))
    print(my_truck.show_factory_price())
    pass
