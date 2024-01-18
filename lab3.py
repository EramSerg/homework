class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = None
        self.validate_pages(pages)

    def __str__(self):
        super().__str__()
        return f"Книга '{self.name}'. Автор: {self.author}. Количество страниц: {self.pages}"

    def __repr__(self):
        super().__repr__()
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"

    def validate_pages(self, pages):
        if not isinstance(pages, int):
            raise TypeError(f"Не верный формат данных: {pages}")
        self.pages = pages


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = None
        self.validate_duration(duration)

    def __str__(self):
        super().__str__()
        return f"Книга '{self.name}'. Автор: {self.author}. Продолжительность: {self.duration} минут."

    def __repr__(self):
        super().__repr__()
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}), duration={self.duration!r}"

    def validate_duration(self, duration):
        if not isinstance(duration, float):
            raise TypeError(f"Не верный формат данных: {duration}")
        self.duration = duration


if __name__ == "__main__":
    book_1 = PaperBook('Шерлок Хомс', 'А.Конан Дойл', 500)
    print(book_1)
    print(repr(book_1))
    book_4 = AudioBook('Сказки', 'А.С.Пушкин', 500.3)
    print(book_4)
    print(repr(book_4))

    # Проверка работы валидации параметров:
    #book_2 = PaperBook('Сказки', 'А.С.Пушкин', '250')
    #print(book2')
    #book_3 = AudioBook('Шерлок Хомс', 'А.Конан Дойл', '500.3')
    #print(book_3)


