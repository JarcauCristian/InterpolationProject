import csv
from pprint import pprint
from time import sleep
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d
from sklearn.neighbors import KDTree


def read_data_from_file():
    with open("data.csv", 'r') as csv_in:
        csv_reader = csv.reader(csv_in)
        data = []
        for row in csv_reader:
            data.append(row[8:])
        data.pop(0)
    for row in data:
        for i, value in enumerate(row):
            if row[i] == '':
                # noinspection PyTypeChecker
                row[i] = 0
            else:
                # noinspection PyTypeChecker
                row[i] = float(value)
    pprint(data)
    return data


def get_function_from_row(data):
    y = []
    for row in data:
        y.append(list(-np.array(row)/3.0))
    pprint(y)
    return y


def interpolate_1d(x, y):
    for i, j in zip(x, y):
        f = interp1d(i, j)
        x_new = np.arange(0, 10000, 100)
        y_new = f(x_new)
        plt.plot(i, j, 'o', x_new, y_new, '-')
        plt.show()
        sleep(5)


def main():
    data = read_data_from_file()
    print('\n')
    y = get_function_from_row(data)


if __name__ == '__main__':
    main()
