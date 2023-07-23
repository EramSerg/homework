numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
element = numbers.index(None)
numbers.remove(None)
sum_of_numbers = sum(numbers)
count_of_numbers = len(numbers) + 1
av_numbers = sum_of_numbers / count_of_numbers
numbers.insert(element, av_numbers)
print('Измененный список:', numbers)





