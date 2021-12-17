from common.script import get_list


def part_one():
    file_list = get_list(7, 'input.txt')
    final_list = [int(x) for x in file_list[0].split(",")]
    movement_cost = []

    for final_position in range(min(final_list), max(final_list) + 1):
        cost = 0
        for submarine_position in final_list:
            cost = cost + (max(final_position, submarine_position) - min(final_position, submarine_position))

        movement_cost.append(cost)

    return min(movement_cost)


def part_two():
    file_list = get_list(7, 'input.txt')
    final_list = [int(x) for x in file_list[0].split(",")]
    movement_cost = []

    for final_position in range(min(final_list), max(final_list) + 1):
        cost = 0
        for submarine_position in final_list:
            distance = abs(final_position - submarine_position)
            cost = cost + sum(range(0, distance + 1))

        movement_cost.append(cost)

    return min(movement_cost)
