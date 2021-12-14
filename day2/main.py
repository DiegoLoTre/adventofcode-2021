from common.script import get_list


def part_one():
    final_list = get_list(2, 'input.txt')
    horizontal = 0
    depth = 0

    for x in final_list:
        instruction = x.split()

        movement = int(instruction[1])

        if instruction[0] == "forward":
            horizontal = horizontal + movement
        elif instruction[0] == "down":
            depth = depth + movement
        else:
            depth = depth - movement

    print(horizontal * depth)


def part_two():
    final_list = get_list(2, 'input.txt')
    horizontal = 0
    depth = 0
    aim = 0

    for x in final_list:
        instruction = x.split()

        movement = int(instruction[1])

        if instruction[0] == "forward":
            horizontal = horizontal + movement

            depth = depth + (aim * movement)

        elif instruction[0] == "down":
            aim = aim + movement
        else:
            aim = aim - movement

    print(horizontal * depth)
