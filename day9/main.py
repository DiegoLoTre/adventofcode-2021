import numpy
import pandas as pd

from common.script import get_list

pd.options.mode.chained_assignment = None  # default='warn'


def item_is_lower(array, x, y, item):
    if y > 0 and array[x][y - 1] <= item:
        return False

    if x > 0 and array[x - 1][y] <= item:
        return False

    if y < len(array) - 1 and array[x][y + 1] <= item:
        return False

    if x < len(array) - 1 and array[x + 1][y] <= item:
        return False

    return True


def part_one():
    array = []
    response = []
    for line in get_list(9, 'input.txt'):
        array.append([int(i) for i in line])

    for x, row in enumerate(array):
        for y, item in enumerate(row):
            if item_is_lower(array, x, y, item):
                response.append(item + 1)

    return sum(response)


class Algorith:

    def __init__(self, array):
        self.df = pd.DataFrame(array)
        self.lowest_spots_positions = []
        self.basin = []

    def item_is_lower(self, x, y, item):
        if y > 0 and self.df[x][y - 1] <= item:
            return False

        if x > 0 and self.df[x - 1][y] <= item:
            return False

        if y < len(self.df) - 1 and self.df[x][y + 1] <= item:
            return False

        if x < len(self.df.columns) - 1 and self.df[x + 1][y] <= item:
            return False

        return True

    def find_lowest_spots(self):
        for y, row in self.df.iterrows():
            for x, item in enumerate(row):
                if self.item_is_lower(x, y, item):
                    self.lowest_spots_positions.append([x, y])

    def get_basin_size(self, x, y):
        top = 0
        right = 0
        left = 0
        bottom = 0

        self.df[x][y] = None

        if x > 0 and self.df[x - 1][y] != 9 and pd.notna(self.df[x - 1][y]):
            left = self.get_basin_size(x - 1, y)

        if y < len(self.df) - 1 and self.df[x][y + 1] != 9 and pd.notna(self.df[x][y + 1]):
            bottom = self.get_basin_size(x, y + 1)

        if y > 0 and self.df[x][y - 1] != 9 and pd.notna(self.df[x][y - 1]):
            top = self.get_basin_size(x, y - 1)

        if x < len(self.df.columns) - 1 and self.df[x + 1][y] != 9 and pd.notna(self.df[x + 1][y]):
            right = self.get_basin_size(x + 1, y)

        return top + right + left + bottom + 1

    def find_basins(self):
        for item in self.lowest_spots_positions:
            self.basin.append(self.get_basin_size(item[0], item[1]))

    def purge_basins(self):
        self.basin = sorted(self.basin)[-3:]


def part_two():
    array = []
    for line in get_list(9, 'input.txt'):
        array.append([int(i) for i in line])

    algorith = Algorith(array)
    algorith.find_lowest_spots()
    algorith.find_basins()
    algorith.purge_basins()

    return numpy.prod(algorith.basin)
