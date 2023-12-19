def main():
    with open("./day18input.txt", "r") as f:
        lines = f.readlines()
    lines = [l.strip("\n") for l in lines]
    startPos = (0, 0)
    vertexList = [startPos]
    currentPos = startPos
    for line in lines:
        directionString, _, _ = line.split(" ")
        directionString = directionString[-1].replace("#", "0x")
        directionMap = {0: "R", 1: "D", 2: "L", 3: "U"}
        direction = directionMap[directionString]
        hexLength = directionString[0:-1]
        intLength = int(hexLength)
        nextPos = (0, 0)
        match direction:
            case "D":
                nextPos = (currentPos[0], currentPos[1] + intLength)
            case "U":
                nextPos = (currentPos[0], currentPos[1] - intLength)
            case "L":
                nextPos = (currentPos[0] - intLength, currentPos[1])
            case "R":
                pass



        # build vertex list
        # Use Shoelace algorithm to get the internal area from the vertex list


if __name__ == "__main__":
    main()

# wrong:
