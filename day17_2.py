import pprint
from itertools import chain

INFINITY = float("inf")
import heapq


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self) -> bool:
        return not self.elements

    def put(self, item, priority: float):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]


class Graph:

    def __len__(self):
        return len(self.resolver)

    def __init__(self, rawGraphInput):
        self.edgeGraph = {}
        self.resolver = [[0 for i in range(len(rawGraphInput[0]))] for j in range(len(rawGraphInput))]
        self.maxX = len(self.resolver[0]) if len(self.resolver) > 0 else 0
        self.maxY = len(self.resolver)
        for x, line in enumerate(rawGraphInput):
            for y, v in enumerate(line):
                self.resolver[x][y] = int(v)

        for y, nodeList in enumerate(self.resolver):
            for x, node in enumerate(nodeList):
                neighborList = self.getNeighbors((x, y))
                self.edgeGraph[(x, y)] = neighborList
        self.straightPathLength = 0

    # def bellmanFord(self, start: (int, int)):
    #     V = []
    #     distanceFromPoints = [[INFINITY for i in range(self.maxX)] for j in range(self.maxY)]
    #     prevPointer = [[None for i in range(self.maxX)] for j in range(self.maxY)]
    #
    #     for i in range(start[0], self.maxX):
    #         for j in range(start[1], self.maxY):
    #             V.append((i, j))
    #
    #     distanceFromPoints[start[1]][start[0]] = 0
    #
    #     for current in V:
    #         for next in self.edgeGraph[current]:
    #             if distanceFromPoints[current[1]][current[0]] != INFINITY and \
    #                     distanceFromPoints[current[1]][current[0]] + next.value < distanceFromPoints[next.y][next.x]:
    #                 distanceFromPoints[next.y][next.x] = distanceFromPoints[current[1]][current[0]] + next.value
    #                 prevPointer[next.y][next.x] = current
    #     return distanceFromPoints, prevPointer

    def heuristic(self, start, next, cameFrom):
        path = self.reconstruct_path(cameFrom, start, next)
        print(path)
        if len(path) >= 4:
            if abs(path[-1][0] - path[-4][0]) == 3:
                return 100_000_000_000
            if abs(path[-1][1] - path[-4][1]) == 3:
                return 100_000_000_000
        return 0
    # @staticmethod
    # def heuristic(a, b) -> float:
    #     (x1, y1) = a
    #     (x2, y2) = b
    #     return abs(x1 - x2) + abs(y1 - y2)

    def AStar(self, start, end):
        frontier = PriorityQueue()
        frontier.put((0, 0), 0)
        cameFrom = {}
        costSoFar = {}
        cameFrom[start] = None
        costSoFar[start] = 0

        while not frontier.empty():
            current = frontier.get()
            if current == end:
                break
            nei = self.getNeighbors(current)
            for next in nei:
                newCost = costSoFar[current] + self.resolver[next[1]][next[0]]
                if next not in costSoFar or newCost < costSoFar[next]:
                    costSoFar[next] = newCost
                    cameFrom[next] = current
                    priority = newCost + self.resolver[next[1]][next[0]]
                    frontier.put(next, priority)
        return cameFrom, costSoFar

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

    @staticmethod
    def reconstruct_path(came_from, start, goal):
        current = goal
        path = []
        if goal not in came_from:  # no path was found
            return []
        while current != start:
            path.append(current)
            current = came_from[current]
        path.append(start)  # optional
        path.reverse()  # optional
        return path

    # def resolveNeighbors(self, currentNode):
    #     neighbors = self.getNeighbors(currentNode)
    #     neighborNodes = []
    #     for neighbor in neighbors:
    #         neighborValue = self.resolver[neighbor[1]][neighbor[0]].value
    #         neighborNodes.append(Node(neighbor[0], neighbor[1], neighborValue))
    #     return neighborNodes

    # def removeEdge(self, node, edge):
    #     edgeList = self.edgeGraph[(node[0], node[1])]
    #     for testEdge in edgeList:
    #         if testEdge.x == edge[0] and testEdge.y == edge[1]:
    #             edgeList.remove(testEdge)
    #             self.edgeGraph[(node[0], node[1])] = edgeList
    #             return testEdge


def getNewDirectionOfMovement(current, next):
    if current[0] - next[0] == 1:
        return "E"
    elif current[0] - next[0] == -1:
        return "W"
    elif current[1] - next[1] == 1:
        return "N"
    elif current[1] - next[1] == -1:
        return "S"





def main():
    with open("./day17test.txt", "r") as f:
        lines = f.readlines()
    lines = [l.strip("\n") for l in lines]
    graph = Graph(lines)
    # costList, prevPointers = graph.bellmanFord((0, 0))
    cameFrom, costSoFar = graph.AStar((0, 0), (12, 12))
    z = graph.reconstruct_path(cameFrom, start=(0, 0), goal=(12, 12))
    print(z)

    # for x, row in enumerate(prevPointers):
    #     for y, prev in enumerate(row):
    #         if prev != None:
    #             nextPointers[prev[0]][prev[1]] = (x, y)
    #
    #
    # currentElementPointer = (len(graph) - 1, len(graph) - 1)
    # nextElementPointer: (int, int)
    # currentDirection = None
    # sameDirectionCount = 0
    # path = []
    #
    # while True:
    #     nextElementPointer = prevPointers[currentElementPointer[1]][currentElementPointer[0]]
    #     newDirection = getNewDirectionOfMovement(currentElementPointer, nextElementPointer)
    #     if newDirection == currentDirection:
    #         sameDirectionCount += 1
    #         if sameDirectionCount == 3:
    #             # Break the edge and redo the BF
    #             graph.removeEdge(currentElementPointer, nextElementPointer)
    #             _, prevPointers = graph.bellmanFord((0, 0))
    #     else:
    #         currentDirection = newDirection
    #     path.append(nextElementPointer)
    #     currentElementPointer = nextElementPointer


if __name__ == "__main__":
    main()
