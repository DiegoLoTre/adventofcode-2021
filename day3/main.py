from math import ceil

from common.script import get_list


def part_one():
    final_list = get_list(3, 'input.txt')
    tmp = [0] * len(list(final_list[0]))

    gamma = ''
    epsilon = ''

    for x in final_list:
        for index, item in enumerate(list(x)):
            tmp[index] += int(item)

    for x in tmp:
        if x > ceil(len(final_list) / 2):
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'

    return int(gamma, 2) * int(epsilon, 2)


def get_common(oxygen, position, length):
    tmp_sum = 0
    for item in oxygen:
        tmp_sum += int(list(item)[position])

    if tmp_sum >= length:
        return 1
    else:
        return 0


def part_two():
    final_list = get_list(3, 'input.txt')

    oxygen = final_list
    scrubber = final_list

    position = 0
    while len(oxygen) > 1:
        common = get_common(oxygen, position, ceil(len(oxygen) / 2))
        tmp = []

        for x in oxygen:
            if int(list(x)[position]) == common:
                tmp.append(x)

        oxygen = tmp
        position += 1

    position = 0
    while len(scrubber) > 1:
        common = get_common(scrubber, position, ceil(len(scrubber) / 2))

        tmp = []

        for x in scrubber:
            if int(list(x)[position]) != common:
                tmp.append(x)

        scrubber = tmp
        position += 1

    decimal_o = int(oxygen[0], 2)
    decimal_s = int(scrubber[0], 2)

    return decimal_s * decimal_o
