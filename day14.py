import time

ROCK = "O"
STOP = "#"
EMPTY = "."


def rollNorth(field, row, column):
    if row == 0:
        return  # base case
    if field[row - 1][column] == ROCK:
        rollNorth(field, row - 1, column)
    if field[row - 1][column] == STOP or field[row - 1][column] == ROCK:
        return
    if field[row - 1][column] == EMPTY and field[row][column] == ROCK:
        field[row - 1][column] = ROCK
        field[row][column] = EMPTY


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


def roll(field, row, column, direction):
    NEXT_POS_VAL = "$"
    CURRENT_POS_VAL = field[row][column]
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
    if isAtBoundary(row, column, direction, field):
        return
    if NEXT_POS_VAL == ROCK:
        rollNorth(field, row - 1, column)
    if NEXT_POS_VAL == STOP or NEXT_POS_VAL == ROCK:
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


def main(DEBUG):
    with open("./day14input.txt", "r") as f:
        lines = f.readlines()
    lines = [l.strip("\n") for l in lines]

    resolver = [[0 for i in range(len(lines[0]))] for j in range(len(lines))]
    for x, line in enumerate(lines):
        for y, v in enumerate(line):
            resolver[x][y] = v

    for i in range(1000):
        for row in range(len(resolver) - 1, -1, -1):
            for column in range(len(resolver[0]) - 1, -1, -1):
                rollNorth(resolver, row, column)

    totalLoad = 0

    # for i in range(1_000_000_000):
    #     for direction in ["NORTH", "WEST", "SOUTH", "EAST"]:
    #         roll(field, )

    for y, line in enumerate(resolver):
        for x, char in enumerate(line):
            if char == ROCK:
                totalLoad += len(resolver) - y

    print(totalLoad)

    if DEBUG:
        with open("./day14test_answer.txt", "r") as f:
            lines = f.readlines()
        lines = [l.strip("\n") for l in lines]

        answerResolver = [[0 for i in range(len(lines[0]))] for j in range(len(lines))]
        for x, line in enumerate(lines):
            for y, v in enumerate(line):
                answerResolver[x][y] = v

        for x, line in enumerate(answerResolver):
            for y, char in enumerate(line):
                try:
                    assert answerResolver[x][y] == resolver[x][y]
                except AssertionError:
                    print("ASSERTION ERROR", x, y)


if __name__ == "__main__":
    main(False)
