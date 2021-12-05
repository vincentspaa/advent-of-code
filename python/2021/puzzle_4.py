class NumberOnBoard:
    left = None
    above = None
    right = None
    below = None
    marked = False

    def __init__(self, number, left=None, above=None):
        self.number = number
        self.left = left
        self.above = above

    def add_right(self, right):
        self.right = right

    def add_below(self, below):
        self.below = below

    def mark(self):
        self.marked = True

    def is_not_marked(self):
        return self.marked is False

    def get_adjacent_marks(self, only_in_direction: str = None):
        def should_count_as_marked(number: 'NumberOnBoard', direction: str):
            is_direction_match = only_in_direction is None or only_in_direction == direction
            return number is not None and is_direction_match and number.marked

        if should_count_as_marked(self.left, 'left'):
            yield self.left, 'left'
        if should_count_as_marked(self.above, 'above'):
            yield self.above, 'above'
        if should_count_as_marked(self.right, 'right'):
            yield self.right, 'right'
        if should_count_as_marked(self.below, 'below'):
            yield self.below, 'below'


def flat_map(xs: list[dict[int, NumberOnBoard]]):
    flattened: [NumberOnBoard] = []
    for ys in xs:
        for y in ys.items():
            flattened.append(y[1])
    return flattened


def get_numbers_from_line(line, separator):
    numbers_raw = line \
        .rstrip('\r') \
        .rstrip('\n') \
        .split(separator)
    without_empties = list(filter(lambda n: n != '', numbers_raw))
    return list(map(lambda n: int(n), without_empties))


def get_numbers_on_board(puzzle_input):
    numbers_on_board: list[dict[int, NumberOnBoard]] = []
    for row_number in range(0, 5):
        numbers_in_row = get_numbers_from_line(puzzle_input.readline(), ' ')

        numbers_on_board.append({})
        current_row = numbers_on_board[row_number]

        for column_number in range(0, len(numbers_in_row)):
            current_number = numbers_in_row[column_number]
            current_row[column_number] = NumberOnBoard(
                current_number,
                None if column_number == 0 else current_row[column_number - 1],
                None if row_number == 0 else numbers_on_board[row_number - 1][column_number])
            if column_number > 0:
                current_row[column_number - 1].right = current_row[column_number]
            if row_number > 0:
                numbers_on_board[row_number - 1][column_number].below = current_row[column_number]

    return flat_map(numbers_on_board)


def makes_bingo(number: NumberOnBoard):
    def count_marks_in_direction(current_number, only_in_direction, mark_count=0):
        for adjacent, direction in current_number.get_adjacent_marks(only_in_direction):
            return count_marks_in_direction(adjacent, direction, mark_count + 1)
        return mark_count

    horizontal_marks = count_marks_in_direction(number, 'left') + count_marks_in_direction(number, 'right') + 1
    vertical_marks = count_marks_in_direction(number, 'above') + count_marks_in_direction(number, 'below') + 1
    return horizontal_marks == 5 or vertical_marks == 5


def get_score_for_board(numbers_on_board: [NumberOnBoard], random_numbers: [int]):
    numbers_needed = 0
    for random_number in random_numbers:
        numbers_needed += 1
        matching_numbers = filter(lambda n: n.number == random_number, numbers_on_board)
        for matching_number in matching_numbers:
            matching_number.mark()
            if makes_bingo(matching_number):
                unmarked = list(map(lambda n: n.number, filter(lambda n: n.is_not_marked(), numbers_on_board)))
                return sum(unmarked) * matching_number.number, numbers_needed


def print_board(numbers_on_board):
    for index in range(0, len(numbers_on_board)):
        if (index % 5) == 0:
            print('\n')
        number = numbers_on_board[index]
        print(number.number if number.is_not_marked() else 'X', end='')
        print('\t', end='')
    print('\n')


def main():
    puzzle_input = open("inputs/03.txt", "r")
    random_numbers = get_numbers_from_line(puzzle_input.readline(), ',')

    lowest_numbers_needed = 9000
    the_fastest_score = -1
    most_numbers_needed = -1
    the_slowest_score = -1

    while puzzle_input.readline() != '':
        numbers_on_board = get_numbers_on_board(puzzle_input)

        score, numbers_needed = get_score_for_board(numbers_on_board, random_numbers)
        print_board(numbers_on_board)
        print(f"Needed {numbers_needed} numbers to get score of {score}")

        if lowest_numbers_needed > numbers_needed:
            lowest_numbers_needed = numbers_needed
            the_fastest_score = score
        if most_numbers_needed < numbers_needed:
            most_numbers_needed = numbers_needed
            the_slowest_score = score

    print("\n\n\n")
    print("***********************************************************************************************")
    print(f"Least amount of numbers needed was {lowest_numbers_needed} to get score of {the_fastest_score}")
    print(f"Most amount of numbers needed was {most_numbers_needed} to get score of {the_slowest_score}")
    print("***********************************************************************************************")


main()
