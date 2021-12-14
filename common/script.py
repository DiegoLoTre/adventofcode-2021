def get_list(day, filename):
    tmp_list = []
    with open('/mnt/d/Python/AdventOfCode/2021/day' + str(day) + "/" + filename) as file:
        for line in file:
            tmp_list.append(str(line.rstrip('\n')))
    return tmp_list
