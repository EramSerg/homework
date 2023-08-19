# TODO решите задачу
import json

INPUT_FILE = 'input.json'


def task() -> float:
    with open(INPUT_FILE, 'r') as file:
        json_file = json.load(file)
    
    score_weight_list = [(value['score'] * value['weight']) for value in json_file]
    
    return round(sum(score_weight_list), 3)


print(task())

