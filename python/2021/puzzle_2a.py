puzzle_input = open("inputs/01.txt", "r")

horizontalPosition = 0
depth = 0

for line in puzzle_input:
    parts = line.split(' ')

    direction = parts[0]
    amount = int(parts[1].strip('\n'))

    if direction == "forward":
        horizontalPosition += amount
    elif direction == "down":
        depth += amount
    elif direction == "up":
        depth -= amount

finalPosition = horizontalPosition * depth
print(finalPosition)
