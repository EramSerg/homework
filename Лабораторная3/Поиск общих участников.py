# TODO Напишите функцию find_common_participants
def find_common_participants(participants_first_group, participants_second_group, delimiter=','):
    first_group = set(list(participants_first_group.split(delimiter)))
    second_group = set(list(participants_second_group.split(delimiter)))
    intersection_group = first_group.intersection(second_group)
    return sorted(list(intersection_group))

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, delimiter='|'))

print(find_common_participants(participants_first_group, participants_second_group))
