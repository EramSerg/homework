# TODO импортировать необходимые молули
import json
import csv

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:

    with open(INPUT_FILENAME) as csv_file:
        csv_file_r = csv.DictReader(csv_file)
        json_list = []
        for row in csv_file_r:
            json_list.append(row)


    with open(OUTPUT_FILENAME, 'w') as json_file:
        json_string = json.dumps(json_list, indent=4)
        json_file.write(json_string)

    return json_file


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
