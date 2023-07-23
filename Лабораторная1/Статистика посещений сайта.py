users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']
count_of_visits = len(users)
# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
unique_of_users = set(users)
unique_counts_of_users = len(unique_of_users)
dict = {"Общее количество": 0, "Уникальные посещения": 0}
dict["Общее количество"] = count_of_visits
dict["Уникальные посещения"] = unique_counts_of_users


print(dict)