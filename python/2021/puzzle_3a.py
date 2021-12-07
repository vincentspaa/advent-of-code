puzzle_input = open("inputs/03.txt", "r")

zero_value_counts = {}
one_value_counts = {}

for line in puzzle_input:
    for index in range(0, len(line) - 1):
        one_value_counts[index] = 0 if index not in one_value_counts else one_value_counts[index]
        zero_value_counts[index] = 0 if index not in zero_value_counts else zero_value_counts[index]
        if line[index] == '1':
            one_value_counts[index] = one_value_counts[index] + 1
        else:
            zero_value_counts[index] = zero_value_counts[index] + 1

gamma_rate = ""
epsilon_rate = ""

for index in range(0, len(zero_value_counts)):
    if one_value_counts[index] >= zero_value_counts[index]:
        gamma_rate += "1"
        epsilon_rate += "0"
    else:
        gamma_rate += "0"
        epsilon_rate += "1"

gamma_rate_value = int(gamma_rate, 2)
epsilon_rate_value = int(epsilon_rate, 2)

print(gamma_rate_value * epsilon_rate_value)
