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


def make_numpy_array(array):
    data = []
    for row in array:
        data.append(np.array(row))
    return data


def tree_and_query(data):
    tree = KDTree(data)
    nearest_dist, nearest_ind = tree.query(data, k=2)
    print(nearest_dist[:, 1])
    print(nearest_ind[:, 1])


def main():
    data = read_data_from_file()
    data = make_numpy_array(data)
    pprint(data)
    tree_and_query(data)
    # y = get_function_from_row(data)


if __name__ == '__main__':
    main()
