#  Bag with cubes, R,G,B

# PARAMS
MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

MAX_DICT = {"blue": MAX_BLUE, "green": MAX_GREEN, "red": MAX_RED}

from functools import reduce
def main():
    total = 0
    with open("./day2input.txt", "r") as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            maxDict = {"red": 0, "green": 0, "blue": 0}
            failed = False
            # each line is a game
            gameInfo = line.split(":")[1]
            roundList = gameInfo.split(";")
            for round in roundList:
                drawList = round.split(",")
                for draw in drawList:
                    splitDraw = draw.split(" ")
                    splitDraw = list(filter(lambda x: x != "", splitDraw))
                    color = splitDraw[1].strip("\n")
                    number = int(splitDraw[0])
                    # Part 1
                    # if number > MAX_DICT[color]:
                    #     failed = True
                    #     break

                    # Part 2
                    if number > maxDict[color]:
                       maxDict[color] = number
            print("Game", i+1, "line:", line, "MAX_DICT:", maxDict)
            # Part 1
            # if not failed:
            #     total += i + 1

            # Part 2

            power = reduce((lambda x, y: x * y), maxDict.values())
            total += power
    print(total)

if __name__ == "__main__":
    main()


    """
    Part 1
        total = 0
    with open("./day2input.txt", "r") as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            maxDict = {"red": 0, "green": 0, "blue": 0}
            failed = False
            # each line is a game
            gameInfo = line.split(":")[1]
            roundList = gameInfo.split(";")
            for round in roundList:
                drawList = round.split(",")
                for draw in drawList:
                    splitDraw = draw.split(" ")
                    splitDraw = list(filter(lambda x: x != "", splitDraw))
                    color = splitDraw[1].strip("\n")
                    number = int(splitDraw[0])
                    # Part 1
                    if number > MAX_DICT[color]:
                        failed = True
                        break

                    # Part 2
                    #if number > maxDict[color]:
                    #    maxDict[color] = number
            #rint("Game", i+1, "line:", line, "MAX_DICT:", maxDict)
            # Part 1
            if not failed:
                total += i + 1

            # Part 2

            #power = reduce((lambda x, y: x * y), maxDict.values())
            #total += power
    print(total)
    """

    """
    Part 2
    
    def main():
    total = 0
    with open("./day2input.txt", "r") as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            maxDict = {"red": 0, "green": 0, "blue": 0}
            failed = False
            # each line is a game
            gameInfo = line.split(":")[1]
            roundList = gameInfo.split(";")
            for round in roundList:
                drawList = round.split(",")
                for draw in drawList:
                    splitDraw = draw.split(" ")
                    splitDraw = list(filter(lambda x: x != "", splitDraw))
                    color = splitDraw[1].strip("\n")
                    number = int(splitDraw[0])
                    # Part 1
                    # if number > MAX_DICT[color]:
                    #     failed = True
                    #     break

                    # Part 2
                    if number > maxDict[color]:
                       maxDict[color] = number
            print("Game", i+1, "line:", line, "MAX_DICT:", maxDict)
            # Part 1
            # if not failed:
            #     total += i + 1

            # Part 2

            power = reduce((lambda x, y: x * y), maxDict.values())
            total += power
    print(total)
    """