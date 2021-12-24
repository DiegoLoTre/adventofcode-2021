from math import ceil, floor

from common.script import get_list


class LineCorrupted(Exception):
    close_elements = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137
    }
    expected_value = 0

    def __init__(self, expected, found):
        print("Expected " + expected + ", but found " + found + " instead")
        self.expected_value = self.close_elements[found]


open_elements = ["[", "(", "{", "<"]
close_elements = {
    "[": "]",
    "(": ")",
    "{": "}",
    "<": ">"
}
open_elements_value = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4
}


def verify_line(line):
    stack = []

    for element in line:
        if element in open_elements:
            stack.append(element)
        else:
            opened_element = stack.pop()
            if element != close_elements[opened_element]:
                raise LineCorrupted(close_elements[opened_element], element)
    return


def complete_line(line):
    stack = []

    for element in line:
        if element in open_elements:
            stack.append(element)
        else:
            opened_element = stack.pop()
            if element != close_elements[opened_element]:
                raise LineCorrupted(close_elements[opened_element], element)

    response = 0
    while len(stack) > 0:
        element = stack.pop()
        response = (response * 5) + open_elements_value[element]

    return response


def part_one():
    response = 0

    for line in get_list(10, 'input.txt'):
        try:
            verify_line(list(line))
        except LineCorrupted as e:
            response += e.expected_value

    return response


def part_two():
    response = []
    for line in get_list(10, 'input.txt'):
        try:
            response.append(complete_line(list(line)))
        except LineCorrupted as e:
            pass

    response = sorted(response)

    return response[floor(len(response) / 2)]
