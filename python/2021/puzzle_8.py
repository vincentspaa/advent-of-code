def sort_pattern(pattern):
    return "".join(sorted(list(pattern)))


def is_subset_of(super_set, sub_set):
    for sub_char in list(sub_set):
        if sub_char not in super_set:
            return False
    return True


def build_translation(unique_signal_patterns: [str], only_use_simple):
    translation_table = {}
    groupings = {}

    for pattern in unique_signal_patterns:
        if len(pattern) in groupings:
            groupings[len(pattern)] = [*groupings[len(pattern)], sort_pattern(pattern)]
        else:
            groupings[len(pattern)] = [sort_pattern(pattern)]

    translation_table[groupings[2][0]] = 1
    translation_table[groupings[4][0]] = 4
    translation_table[groupings[3][0]] = 7
    translation_table[groupings[7][0]] = 8

    if only_use_simple is False:
        # 6 should not be a subset of 1, where 9 and 0 are
        six = list(filter(lambda l: is_subset_of(l, groupings[2][0]) is False, groupings[6]))[0]
        translation_table[six] = 6
        # 9 should be a subset of 4, where 0 is not
        nine = list(filter(lambda l: l != six and is_subset_of(l, groupings[4][0]) is True, groupings[6]))[0]
        translation_table[nine] = 9
        # 0 should be the last character with 6 segments
        zero = list(filter(lambda l: l != six and l != nine, groupings[6]))[0]
        translation_table[zero] = 0
        # 5 should be the only subset of 6, where 3 and 2 are not
        five = list(filter(lambda l: is_subset_of(six, l) is True, groupings[5]))[0]
        translation_table[five] = 5
        # 3 should be a subset of 9, where 2 is not
        three = list(filter(lambda l: l != five and is_subset_of(nine, l) is True, groupings[5]))[0]
        translation_table[three] = 3
        # 2 should be the last character with 5 segments
        two = list(filter(lambda l: l != five and l != three, groupings[5]))[0]
        translation_table[two] = 2

    return translation_table


def main():
    puzzle_input = open("inputs/08.txt", "r")

    part_one = False

    value_counts = {}
    sum_of_output_values = 0

    for line in puzzle_input:
        unique_signal_patterns_line, output_values_line = line.rstrip('\r').rstrip('\n').split('|')
        unique_signal_patterns = list(map(lambda p: p.strip(' '), unique_signal_patterns_line.strip(' ').split(' ')))
        output_values = list(map(lambda p: p.strip(' '), output_values_line.strip(' ').split(' ')))

        translation_table = build_translation(unique_signal_patterns, part_one)

        complete_output = ""
        for output_value in output_values:
            sorted_output_value = sort_pattern(output_value)
            if sorted_output_value in translation_table:
                translation = translation_table[sorted_output_value]
                if translation in value_counts:
                    value_counts[translation] += 1
                else:
                    value_counts[translation] = 1
                complete_output += str(translation)

        if part_one is False:
            sum_of_output_values += int(complete_output)

    if part_one is True:
        print(f"Value counts are {value_counts}, summed: {sum(value_counts.values())}")
    else:
        print(f"Sum of all output values is {sum_of_output_values}")


main()
