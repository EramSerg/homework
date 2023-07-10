list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]
len_list_players = len(list_players)
command_1 = list_players[0:int(len_list_players / 2)]
command_2 = list_players[int(len_list_players / 2):]
# TODO Разделите участников на две команды
print(command_1)
print(command_2)