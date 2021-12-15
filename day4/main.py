from common.script import get_list


class Board:
    def __init__(self):
        self.data = []
        self.marked = []

    def add_row(self, information):
        self.data.append(information)
        self.marked.append([True] * len(information))

    def remove_number(self, number):
        for row, x in enumerate(self.data):
            for column, y in enumerate(x):
                if y == number:
                    self.data[row][column] = 0
                    self.marked[row][column] = False

                    if self.win():
                        return True

        return False

    def get_unmarked_sum(self):
        return sum(sum(self.data, []))

    def win(self):
        # Review rows
        for value in self.marked:
            if sum(value) == 0:
                return True

        # Review columns
        for value in zip(*self.marked):
            if sum(value) == 0:
                return True


def fill_boards(final_list):
    bingo_boards = []

    board = None

    for x in final_list:
        if x == "":
            board = Board()
            bingo_boards.append(board)
            continue

        board.add_row(list(map(int, x.split())))

    return bingo_boards


def play_bingo(bingo_boards, bingo_numbers):
    for x in bingo_numbers:
        for board in bingo_boards:
            if board.remove_number(x):
                return x, board


def lose_bingo(bingo_boards, bingo_numbers):
    flag_index = []
    board = None
    for index1, x in enumerate(bingo_numbers):
        for index, board in enumerate(bingo_boards):
            if board.remove_number(x):
                flag_index.insert(0, index)

        if flag_index is not None:
            for index in flag_index:
                bingo_boards.pop(index)
            flag_index = []

        if len(bingo_boards) == 0:
            return x, board


def part_one():
    final_list = get_list(4, 'input.txt')

    bingo_numbers = list(map(int, final_list[0].split(",")))

    bingo_boards = fill_boards(final_list[1:])
    winner_number, winner_board = play_bingo(bingo_boards, bingo_numbers)

    return winner_number * winner_board.get_unmarked_sum()


def part_two():
    final_list = get_list(4, 'input.txt')

    bingo_numbers = list(map(int, final_list[0].split(",")))

    bingo_boards = fill_boards(final_list[1:])
    winner_number, winner_board = lose_bingo(bingo_boards, bingo_numbers)

    return winner_number * winner_board.get_unmarked_sum()
