input_file_name = "inputs/02.txt"


def get_most_and_least_common_at(input_lines, index):
    zero_value_count = 0
    one_value_count = 0

    for line in input_lines:
        if line[index] == '1':
            one_value_count = one_value_count + 1
        else:
            zero_value_count = zero_value_count + 1

    return ('1' if one_value_count >= zero_value_count else '0'), ('0' if one_value_count >= zero_value_count else '1')


def main():
    puzzle_input = open(input_file_name, "r")

    oxygen_generator_rating_lines = []
    co2_scrubber_rating_lines = []

    for line in puzzle_input:
        trimmed = line.rstrip('\r').rstrip('\n')
        oxygen_generator_rating_lines.append(trimmed)
        co2_scrubber_rating_lines.append(trimmed)

    for index in range(0, len(oxygen_generator_rating_lines[0])):
        most_common, least_common = get_most_and_least_common_at(oxygen_generator_rating_lines, index)
        if index > 0:
            _, least_common = get_most_and_least_common_at(co2_scrubber_rating_lines, index)

        if len(oxygen_generator_rating_lines) > 1:
            for oxygen_line in oxygen_generator_rating_lines.copy():
                if oxygen_line[index] != most_common:
                    oxygen_generator_rating_lines.remove(oxygen_line)

        if len(co2_scrubber_rating_lines) > 1:
            for co2_line in co2_scrubber_rating_lines.copy():
                if co2_line[index] != least_common:
                    co2_scrubber_rating_lines.remove(co2_line)

    oxygen_generator_rating = int(oxygen_generator_rating_lines[0], 2)
    co2_scrubber_rating = int(co2_scrubber_rating_lines[0], 2)

    print(oxygen_generator_rating * co2_scrubber_rating)


main()
