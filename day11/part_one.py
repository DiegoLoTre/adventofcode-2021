import numpy as np
import pandas as pd

pd.options.mode.chained_assignment = None  # default='warn'

response = 0


# Increase by one and return if flashed
def increase(x, y):
    global response

    if data[x][y] is not np.nan:
        data[x][y] = data[x][y] + 1

    if 10 == data[x][y]:
        data[x][y] = np.nan
        response += 1
        return True

    return False


def flash_near(x, y):
    if y > 0:
        if x > 0:
            if increase(x - 1, y - 1):
                flash_near(x - 1, y - 1)

        if increase(x, y - 1):
            flash_near(x, y - 1)

        if x < len(data.columns) - 1:
            if increase(x + 1, y - 1):
                flash_near(x + 1, y - 1)

    if x > 0:
        if increase(x - 1, y):
            flash_near(x - 1, y)

    if x < len(data.columns) - 1:
        if increase(x + 1, y):
            flash_near(x + 1, y)

    if y < len(data) - 1:
        if x > 0:
            if increase(x - 1, y + 1):
                flash_near(x - 1, y + 1)

        if increase(x, y + 1):
            flash_near(x, y + 1)

        if x < len(data.columns) - 1:
            if increase(x + 1, y + 1):
                flash_near(x + 1, y + 1)


data = pd.read_fwf('day11/input.txt',
                   widths=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                   header=None)

for step in range(100):

    for row in range(10):
        for column in range(10):
            if increase(column, row):
                flash_near(column, row)

    data = data.fillna(0)
