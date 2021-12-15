class SplitAction:
    def __init__(self, pair, insert, pair_count, matches_starting_pair):
        self.pair = pair
        self.insert = insert
        self.pair_count = pair_count
        self.matches_starting_pair = matches_starting_pair


class Template:
    def __init__(self):
        self.template_pairs = {}
        self.starting_pair = None

    def add_pair(self, pair, count):
        if self.starting_pair is None:
            self.starting_pair = pair
            count -= 1
            if count == 0:
                return

        if pair in self.template_pairs:
            self.template_pairs[pair] += count
        else:
            self.template_pairs[pair] = count

    def remove_pair(self, pair, pair_count, consider_starting_pair):
        if consider_starting_pair is True:
            self.starting_pair = None
            pair_count -= 1
        if pair in self.template_pairs:
            self.template_pairs[pair] -= pair_count

    def get_split_action(self, pattern, insert):
        count = 0
        matches_starting_pair = False

        if pattern in self.template_pairs:
            count += self.template_pairs[pattern]
        if pattern == self.starting_pair:
            count += 1
            matches_starting_pair = True

        return None if count == 0 else SplitAction(pattern, insert, count, matches_starting_pair)

    def execute_split_action(self, action: SplitAction):
        self.remove_pair(action.pair, action.pair_count, action.matches_starting_pair)
        self.add_pair(action.pair[0] + action.insert, action.pair_count)
        self.add_pair(action.insert + action.pair[1], action.pair_count)

    def get_char_counts(self):
        counts = {}

        def add_count(counting_char, value):
            if counting_char in counts:
                counts[counting_char] += value
            else:
                counts[counting_char] = value

        for pair in self.template_pairs.keys():
            add_count(pair[1], self.template_pairs[pair])

        add_count(self.starting_pair[0], 1)
        add_count(self.starting_pair[1], 1)
        return counts.values()


def apply_rules(template: Template, rules):
    actions = []
    for pattern in rules.keys():
        split_action = template.get_split_action(pattern, rules[pattern])
        if split_action is not None:
            actions.append(split_action)

    for action in actions:
        template.execute_split_action(action)


def main():
    puzzle_input = open("inputs/14.txt", "r")

    part_one = False

    rules = {}
    template_list = list(puzzle_input.readline().rstrip('\r').rstrip('\n'))
    template = Template()

    for index in range(0, len(template_list) - 1):
        template.add_pair(template_list[index] + template_list[index + 1], 1)

    puzzle_input.readline()

    for line in puzzle_input:
        clean_line = line.rstrip('\r').rstrip('\n')
        pattern, insertion = clean_line.split(' -> ')
        rules[pattern] = insertion

    max_steps = 11 if part_one is True else 41
    for step in range(1, max_steps):
        print(f"Step {step}")
        apply_rules(template, rules)

    char_counts = template.get_char_counts()
    most_common_count = max(char_counts)
    least_common_count = min(char_counts)
    print(f"{most_common_count} - {least_common_count} = {most_common_count - least_common_count}")


main()
