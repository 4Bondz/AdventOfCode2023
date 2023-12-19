import sys


# Did it take 16 days?
# YES
# Did you #GETGOOD?
# Sorta
# I don't love that I had to add in a "base" case but its fine.

# TODO: Refactor to make this look nice

def handleBeam0(resolver, startx, starty, direction):
    match resolver[starty][startx].value:
        case ".":
            return direction
        case "\\":
            match direction:
                case "L":
                    return "U"
                case "R":
                    return "D"
                case "D":
                    return "R"
                case "U":
                    return "L"
        case "/":
            match direction:
                case "L":
                    return "D"
                case "R":
                    return "U"
                case "D":
                    return "L"
                case "U":
                    return "R"
        case "|":
            match direction:
                case "R" | "L":
                    return "D", "U"
                case _:
                    return direction

        case "-":
            match direction:
                case "U" | "D":
                    return "L", "R"
                case _:
                    return direction


def outOfRoom(resolver, startx, starty, direction):
    match direction:
        case "R":
            if startx == len(resolver[0]):
                return True
        case "L":
            if startx == -1:
                return True
        case "U":
            if starty == -1:
                return True
        case "D":
            if starty == len(resolver):
                return True
        case _:
            return False


def move(startx, starty, direction):
    match direction:
        case "R":
            return startx + 1, starty
        case "L":
            return startx - 1, starty
        case "U":
            return startx, starty - 1
        case "D":
            return startx, starty + 1


def handleBeam(resolver, startx, starty, direction, beam):
    EMPTY = "."
    ENERGIZED = "#"
    if not outOfRoom(resolver, startx, starty, direction):
        resolver[starty][startx].isActive = True
    nextx, nexty = move(startx, starty, direction)
    if outOfRoom(resolver, nextx, nexty, direction):
        return
    if (nextx, nexty, direction) in beam:
        beam.remove((nextx, nexty, direction))
        return
    else:
        beam.append((nextx, nexty, direction))
    resolver[nexty][nextx].isActive = True
    match resolver[nexty][nextx].value:
        case ".":
            handleBeam(resolver, nextx, nexty, direction, beam)
        case "/":
            if direction == "R":
                handleBeam(resolver, nextx, nexty, "U", beam)
            elif direction == "L":
                handleBeam(resolver, nextx, nexty, "D", beam)
            elif direction == "U":
                handleBeam(resolver, nextx, nexty, "R", beam)
            elif direction == "D":
                handleBeam(resolver, nextx, nexty, "L", beam)
            else:
                handleBeam(resolver, nextx, nexty, direction, beam)
        case "\\":
            if direction == "R":
                handleBeam(resolver, nextx, nexty, "D", beam)
            elif direction == "L":
                handleBeam(resolver, nextx, nexty, "U", beam)
            elif direction == "U":
                handleBeam(resolver, nextx, nexty, "L", beam)
            elif direction == "D":
                handleBeam(resolver, nextx, nexty, "R", beam)
            else:
                handleBeam(resolver, nextx, nexty, direction, beam)
        case "|":
            if direction == "R":
                handleBeam(resolver, nextx, nexty, "D", beam)
                handleBeam(resolver, nextx, nexty, "U", beam)
            elif direction == "L":
                handleBeam(resolver, nextx, nexty, "D", beam)
                handleBeam(resolver, nextx, nexty, "U", beam)
            else:
                handleBeam(resolver, nextx, nexty, direction, beam)
        case "-":
            if direction == "U":
                handleBeam(resolver, nextx, nexty, "R", beam)
                handleBeam(resolver, nextx, nexty, "L", beam)
            elif direction == "D":
                handleBeam(resolver, nextx, nexty, "R", beam)
                handleBeam(resolver, nextx, nexty, "L", beam)
            else:
                handleBeam(resolver, nextx, nexty, direction, beam)


class Tile:
    def __init__(self, isActive, value="."):
        self.isActive = isActive
        self.value = value


def resetResolver():
    with open("./day16input.txt", "r") as f:
        lines = f.readlines()
    lines = [l.strip("\n") for l in lines]
    resolver = [[Tile(isActive=False) for i in range(len(lines[0]))] for j in range(len(lines))]
    for x, line in enumerate(lines):
        for y, v in enumerate(line):
            resolver[x][y] = Tile(isActive=False, value=v)
    return resolver


def main():
    resolver = resetResolver()

    sys.setrecursionlimit(100_000)

    MAX = 0
    for side in ["L", "R", "D", "U"]:
        for startpos in range(len(resolver)):
            startx = 0
            starty = 0
            if side == "L":
                startx = len(resolver[0]) - 1
                starty = startpos
            elif side == "R":
                startx = 0
                starty = startpos
            elif side == "U":
                startx = startpos
                starty = len(resolver) - 1
            elif side == "D":
                startx = startpos
                starty = 0

            print("FOR STARTING VALUE", startx, starty, side)
            beam = []
            initialDirection = handleBeam0(resolver, startx, starty, side)
            for direction in initialDirection:
                handleBeam(resolver, startx, starty, direction, beam)

            total = 0
            for row in resolver:
                for tile in row:
                    if tile.isActive:
                        total += 1
            print(total)
            if total > MAX:
                MAX = total
                ## PRINT
                for row in resolver:
                    for tile in row:
                        if tile.isActive:
                            print("#", end="")
                        else:
                            print(".", end="")
                    print("\n")
            del resolver
            resolver = resetResolver()
        print("MAX VAL: ", MAX)


if __name__ == "__main__":
    main()
