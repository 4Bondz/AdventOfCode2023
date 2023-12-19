import pprint

class Node:
    def __init__(self, x, y, value):
        self.value = value
        self.y = y
        self.x = x


class Graph:
    def __init__(self, rawGraphInput):
        self.resolver = [[Node(0, 0, 0) for i in range(len(rawGraphInput[0]))] for j in range(len(rawGraphInput))]
        for x, line in enumerate(rawGraphInput):
            for y, v in enumerate(line):
                self.resolver[x][y] = Node(x, y, int(v))

        self.maxX = len(self.resolver[0]) if len(self.resolver) > 0 else 0
        self.maxY = len(self.resolver)
        self.straightPathLength = 0

    def bellmanFord(self, start: (int, int)):
        V = []
        distances = [[float("inf") for i in range(self.maxX)] for j in range(self.maxY)]
        prevPointer = [[None for i in range(self.maxX)] for j in range(self.maxY)]

        for i in range(self.maxX):
            for j in range(self.maxY):
                V.append((i, j))

        # NOT DONE

    def dijkstra(self, start: (int, int)):
        distances = [[float("inf") for i in range(self.maxX)] for j in range(self.maxY)]
        prevPointer = [[None for i in range(self.maxX)] for j in range(self.maxY)]
        Q = []
        distances[start[1]][start[0]] = 0

        for i in range(self.maxX):
            for j in range(self.maxY):
                Q.append((i, j))

        while Q:
            currentNode = self.minDistance(distances, Q)
            Q.remove(currentNode)
            neighbors = self.getNeighbors(currentNode)
            for neighbors in neighbors:
                newDistance = distances[currentNode[0]][currentNode[1]] + self.resolver[neighbors[0]][neighbors[1]].value
                if newDistance < distances[neighbors[0]][neighbors[1]]:
                    distances[neighbors[0]][neighbors[1]] = newDistance
                    prevPointer[neighbors[0]][neighbors[1]] = currentNode

        return distances, prevPointer

    @staticmethod
    def minDistance(distances, Q):
        minVal = float("inf")
        minIndex = -1

        for vertex in Q:
            if distances[vertex[1]][vertex[0]] < minVal:
                minVal = distances[vertex[1]][vertex[0]]
                minIndex = vertex
        return minIndex

    def getNeighbors(self, currentNode):
        neighborList = []
        if currentNode[0] < self.maxY - 1:
            neighborList.append((currentNode[0] + 1, currentNode[1]))
        if currentNode[0] > 0:
            neighborList.append((currentNode[0] - 1, currentNode[1]))
        if currentNode[1] < self.maxX - 1:
            neighborList.append((currentNode[0], currentNode[1] + 1))
        if currentNode[1] > 0:
            neighborList.append((currentNode[0], currentNode[1] - 1))
        return neighborList


def getNeighbors(k, currentNode):
    neighborList = []
    if currentNode[0] < len(k) - 1:
        neighborList.append((currentNode[0] + 1, currentNode[1]))
    if currentNode[0] > 0:
        neighborList.append((currentNode[0] - 1, currentNode[1]))
    if currentNode[1] < len(k) - 1:
        neighborList.append((currentNode[0], currentNode[1] + 1))
    if currentNode[1] > 0:
        neighborList.append((currentNode[0], currentNode[1] - 1))
    return neighborList
def main():
    with open("./day17test.txt", "r") as f:
        lines = f.readlines()
    lines = [l.strip("\n") for l in lines]
    graph = Graph(lines)
    k = graph.dijkstra((0, 0))
    pprint.pprint(k[0])








if __name__ == "__main__":
    main()
