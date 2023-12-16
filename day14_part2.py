import time
import pprint
from collections import defaultdict

ROCK = "O"
STOP = "#"
EMPTY = "."


def isAtBoundary(row, column, direction, field):
    match direction:
        case "NORTH":
            return row == 0
        case "WEST":
            return column == 0
        case "EAST":
            return column == len(field[row]) - 1
        case "SOUTH":
            return row == len(field) - 1


def rollRound(resolver):
    for column in range(len(resolver) - 1, -1, -1):
        for row in range(0, len(resolver)):
            roll(resolver, row, column, "NORTH")

    # pprint.pprint(resolver)
    # print("\n")

    for row in range(0, len(resolver)):
        for column in range(0, len(resolver)):
            roll(resolver, row, column, "WEST")

    # pprint.pprint(resolver)
    # print("\n")

    for column in range(0, len(resolver)):
        for row in range(len(resolver) - 1, -1, -1):
            roll(resolver, row, column, "SOUTH")

    # pprint.pprint(resolver)
    # print("\n")

    for row in range(len(resolver) - 1, -1, -1):
        for column in range(len(resolver) - 1, -1, -1):
            roll(resolver, column, row, "EAST")

    # pprint.pprint(resolver)
    # print("\n")


def roll(field, row, column, direction):
    NEXT_POS_VAL = "$"
    CURRENT_POS_VAL = field[row][column]
    if isAtBoundary(row, column, direction, field):
        return
    match direction:
        case "NORTH":
            NEXT_POS_VAL = field[row - 1][column]
        case "WEST":
            NEXT_POS_VAL = field[row][column - 1]
        case "SOUTH":
            NEXT_POS_VAL = field[row + 1][column]
        case "EAST":
            NEXT_POS_VAL = field[row][column + 1]
    assert NEXT_POS_VAL != "$"
    if NEXT_POS_VAL == ROCK:
        match direction:
            case "NORTH":
                roll(field, row - 1, column, "NORTH")
            case "WEST":
                roll(field, row, column - 1, "WEST")
            case "SOUTH":
                roll(field, row + 1, column, "SOUTH")
            case "EAST":
                roll(field, row, column + 1, "EAST")
    if NEXT_POS_VAL == STOP:
        return
    if NEXT_POS_VAL == EMPTY and CURRENT_POS_VAL == ROCK:
        match direction:
            case "NORTH":
                field[row - 1][column] = ROCK
            case "WEST":
                field[row][column - 1] = ROCK
            case "SOUTH":
                field[row + 1][column] = ROCK
            case "EAST":
                field[row][column + 1] = ROCK
        field[row][column] = EMPTY
        match direction:
            case "NORTH":
                roll(field, row - 1, column, "NORTH")
            case "WEST":
                roll(field, row, column - 1, "WEST")
            case "SOUTH":
                roll(field, row + 1, column, "SOUTH")
            case "EAST":
                roll(field, row, column + 1, "EAST")


def main():
    with open("./day14input.txt", "r") as f:
        lines = f.readlines()
    lines = [l.strip("\n") for l in lines]

    resolver = [[0 for i in range(len(lines[0]))] for j in range(len(lines))]
    for x, line in enumerate(lines):
        for y, v in enumerate(line):
            resolver[x][y] = v

    ballinDict = defaultdict(lambda x: 0)
    collection = []
    done = False
    for i in range(1_000_000_000):
        before = "".join([j for sub in resolver for j in sub])
        rollRound(resolver)
        after = "".join([j for sub in resolver for j in sub])

        if before not in ballinDict.keys():
            ballinDict[before] = after
        else:
            ans = ballinDict[before]
            collection = [ans]
            while ans:
                ans = ballinDict[ans]
                if ans in collection:
                    done = True
                    break
                collection.append(ans)
        if done:
            break

    mod = 1_000_000_000 % (len(collection) + 1)
    patternString = collection[mod - 1]
    LINE_LEN = len(resolver)

    solutionResolver = [[0 for i in range(len(lines[0]))] for j in range(len(lines))]

    for n, char in enumerate(patternString):
        solutionResolver[n // LINE_LEN][n % LINE_LEN] = char

    totalLoad = 0

    for y, line in enumerate(solutionResolver):
        for x, char in enumerate(line):
            if char == ROCK:
                totalLoad += len(resolver) - y

    print(totalLoad)




if __name__ == "__main__":
    main()

# Too Low was 97044
# Too Low was 97080
# Too Low was 97230