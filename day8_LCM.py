from math import lcm
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
    numberOfPathsToZ = []
    for key in mapDict.keys():
        if key.endswith("A"):
            watchPathList.append(key)

    for startPath in watchPathList:
        done = False
        count = 0
        sourceKey = startPath
        while not done:
            # Find the ??Z
            for direction in RLGameString:
                count += 1
                index = int(direction)
                sourceKey = mapDict[sourceKey][index]
                if sourceKey.endswith("Z"):
                    done = True
                    break
            if done:
                numberOfPathsToZ.append(count)

    print(lcm(*numberOfPathsToZ))


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
