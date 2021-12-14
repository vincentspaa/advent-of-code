class Cave:

    def __init__(self, name, is_big):
        self.name = name
        self.is_big = is_big
        self.connected_caves = []

    def add_connected_cave(self, other_cave):
        if other_cave not in self.connected_caves:
            self.connected_caves.append(other_cave)


def recursively_visit(current: Cave, path: [Cave], small_cave_visit_allowance):
    path_with_current = [*path, current]

    if current.name == 'end':
        yield path_with_current
    else:
        for connected_cave in current.connected_caves:
            if connected_cave.name == 'start':
                continue

            should_visit_small = connected_cave not in path or (small_cave_visit_allowance > 0)
            should_visit = connected_cave.is_big is True or should_visit_small

            new_small_cave_visit_allowance = small_cave_visit_allowance \
                if connected_cave.is_big is True or connected_cave not in path \
                else small_cave_visit_allowance - 1

            if should_visit:
                for new_path in recursively_visit(connected_cave, path_with_current, new_small_cave_visit_allowance):
                    yield new_path


def add_cave(caves, cave_name):
    if cave_name not in caves:
        new_cave = Cave(cave_name, True if str.isupper(cave_name) else False)
        caves[cave_name] = new_cave
        return new_cave
    return caves[cave_name]


def main():
    puzzle_input = open("inputs/12.txt", "r")

    part_one = False

    caves = {'start': Cave('start', False), 'end': Cave('end', False)}

    for line in puzzle_input:
        from_cave_name, to_cave_name = line.rstrip('\r').rstrip('\n').split('-')
        from_cave = add_cave(caves, from_cave_name)
        to_cave = add_cave(caves, to_cave_name)
        from_cave.add_connected_cave(to_cave)
        to_cave.add_connected_cave(from_cave)

    small_cave_visit_allowance = 0 if part_one is True else 1
    paths = list(recursively_visit(caves['start'], [], small_cave_visit_allowance))

    for path in paths:
        print(str.join(",", map(lambda p: p.name, path)))

    print(f"{len(paths)} possible paths")


main()
