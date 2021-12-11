import math


def main():
    puzzle_input = open("inputs/10.txt", "r")

    part_one = False

    illegals = []
    missings = []

    for line in puzzle_input:
        chunk_boundaries = list(map(lambda c: c, list(line.rstrip('\r').rstrip('\n'))))

        opening_char_map = {'(': ')', '[': ']', '{': '}', '<': '>'}
        expecting_closing_char_stack = []
        has_illegal = False

        for boundary in chunk_boundaries:
            if boundary in opening_char_map:
                expecting_closing_char_stack.insert(0, opening_char_map[boundary])
            else:
                if boundary == expecting_closing_char_stack[0]:
                    expecting_closing_char_stack.pop(0)
                else:
                    if part_one is True:
                        print(f"Illegal line, expected {expecting_closing_char_stack[0]} but found {boundary}")
                    illegals.append(boundary)
                    has_illegal = True
                    break

        if has_illegal is False:
            missings.append(expecting_closing_char_stack)

    if part_one is True:
        score_count = 0
        score_map = {')': 3, ']': 57, '}': 1197, '>': 25137}
        for illegal in illegals:
            score_count += score_map[illegal]
        print(score_count)
    else:
        scores = []
        score_map = {')': 1, ']': 2, '}': 3, '>': 4}
        for missing in missings:
            score_count = 0
            for char in missing:
                score_count *= 5
                score_count += score_map[char]
            scores.append(score_count)
        sorted_scores = list(sorted(scores))
        print(sorted_scores[math.floor(len(scores) / 2)])


main()
