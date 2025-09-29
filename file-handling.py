import csv
import json
import os


# TXT ________________________________________________
def read_text_file(source):
    print(f"lines from {source}")
    with open(source, "r") as file:
        lines = file.read()
    # print(f"{source} closed successully")
    return lines


# CSV ________________________________________________
def read_csv_to_dicts(filepath):
    records = []
    #  r mode opens for reading
    with open(filepath, "r", newline="") as csvfile:
        # dictreader means first row is keys, subsequent rows are values
        reader = csv.DictReader(csvfile)
        for row in reader:
            records.append(row)
    return records


def transform_to_int(records):
    for record in records:
        record["score"] = int(record["score"])
    return records


# JSON ________________________________________________
from data.user_profile import user_profile


def parse_and_write_json():
    # read json from a file
    with open("data/user.json", "w") as outfile:
        json.dump(user_profile, outfile, indent=4)
        print("data written to output.json.")
    with open("data/user.json", "r") as infile:
        print("...")
        print("loading output.json")
        print("...")
        user_data = json.load(infile)
        print(user_data["name"])
        print("...")
        print("printed user data... check it out")


# CSV to JSON ________________________________________________


def csv_to_json(filepath):
    records = []
    with open(filepath, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            records.append(row)
        # returns dictionary
    # convert dictionary to JSON string
    json_string = records

    with open("data/output2.json", "w") as outfile:
        json.dump(json_string, outfile, indent=4)
        print("data written to output2.json")


# MAIN ________________________________________________
def main():

    text = read_text_file("data/notes.txt")
    print(text)

    csv = read_csv_to_dicts("data/students.csv")
    int_csv = transform_to_int(csv)
    greater_than_80_int_csv = [s for s in int_csv if s["score"] > 80]
    # higher_than_80_csv = [c for c in csv if int(c["score"]) > 80]
    print(greater_than_80_int_csv)
    # print(higher_than_80_csv)
    # print(csv)

    parse_and_write_json()

    csv_to_json('data/students.csv')


# runs it! ________________________________________________
if __name__ == "__main__":
    main()
