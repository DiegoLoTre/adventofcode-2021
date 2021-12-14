import sys

from common.script import get_list


def part_one():
    final_list = get_list(1, 'input.txt')
    counter = 0
    prev = sys.maxsize

    for line in final_list:
        current = int(line)

        if current > prev:
            counter = counter + 1

        prev = int(line)

    print(counter)


def part_two():
    final_list = get_list(1, 'input.txt')
    prev = final_list[0] + final_list[1] + final_list[2]
    index = 3
    counter = 0

    for x in final_list[3:]:
        current = final_list[index - 2] + final_list[index - 1] + final_list[index]

        if current > prev:
            counter = counter + 1

        prev = current
        index = index + 1

    print(counter)
