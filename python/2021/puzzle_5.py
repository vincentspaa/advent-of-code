class Point:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y


def convert_to_point(coordinate_set):
    numbers = list(map(lambda c: int(c), coordinate_set.split(',')))
    return Point(numbers[0], numbers[1])


def get_points_in_between(from_point, to_point):
    delta_x = 0 if from_point.x == to_point.x else \
        -1 if from_point.x > to_point.x else 1
    delta_y = 0 if from_point.y == to_point.y else \
        -1 if from_point.y > to_point.y else 1
    current_x = from_point.x
    current_y = from_point.y

    yield Point(current_x, current_y)

    while current_x != to_point.x or current_y != to_point.y:
        current_x += delta_x
        current_y += delta_y

        yield Point(current_x, current_y)


def print_ocean_floor(ocean_floor):
    max_row = 0
    for rows in ocean_floor.values():
        new_max = max(rows.keys())
        max_row = max_row if max_row > new_max else new_max

    max_column = max(ocean_floor.keys())
    for column in range(0, max_column + 1):
        for row in range(0, max_row + 1):
            if column in ocean_floor and row in ocean_floor[column]:
                print(f' {ocean_floor[column][row]}', end='')
            else:
                print(f' .', end='')
        print('\n', end='')


def count_intersections(ocean_floor, threshold=2):
    count = 0
    for rows in ocean_floor.values():
        for intersects in rows.values():
            if intersects >= threshold:
                count += 1
    return count


def main():
    puzzle_input = open("inputs/05.txt", "r")

    ocean_floor = {}

    for line in puzzle_input:
        left, right = line.rstrip('\r').rstrip('\n').split(' -> ')

        from_point = convert_to_point(left)
        to_point = convert_to_point(right)

        # if from_point.x != to_point.x and from_point.y != to_point.y:
        #     continue

        for point in get_points_in_between(from_point, to_point):
            if point.y not in ocean_floor:
                ocean_floor[point.y] = {}
                ocean_floor[point.y][point.x] = 1
            elif point.x not in ocean_floor[point.y]:
                ocean_floor[point.y][point.x] = 1
            else:
                ocean_floor[point.y][point.x] += 1

    print_ocean_floor(ocean_floor)

    print("\n\n\n")
    print("***********************************************************************************************")
    print(f"Amount of points with more than 2 intersects: {count_intersections(ocean_floor, 2)}")
    print("***********************************************************************************************")


main()
