import itertools


class MapPoint:
    line_index = 0
    point_index = 0

    def __init__(self, line_index, point_index):
        self.line_index = line_index
        self.point_index = point_index

    def __eq__(self, other):
        return self.line_index == other.line_index and self.point_index == other.point_index

    def __ne__(self, other):
        return self.line_index != other.line_index or self.point_index != other.point_index


def recursive_basic_grow(current_point, height_map, low_point_map, considered_points: [MapPoint]):
    if current_point in considered_points:
        return 0, considered_points

    considered_points.append(current_point)
    value = height_map[current_point.line_index][current_point.point_index]
    if value == 9:
        return 0, considered_points

    count = 0

    if current_point.line_index > 0:
        next_point = MapPoint(current_point.line_index - 1, current_point.point_index)
        increment, considered_points = recursive_basic_grow(next_point, height_map, low_point_map, considered_points)
        count += increment

    if current_point.line_index < (len(height_map) - 1):
        next_point = MapPoint(current_point.line_index + 1, current_point.point_index)
        increment, considered_points = recursive_basic_grow(next_point, height_map, low_point_map, considered_points)
        count += increment

    if current_point.point_index > 0:
        next_point = MapPoint(current_point.line_index, current_point.point_index - 1)
        increment, considered_points = recursive_basic_grow(next_point, height_map, low_point_map, considered_points)
        count += increment

    if current_point.point_index < (len(height_map[0]) - 1):
        next_point = MapPoint(current_point.line_index, current_point.point_index + 1)
        increment, considered_points = recursive_basic_grow(next_point, height_map, low_point_map, considered_points)
        count += increment

    return count + 1, considered_points


def main():
    puzzle_input = open("inputs/09.txt", "r")

    part_one = False

    height_map = []
    low_point_map = []
    current_line_index = 0

    for line in puzzle_input:
        height_numbers = list(map(lambda c: int(c), list(line.rstrip('\r').rstrip('\n'))))
        height_map.append(height_numbers)
        low_points = []
        low_point_map.append(low_points)

        for index in range(0, len(height_numbers)):
            is_low_point = True
            current_point = height_numbers[index]
            if index > 0:
                is_low_point = is_low_point and height_numbers[index - 1] > current_point
            if current_line_index > 0:
                is_low_point = is_low_point and height_map[current_line_index - 1][index] > current_point
                low_point_map[current_line_index - 1][index] = \
                    low_point_map[current_line_index - 1][index] \
                    and current_point > height_map[current_line_index - 1][index]
            if index < (len(height_numbers) - 1):
                is_low_point = is_low_point and height_numbers[index + 1] > current_point
            low_points.append(is_low_point)

        current_line_index += 1

    if part_one is True:
        height_sum = 0
        for line_index in range(0, len(low_point_map)):
            low_point_line = low_point_map[line_index]
            for point_index in range(0, len(low_point_line)):
                if low_point_line[point_index] is True:
                    height_sum += (height_map[line_index][point_index] + 1)

        print(height_sum)
    else:
        basin_sizes = []
        for line_index in range(0, len(low_point_map)):
            low_point_line = low_point_map[line_index]
            for point_index in range(0, len(low_point_line)):
                if low_point_line[point_index] is True:
                    current_point = MapPoint(line_index, point_index)

                    basin_size, _ = recursive_basic_grow(current_point, height_map, low_point_map, [])
                    basin_sizes.append(basin_size)

        biggest_three = list(itertools.islice((reversed(sorted(basin_sizes))), 3))
        print(biggest_three)
        print(biggest_three[0] * biggest_three[1] * biggest_three[2])


main()
