class Octopus:
    line_index = 0
    point_index = 0

    def __init__(self, line_index, point_index):
        self.line_index = line_index
        self.point_index = point_index

    def __eq__(self, other):
        return self.line_index == other.line_index and self.point_index == other.point_index

    def __ne__(self, other):
        return self.line_index != other.line_index or self.point_index != other.point_index


def check_flash_recursively(current_octopus, octopuses, increase_energy=False):
    flashes = 0

    energy = octopuses[current_octopus.line_index][current_octopus.point_index]
    increased_beyond_ten = False
    if increase_energy is True and energy < 10:
        energy += 1
        if energy == 10:
            energy += 1
            increased_beyond_ten = True
        octopuses[current_octopus.line_index][current_octopus.point_index] = energy

    if (increase_energy is False and energy == 10) or increased_beyond_ten is True:
        flashes += 1

        octopuses_to_check = [
            Octopus(current_octopus.line_index - 1, current_octopus.point_index),  # Top
            Octopus(current_octopus.line_index - 1, current_octopus.point_index + 1),  # Top, Right
            Octopus(current_octopus.line_index, current_octopus.point_index + 1),  # Right
            Octopus(current_octopus.line_index + 1, current_octopus.point_index + 1),  # Bottom, Right
            Octopus(current_octopus.line_index + 1, current_octopus.point_index),  # Bottom
            Octopus(current_octopus.line_index + 1, current_octopus.point_index - 1),  # Bottom, Left
            Octopus(current_octopus.line_index, current_octopus.point_index - 1),  # Left
            Octopus(current_octopus.line_index - 1, current_octopus.point_index - 1),  # Top, Left
        ]

        for to_check in octopuses_to_check:
            positive = to_check.line_index >= 0 and to_check.point_index >= 0
            in_bounds = to_check.line_index < len(octopuses) and to_check.point_index < len(octopuses[0])
            if positive and in_bounds:
                flashes += check_flash_recursively(to_check, octopuses, increase_energy=True)

    return flashes


def print_octopuses(octopuses):
    for line_index in range(0, len(octopuses)):
        for point_index in range(0, len(octopuses[line_index])):
            display_value = octopuses[line_index][point_index]
            if display_value == 10:
                display_value = '*'
            if display_value == 11:
                display_value = '^'
            print(display_value, end='')
        print('\n', end='')


def main():
    puzzle_input = open("inputs/11.txt", "r")

    part_one = False

    octopuses = []
    total_octopuses = 0

    for line in puzzle_input:
        from_line = list(map(lambda c: int(c), list(line.rstrip('\r').rstrip('\n'))))
        octopuses.append(from_line)
        total_octopuses += len(from_line)

    total_flashes = 0
    sync_step = -1

    print_octopuses(octopuses)
    print(f"Before any steps")

    for step in range(1, 801):
        total_resets = 0

        for line_index in range(0, len(octopuses)):
            for point_index in range(0, len(octopuses[line_index])):
                current_energy = octopuses[line_index][point_index]
                if current_energy >= 10:
                    total_resets += 1
                    current_energy = 0
                octopuses[line_index][point_index] = current_energy + 1

        if total_resets == total_octopuses and sync_step == -1:
            sync_step = step - 1

        for line_index in range(0, len(octopuses)):
            for point_index in range(0, len(octopuses[line_index])):
                total_flashes += check_flash_recursively(Octopus(line_index, point_index), octopuses)

        print_octopuses(octopuses)
        print(f"After step {step}, {total_flashes} flashes")

    if part_one is False:
        print(f"Octopuses synced for the first time at step {sync_step}")


main()
