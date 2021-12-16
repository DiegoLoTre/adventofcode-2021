import pandas as pd

from common.script import get_list


def get_board_size(final_list):
    x = 0
    y = 0

    for item in final_list:
        coordinates = item.split(" -> ")
        point1 = coordinates[0].split(',')
        point2 = coordinates[1].split(',')

        if int(point1[0]) > x: x = int(point1[0])
        if int(point2[0]) > x: x = int(point2[0])

        if int(point1[1]) > y: y = int(point1[1])
        if int(point2[1]) > y: y = int(point2[1])

    return x, y


def part_one():
    final_list = get_list(5, 'input.txt')

    row_size, column_size = get_board_size(final_list)

    df = pd.DataFrame(0, index=range(0, row_size + 1), columns=range(0, column_size + 1))

    for x in final_list:
        coordinates = x.split(" -> ")
        point1 = coordinates[0].split(',')
        point2 = coordinates[1].split(',')

        x1 = int(point1[0])
        y1 = int(point1[1])

        x2 = int(point2[0])
        y2 = int(point2[1])

        if x1 == x2:
            for cursor in range(min(y1, y2), max(y1, y2) + 1):
                df[x1][cursor] += 1

        if y1 == y2:
            for cursor in range(min(x1, x2), max(x1, x2) + 1):
                df[cursor][y1] += 1

    return sum(df[df >= 2].count())


def part_two():
    final_list = get_list(5, 'input.txt')

    row_size, column_size = get_board_size(final_list)

    df = pd.DataFrame(0, index=range(0, row_size + 1), columns=range(0, column_size + 1))

    for x in final_list:
        coordinates = x.split(" -> ")
        point1 = coordinates[0].split(',')
        point2 = coordinates[1].split(',')

        x1 = int(point1[0])
        y1 = int(point1[1])

        x2 = int(point2[0])
        y2 = int(point2[1])

        if x1 == x2:
            for cursor in range(min(y1, y2), max(y1, y2) + 1):
                df[x1][cursor] += 1
        elif y1 == y2:
            for cursor in range(min(x1, x2), max(x1, x2) + 1):
                df[cursor][y1] += 1
        else:
            distance = max(x1, x2) - min(x1, x2)
            move_in_x = 1
            move_in_y = 1
            if x1 > x2: move_in_x = -1
            if y1 > y2: move_in_y = -1

            for movement in range(0, distance + 1):
                df[x1 + (movement * move_in_x)][y1 + (movement * move_in_y)] += 1

    return sum(df[df >= 2].count())
