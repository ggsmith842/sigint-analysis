import json
import csv

def csv_to_json(csv_file_path, json_file_path):

    with open(csv_file_path, 'r', encoding="utf-8") as csvf:

        #load csv file data using csv lib
        csvReader = csv.DictReader(csvf)

        json_array = [row for row in csvReader]


    with open(json_file_path, "w", encoding="utf-8") as jsonf:
        jsonString = json.dumps(json_array, ensure_ascii=False,indent=4)
        jsonf.write(jsonString)

csv_to_json("./transcripts.csv", "./transcripts.json")
