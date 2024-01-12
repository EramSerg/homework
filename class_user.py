import re


class User:
    def __init__(self, name: str, last_name: str, nicname: str, age: int, user_age_category: str, email: str, phone_number: str, address: object, login: str, password: str):
        """
        Создание и подготовка к работе объекта Пользователь
        :param name: имя пользователя
        :param last_name: фамилия пользователя
        :param nicname: псевдоним пользователя
        :param age: возраст пользователя
        :param email: адресс электронной почты пользователя
        :param phone_number: номер телефона пользователя
        :param address: физический адресс пользователя
        :param login: логин для входа пользователя
        :param password: пароль для входа пользователя
        """
        if not isinstance(name, str):
            raise TypeError("Неверный формат ввода имени пользователя, должен быть тип string.")
        if not name.isalpha():
            raise ValueError("Введенное имя содержит недопустимые символы.")
        self.name = name

        if not isinstance(last_name, str):
            raise TypeError("Неверный формат ввода фамилии пользователя, должен быть тип string.")
        if not last_name.isalpha():
            raise ValueError("Введенная фамилия содержит недопустимые символы.")
        self.last_name = last_name

        if not isinstance(age, int):
            raise TypeError("Неверный формат ввода возраста пользователя, должен быть тип integer.")
        self.age = age
        AgeGroupOfUser.validate_age = user_age_category     # так можно делать или как правильно определять в данном случае?

        if not self.validation_email:
            raise ValueError("Формат email не прошел валидацию, проверьте корректность заполнения данных.")
        self.email = email

        if not self.validation_phone_number:
            raise ValueError("Формат номера телефона не прошел валидацию, проверьте корректность заполнения данных.")
        self.format_phone_numbers = phone_number

        self.nicname = nicname
        self.address = address  # как правильно сослаться на class Address?
        self.login = login
        self.password = password

    def validation_email(self, email: str):
        """
        Функция проверки валидности адреса электронной почты пользователя
        :param email: адрес электронной почты пользователя
        :return: True или False в зависимости от результата проверки
        """
        pattern = r"^[-\w\.]+@([-\w]+\.)+[-\w]{2,4}$"

        if re.match(pattern, email) is None:
            return False
        return True

    def validation_phone_number(self, phone_number: str):
        """
        Функция проверки валидности телефонного номера пользователя
        :param phone_number: номер мобильного телефона пользователя (в примере учитываются только номера
        мобильных операторов РФ)
        :return: True или False в зависимости от результата проверки
        """
        pattern = r'(^[+|8|\d])\s?(\(.{3}\))?([0-9,-]{7})\d{1,}'
        if re.match(pattern, phone_number):
            return True
        return False

    def format_phone_numbers(self, phone_number: str):
        """
        Функция приведения номера мобильного телефона пользователя к единому стандарту
        :param phone_number: номер мобильного телефона пользователя (в примере учитываются только номера
        мобильных операторов РФ)
        :return: строку с номером телефона пользователя вида +7(123)123-45-67
        """
        return '+7({0}{1}{2}){3}{4}{5}-{6}{7}-{8}{9}'.format(*[i for i in phone_number if i.isdigit()][1:])


class AgeGroupOfUser:
    def __init__(self, age: int, age_category: str):
        """
        Создание и подготовка к работе объекта возрастная группа пользователя
        :param age: возраст пользователя
        """

        if not isinstance(age, int):
            raise TypeError("Неверный формат ввода возраста пользователя, должен быть тип integer.")
        self.age = age

        self.validate_age = age_category

    def validate_age(self, age: int, category: str):
        """
        Фугкция проверки возраста на соответствие категории
        :param age: возраст пользователя
        :param category: возрастная категория пользователя (0+, 6+, 12+, 18+)
        :return: строку с указанием возрастной категории пользователя
        """
        categories = ['0+', '6+', '12+', '18+']
        if not isinstance(age, int):
            raise TypeError("Неверный формат ввода возраста пользователя, должен быть тип integer.")
        if category not in categories:
            raise ValueError("Выбрана несуществующая возрастная категория.")
        if 0 < age < 6:
            return "Возрастная категория 0+"
        elif 6 <= age < 12:
            return "Возрастная категория 6+"
        elif 12 <= age < 18:
            return "Возрастная категория 12+"
        elif age >= 18:
            return "Возрастная категория 18+"


class Address:
    def __init__(self, post_index: int, country: str, city: str, district: str, street: str, home_number: int, flat_number: int):
        """
        Создание и подготовка к работе объекта адресс пользователя
        :param post_index: почтовый индекс
        :param country: страна
        :param city: город
        :param district: район
        :param street: улица
        :param home_number: номер дома
        :param flat_number: номер квартиры
        """
        if not isinstance(post_index, int):
            raise TypeError("Неверный формат почтового индекса, должен быть integer.")
        self.post_index = post_index

        if not self.validation_country:
            raise ValueError("Укаазана недопустимая страна.")
        self.country = country

        self.city = city
        self.district = district
        self.street = street
        self.home_number = home_number
        self.flat_number = flat_number

    def validation_country(self, country):
        """
        Функция проверки существования страны (список стран дан просто для примера, в идеале,
        список стран выделяется в отдельный файл и импортируется
        :param country: страна пользователя
        :return: True или False в зависимотси от успешности валидации
        """
        countries = ["Россия", "Соединенные Штаты Америки", "Германия", "Финляндия", "Казахстан", "Китай", "Алжир", "Япония"]
        if country not in countries:
            return False

        return True
