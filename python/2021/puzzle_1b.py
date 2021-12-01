puzzleInput = open("inputs/00.txt", "r")

measurementsLargerThanPrevious = 0
firstWindow = []
secondWindow = []
input_count = 1

for line in puzzleInput:
    integerLine = int(line)

    if len(firstWindow) > 0:
        secondWindow.append(integerLine)

    if len(secondWindow) == 3:
        if sum(secondWindow) > sum(firstWindow):
            measurementsLargerThanPrevious += 1

        firstWindow.pop(0)
        secondWindow.pop(0)

    firstWindow.append(integerLine)
    input_count += 1

print(measurementsLargerThanPrevious)
