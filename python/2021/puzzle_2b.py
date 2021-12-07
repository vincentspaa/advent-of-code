puzzle_input = open("inputs/02.txt", "r")

horizontalPosition = 0
depth = 0
aim = 0

for line in puzzle_input:
    parts = line.split(' ')

    direction = parts[0]
    amount = int(parts[1].strip('\n'))

    if direction == "forward":
        horizontalPosition += amount
        depth += amount * aim
    elif direction == "down":
        aim += amount
    elif direction == "up":
        aim -= amount

finalPosition = horizontalPosition * depth
print(finalPosition)
