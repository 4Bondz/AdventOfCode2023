import sys


def addRight(x, y, resolver, graph):
    ACCEPTING_LEFT = ["J", "7", "-", "S"]
    for e in ACCEPTING_LEFT:
        if e in resolver[x + 1][y]:
            graph[(x, y)].add((x + 1, y))
            graph[(x + 1, y)].add((x, y))


def addLeft(x, y, resolver, graph):
    ACCEPTING_RIGHT = ["-", "F", "L", "S"]
    for e in ACCEPTING_RIGHT:
        if e in resolver[x - 1][y]:
            graph[(x, y)].add((x - 1, y))
            graph[(x - 1, y)].add((x, y))


def addAbove(x, y, resolver, graph):
    ACCEPTING_DOWN = ["|", "7", "F", "S"]
    for e in ACCEPTING_DOWN:
        if e in resolver[x][y - 1]:
            graph[(x, y)].add((x, y - 1))
            graph[(x, y - 1)].add((x, y))


def addBelow(x, y, resolver, graph):
    ACCEPTING_UP = ["|", "J", "L", "S"]
    for e in ACCEPTING_UP:
        if e in resolver[x][y + 1]:
            graph[(x, y)].add((x, y + 1))
            graph[(x, y + 1)].add((x, y))


def main():
    with open("./day10input.txt", "r") as f:
        lines = f.readlines()
    lines = [l.strip("\n") for l in lines]
    startPos = 0

    # This is how you know the makers of the question didn't mean for you to use recursion
    sys.setrecursionlimit(100_000)

    graph = {}

    resolver = [[0 for i in range(len(lines))] for j in range(len(lines[0]))]
    for x, line in enumerate(lines):
        for y, v in enumerate(line):
            resolver[y][x] = v

    for y, line in enumerate(lines):
        for x in range(len(line)):
            graph[(x, y)] = set()

    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            CURRENT_POS = (x, y)
            if char == ".":
                continue
            elif char == "F":
                # bottom boundary
                if y != len(lines) - 1:
                    addBelow(x, y, resolver, graph)
                # right boundary
                if x != len(line) - 1:
                    addRight(x, y, resolver, graph)
                    # graph[RIGHT_ONE_SQUARE].add(CURRENT_POS)
            elif char == "7":
                # bottom boundary
                if y != len(lines) - 1:
                    addBelow(x, y, resolver, graph)
                    # graph[DOWN_ONE_LINE].add(CURRENT_POS)
                # left boundary
                if x != 0:
                    addLeft(x, y, resolver, graph)
                    # graph[LEFT_ONE_SQUARE].add(CURRENT_POS)
            elif char == "J":
                # left boundary
                if x != 0:
                    addLeft(x, y, resolver, graph)
                    # graph[LEFT_ONE_SQUARE].add(CURRENT_POS)
                # top boundary
                if y != 0:
                    addAbove(x, y, resolver, graph)
                    # graph[UP_ONE_LINE].add(CURRENT_POS)
            elif char == "L":
                # top boundary
                if y != 0:
                    addAbove(x, y, resolver, graph)
                    # graph[UP_ONE_LINE].add(CURRENT_POS)
                # right boundary
                if x != len(line) - 1:
                    addRight(x, y, resolver, graph)
                    # graph[RIGHT_ONE_SQUARE].add(CURRENT_POS)
            elif char == "-":
                # left boundary
                if x != 0:
                    addLeft(x, y, resolver, graph)
                    # graph[LEFT_ONE_SQUARE].add(CURRENT_POS)
                # right boundary
                if x != len(line) - 1:
                    addRight(x, y, resolver, graph)
                    # graph[RIGHT_ONE_SQUARE].add(CURRENT_POS)
            elif char == "|":
                # top boundary
                if y != 0:
                    addAbove(x, y, resolver, graph)
                    # graph[UP_ONE_LINE].add(CURRENT_POS)
                # bottom boundary
                if y != len(lines) - 1:
                    addBelow(x, y, resolver, graph)
                    # graph[DOWN_ONE_LINE].add(CURRENT_POS)
            elif char == "S":
                startPos = CURRENT_POS
    print(graph)

    visited = []

    loopList = []

    def dfs(visited, graph, node):
        if node == startPos and len(visited) != 0:
            visited.append(node)
            loopList.append([x for x in visited])
        if node not in visited:
            if node is not startPos:
                visited.append(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(visited, graph, neighbor)
                    visited.remove(neighbor)

    dfs(visited, graph, startPos)

    maxLoopLen = 0
    maxLoop = []

    for loop in loopList:
        maxLoopLen = max(len(loop), maxLoopLen)
        maxLoop = loop

    bfsVisit = []
    bfsQueue = []
    bfsRemember = []

    def bfs(visited, graph, node):
        bfsVisit.append(node)
        bfsQueue.append(node)

        while bfsQueue:
            n = bfsQueue.pop(0)
            nx = n[0]
            ny = n[1]
            neighbors = []
            if nx != 0 and (nx - 1, ny) not in maxLoop:
                neighbors.append((nx - 1, ny))
            if nx != len(graph[0]) and (nx + 1, ny) not in maxLoop:
                neighbors.append((nx + 1, ny))
            if ny != 0 and (nx, ny - 1) not in maxLoop:
                neighbors.append((nx, ny - 1))
            if ny != len(graph) and (nx, ny + 1) not in maxLoop:
                neighbors.append((nx, ny + 1))

            for neighbor in neighbors:
                if neighbor not in bfsVisit:
                    bfsRemember.append(neighbor)
                    bfsVisit.append(neighbor)
                    bfsQueue.append(neighbor)
    #
    # bfs(bfsQueue, resolver, (0, 0))
    #
    # rem = []
    # for x, line in enumerate(lines):
    #     for y, v in enumerate(line):
    #         if (x, y) not in maxLoop and (x,y) not in bfsRemember:
    #             bfsVisit = []
    #             bfsQueue = []
    #             bfs(bfsQueue, resolver, (x,y))
    #             print("@", (x, y), "Found: ", len(bfsVisit))
    #

    def isVertex(prev, after):
        if prev[0] != after[0] and prev[1] != after[1]:
            return True
        else:
            return False

    vList = []

    for i, point in maxLoop:
        isV = False
        if i == 0:
            isV = isVertex(maxLoop[-1], maxLoop[1])
        elif i == len(maxLoop) - 1:
            isV = isVertex(maxLoop[i - 1], maxLoop[0])
        else:
            isV = isVertex(maxLoop[i - 1], maxLoop[i + 1])
        if isV:
            vList.append(maxLoop[i])

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

    maxLoop.append(maxLoop[0])

    print(polygonArea(maxLoop))


    print(maxLoopLen)
    print(len(bfsVisit))


if __name__ == "__main__":
    main()

# 277 is too high
# 100 too low
