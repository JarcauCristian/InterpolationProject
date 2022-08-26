import csv
from pprint import pprint


def main():
    with open("data.csv", 'r') as csv_in:
        csv_reader = csv.reader(csv_in)
        data = []
        for row in csv_reader:
            data.append(row[8:])
        data.pop(0)
    pprint(data)


if __name__ == '__main__':
    main()
