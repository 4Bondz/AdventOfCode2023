def polygonArea(vertices):
    # A function to apply the Shoelace algorithm
    numberOfVertices = len(vertices)
    sum1 = 0
    sum2 = 0

    for i in range(0, numberOfVertices - 1):
        sum1 = sum1 + vertices[i][0] * vertices[i + 1][1]
        sum2 = sum2 + vertices[i][1] * vertices[i + 1][0]

    # Add xn.y1
    sum1 = sum1 + vertices[numberOfVertices - 1][0] * vertices[0][1]
    # Add x1.yn
    sum2 = sum2 + vertices[0][0] * vertices[numberOfVertices - 1][1]

    area = abs(sum1 - sum2) / 2
    return area

def main():
    with open("./day18input.txt", "r") as f:
        lines = f.readlines()
    lines = [l.strip("\n") for l in lines]
    startPos = (0, 0)
    vertexList = []
    currentPos = startPos
    edge = []
    vSum = 0
    for line in lines:
        _, _, directionString = line.split(" ")
        directionString = directionString.strip("(")
        directionString = directionString.strip(")")
        directionString = directionString.replace("#", "0x")
        directionMap = {0: "R", 1: "D", 2: "L", 3: "U"}
        direction = directionMap[int(directionString[-1])]
        hexLength = directionString[0:-1]
        intLength = int(hexLength, 16)
        nextPos = (0, 0)
        match direction:
            case "D":
                nextPos = (currentPos[0], currentPos[1] + intLength)
            case "U":
                nextPos = (currentPos[0], currentPos[1] - intLength)
            case "L":
                nextPos = (currentPos[0] - intLength, currentPos[1])
            case "R":
                nextPos = (currentPos[0] + intLength, currentPos[1])
        vertexList.append(nextPos)
        edge.append((directionMap[int(directionString[-1])], intLength))
        currentPos = nextPos
        vSum += intLength

    print(edge, end="\n")
    print(vertexList)
        # build vertex list
    area = polygonArea(vertexList)
    print((area + 1 + vSum / 2))
        # Use Shoelace algorithm to get the internal area from the vertex list

    print("952408144115.0")

if __name__ == "__main__":
    main()

# wrong:
