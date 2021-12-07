puzzle_input = open("inputs/01.txt", "r")

measurementsLargerThanPrevious = 0
lastLine = -1

for line in puzzle_input:
    integerLine = int(line)
    if lastLine != -1 and integerLine > lastLine:
        measurementsLargerThanPrevious += 1
    lastLine = integerLine

print(measurementsLargerThanPrevious)
