import numpy as np


def filter_based_on_std(coll, std_multiples=1):
    data_std = np.std(coll)
    data_mean = np.mean(coll)

    lower_limit = data_mean - (data_std * std_multiples)
    upper_limit = data_mean + (data_std * std_multiples)

    for item in coll:
        if lower_limit <= item <= upper_limit:
            yield item


def main():
    puzzle_input = open("inputs/07.txt", "r")
    use_correct_fuel_calculation = True

    estimation_error_value = 10 if use_correct_fuel_calculation else 30
    std_multiples = 3 if use_correct_fuel_calculation else 1

    horizontal_positions = list(map(lambda n: int(n), puzzle_input.readline().rstrip('\r').rstrip('\n').split(',')))
    filtered_horizontal_positions = list(filter_based_on_std(horizontal_positions, std_multiples))

    mean_position = np.mean(filtered_horizontal_positions)
    estimated_best_position = int(np.floor(mean_position))

    print(f"Estimated cheapest alignment position is {estimated_best_position} "
          f"(with an error margin of {estimation_error_value} points)")

    position_range = range(
        estimated_best_position - estimation_error_value,
        estimated_best_position + estimation_error_value)

    lowest_cost = -1
    best_position = 0

    for current_position in position_range:
        fuel_cost = 0

        for position in horizontal_positions:
            fuel_count = abs(position - current_position)
            fuel_cost += int(pow((fuel_count + 1), 2) / 2 - ((fuel_count + 1) / 2)) \
                if use_correct_fuel_calculation else fuel_count

        if lowest_cost == -1 or lowest_cost > fuel_cost:
            lowest_cost = fuel_cost
            best_position = current_position

    print(f"Fuel cost of alignment is {lowest_cost} for alignment position at {best_position}")


main()
