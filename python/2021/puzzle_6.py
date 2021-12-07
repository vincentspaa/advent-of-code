def add_fish(lantern_fish, count, all_fish):
    if lantern_fish in all_fish:
        all_fish[lantern_fish] += count
    else:
        all_fish[lantern_fish] = count


def main():
    puzzle_input = open("inputs/06.txt", "r")

    fish_count = 0
    all_fish = {}
    lantern_fishes = map(lambda n: int(n), puzzle_input.readline().rstrip('\r').rstrip('\n').split(','))

    for lantern_fish in lantern_fishes:
        add_fish(lantern_fish, 1, all_fish)
        fish_count += 1

    for day in range(1, 257):
        new_fish = all_fish[0] if 0 in all_fish else 0
        all_fish[0] = 0

        for lantern_fish in range(1, 9):
            if lantern_fish in all_fish:
                all_fish[lantern_fish - 1] = all_fish[lantern_fish]
                all_fish[lantern_fish] = 0

        if new_fish > 0:
            add_fish(8, new_fish, all_fish)
            add_fish(6, new_fish, all_fish)
            fish_count += new_fish

        print(f"After {day} {'days' if day > 1 else 'day'}, there are a total of {fish_count} fish")


main()
