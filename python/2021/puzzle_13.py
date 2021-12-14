class Dot:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return self.x != other.x or self.y != other.y


class FoldInstruction:
    def __init__(self, axis, value):
        self.axis = axis
        self.value = value


def print_dots(dots):
    max_x = max(map(lambda p: p.x, dots))
    max_y = max(map(lambda p: p.y, dots))

    for y in range(0, max_y + 1):
        for x in range(0, max_x + 1):
            if Dot(x, y) in dots:
                print('#', end='')
            else:
                print('.', end='')
        print('\n', end='')


def main():
    puzzle_input = open("inputs/13.txt", "r")

    part_one = False

    dots = []
    fold_instructions = []

    for line in puzzle_input:
        clean_line = line.rstrip('\r').rstrip('\n')
        if line.startswith("fold"):
            axis, value = clean_line.replace("fold along ", "").split('=')
            fold_instructions.append(FoldInstruction(axis, int(value)))
        elif "," in line:
            x, y = clean_line.split(',')
            dots.append(Dot(int(x), int(y)))

    for fold_instruction in fold_instructions:
        for dot in list(dots):
            new_dot = None
            if fold_instruction.axis == 'x' and dot.x > fold_instruction.value:
                new_dot = Dot(dot.x - ((dot.x - fold_instruction.value) * 2), dot.y)
            elif fold_instruction.axis == 'y' and dot.y > fold_instruction.value:
                new_dot = Dot(dot.x, dot.y - ((dot.y - fold_instruction.value) * 2))

            if new_dot is not None:

                dots.remove(dot)
                if new_dot not in dots:
                    dots.append(new_dot)

        if part_one is True:
            break

    if part_one is True:
        print(f"Dots left: {len(dots)}")
    else:
        print_dots(dots)


main()
