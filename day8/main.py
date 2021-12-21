from common.script import get_list


def part_one():
    counter = 0
    for line in get_list(8, 'input.txt'):
        output_value = (line.split(" | "))[1].split(" ")

        for digit in output_value:
            length = len(list(digit))
            if 2 == length or 4 == length or 3 == length or 7 == length:
                counter += 1

    return counter


class Decode:
    number_dict = {}
    letter_dict = {}

    def __init__(self, input):
        self.number_dict = {}
        self.letter_dict = {}
        while len(input) > 0:
            string = input.pop(0)

            if not self.find_number(string):
                input.append(string)

    def find_number(self, string):
        size = len(list(string))
        if 2 == size:
            self.add_to_dict(1, string)
            return True
        elif 3 == size:
            self.add_to_dict(7, string)
            return True
        elif 4 == size:
            self.add_to_dict(4, string)
            return True
        elif 7 == size:
            self.add_to_dict(8, string)
            return True

        # 2,3,5
        elif 5 == size:
            if self.number_dict.get(8) is not None and self.number_dict.get(9) is not None:
                key_letter = set(self.number_dict.get(8)) - set(self.number_dict.get(9))
                if self.not_contains(string, 1) and list(key_letter)[0] in list(string):
                    self.add_to_dict(2, string)
                    return True

            if self.contains(string, 1):
                self.add_to_dict(3, string)
                return True

            if self.number_dict.get(8) is not None and self.number_dict.get(9) is not None:
                key_letter = set(self.number_dict.get(8)) - set(self.number_dict.get(9))
                if self.not_contains(string, 1) and list(key_letter)[0] not in list(string):
                    self.add_to_dict(5, string)
                    return True

        # 0,6,9
        elif 6 == size:
            if self.contains(string, 1) and self.not_contains(string, 4):
                self.add_to_dict(0, string)
                return True

            if self.not_contains(string, 1):
                self.add_to_dict(6, string)
                return True

            if self.contains(string, 4):
                self.add_to_dict(9, string)
                return True

        return False

    def contains(self, original, must_have):
        if self.number_dict.get(must_have) is None:
            return False

        return set(list(self.number_dict.get(must_have))).issubset(list(original))

    def not_contains(self, original, must_have):
        tmp = self.number_dict.get(must_have)
        if tmp is None:
            return False

        return set(tmp) - set(original) != set()

    def add_to_dict(self, number, string):
        string = ''.join(sorted(list(string)))
        self.number_dict.update({number: string})
        self.letter_dict.update({string: number})

    def decode(self, output_value):
        response = []
        for item in output_value:
            order = ''.join(sorted(list(item)))
            response.append(str(self.letter_dict.get(order)))
        return ''.join(response)


def part_two():
    output_values = []
    for line in get_list(8, 'input.txt'):
        line = line.split(" | ")

        output_values.append(
            int(
                Decode(
                    line[0].split(" ")
                ).decode(
                    line[1].split(" ")
                )
            )
        )

    return sum(output_values)


letter_dict = {
    "a": ["a", "b", "c", "d", "e", "f", "g"]
}
