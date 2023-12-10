def main():
    with open("./day8input.txt", "r") as f:
        lines = f.readlines()

    RLGameString = lines[0].strip("\n")
    directionLines = lines[2:]

    RLGameString = RLGameString.replace("R", "1")
    RLGameString = RLGameString.replace("L", "0")

    mapDict = {}

    for line in directionLines:
        mapArr = line.strip("\n").replace(" ", "").split("=")
        src = mapArr[0]
        dst = mapArr[1].replace("(", "").replace(")", "").split(",")
        mapDict[src] = dst

    # Part 2 (Hard way)
    watchPathList = []
    for key in mapDict.keys():
        if key.endswith("A"):
            watchPathList.append(key)
    count = 0
    done = False
    while not done:
        for direction in RLGameString:
            for i, pos in enumerate(watchPathList):
                index = int(direction)
                sourceKey = mapDict[pos][index]
                watchPathList[i] = sourceKey
            count += 1
            if count % 10_000_000 == 0:
                print("CHKPT", count)
            done = True
            for val in watchPathList:
                if not val.endswith("Z"):
                    done = False
            if done:
                print("count", count)
                return
            # if sourceKey == "ZZZ":
            #     done = True
            #     print("count", count)
            #     break

    # The answer was "14_935_034_899_483"
    # THe slow way is completely infeasble
    # See day8_LCM


if __name__ == "__main__":
    main()

"""
def main():
    with open("./day8input.txt", "r") as f:
        lines = f.readlines()

    RLGameString = lines[0].strip("\n")
    directionLines = lines[2:]

    RLGameString = RLGameString.replace("R", "1")
    RLGameString = RLGameString.replace("L", "0")

    mapDict = {}

    for line in directionLines:
        mapArr = line.strip("\n").replace(" ", "").split("=")
        src = mapArr[0]
        dst = mapArr[1].replace("(", "").replace(")", "").split(",")
        mapDict[src] = dst
    
    #

    count = 0
    sourceKey = "AAA"
    done = False
    while not done:
        for direction in RLGameString:
            index = int(direction)
            sourceKey = mapDict[sourceKey][index]
            count += 1
            if sourceKey == "ZZZ":
                done = True
                print("count", count)
                break


    print("X")
"""
