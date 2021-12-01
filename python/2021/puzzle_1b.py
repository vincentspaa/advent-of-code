puzzleInput = open("inputs/00.txt", "r")

measurementsLargerThanPrevious = 0
firstWindow = []
secondWindow = []


def sum_n_elements(arr, n):
    current_sum = 0
    for index in range(0, n):
        current_sum += arr[index]
    return current_sum


for line in puzzleInput:
    integerLine = int(line)

    if len(firstWindow) > 0:
        secondWindow.insert(0, integerLine)
    if len(secondWindow) < 3:
        firstWindow.insert(0, integerLine)

    print(firstWindow)
    print(secondWindow)

    if len(secondWindow) >= 3 and sum_n_elements(secondWindow, 3) > sum_n_elements(firstWindow, 3):
        measurementsLargerThanPrevious += 1

    lastLine = integerLine
    if len(secondWindow) > 5:
        break

print(measurementsLargerThanPrevious)
