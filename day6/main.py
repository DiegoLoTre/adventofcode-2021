import pandas as pd

from common.script import get_list


def part_one():
    file_list = get_list(6, 'input.txt')
    final_list = [int(x) for x in file_list[0].split(",")]

    for day in range(0, 80):
        list_length = len(final_list)
        for item in range(0, list_length):
            final_list[item] -= 1
            if final_list[item] == -1:
                final_list[item] = 6
                final_list.append(8)

    return len(final_list)


def part_two():
    file_list = get_list(6, 'input.txt')
    current_fish = [0] * 7
    new_fish = [0] * 9

    for x in file_list[0].split(","):
        current_fish[int(x)] += 1

    for day in range(1, 257):
        tmp = current_fish.pop(0)
        to_add = new_fish.pop(0)

        current_fish.append(to_add + tmp)
        new_fish.append(to_add + tmp)

    return sum(current_fish) + sum(new_fish)
