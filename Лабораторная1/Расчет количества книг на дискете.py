# TODO Найдите количество книг, которое можно разместить на дискете


size_of_disc = 1.44 * 1024 * 1024
count_of_page = 100
str_of_page = 50
sym_of_str = 25
size_of_sym = 4
count_symbol_in_book = sym_of_str * str_of_page * count_of_page
size_all_symbol_in_book = count_symbol_in_book * size_of_sym
count_of_books = int(size_of_disc // size_all_symbol_in_book)
print("Количество книг, помещающихся на дискету:", count_of_books)