import re
import itertools


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

        if not self.validation_country(country):
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


class User:
    def __init__(self, name: str, last_name: str, nicname: str, age: int, email: str, phone_number: str, address: Address, login: str, password: str):
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
        self.age_group = AgeGroupOfUser(self.age).age_group     # так можно делать или как правильно определять в данном случае?

        self.email = self.validation_email(email)

        if not self.validation_phone_number(phone_number):
            raise ValueError("Формат номера телефона не прошел валидацию, проверьте корректность заполнения данных.")
        self.phone_number = self.format_phone_numbers(phone_number)

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
            raise ValueError("Формат email не прошел валидацию, проверьте корректность заполнения данных.")

        return email

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
    categories = [0, 6, 12, 18]

    def __init__(self, age: int):
        """
        Создание и подготовка к работе объекта возрастная группа пользователя
        :param age: возраст пользователя
        """

        self.age_group = self.validate_age(age)

    def validate_age(self, age: int):
        """
        Фугкция проверки возраста на соответствие категории
        :param age: возраст пользователя
        :return: строку с указанием возрастной категории пользователя
        """

        if not isinstance(age, int):
            raise TypeError("Неверный формат ввода возраста пользователя, должен быть тип integer.")

        # Можно проверить что возраст не отрицательный

        # Как аналог коду ниже
        for min_age, max_age in itertools.pairwise(
                self.categories):  # К классовым атрибутам можно также обращаться через self (так как они лежат и в области памяти экземпляра)
            if age < max_age:
                return f"Возрастная категория {min_age}+"
        return f"Возрастная категория {max_age}+"


if __name__ == "__main__":
    a_g = AgeGroupOfUser(13)
    print(a_g.age_group)
    try:
        print(Address(post_index=1, country=1, city=1, district=1, street=1, home_number=1, flat_number=1))
    except ValueError as e:
        print(f"Ошибка: {e}")

    adr = Address(post_index=1, country="Россия", city=1, district=1, street=1, home_number=1, flat_number=1)
    user = User(name="user", last_name="test", nicname="user_test", age=15, email="young_troll@gmail.com", phone_number="89991234567", address=adr, login="login", password="password")

    print(user.phone_number)

