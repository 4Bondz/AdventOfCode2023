def search(board, r, c):
    SYMBOL_LIST = ["!", "@", "#", "$", "%", "^", "&", "&", "*", "(", ")", "-", "_", "=", "+", "|", ",", "/", "?"]
    # 8 spaces to search

    # N, NE, E, SE, S, SW, W, NW

    UP = max(r - 1, 0)
    DOWN = min(r + 1, len(board) - 1)
    LEFT = max(c - 1, 0)
    RIGHT = min(c + 1, len(board[r]) - 1)

    # board default is board[r][c]
    N = board[UP][c]
    NE = board[UP][RIGHT]
    E = board[r][RIGHT]
    SE = board[DOWN][RIGHT]
    S = board[DOWN][c]
    SW = board[DOWN][LEFT]
    W = board[r][LEFT]
    NW = board[UP][LEFT]

    for charInDirection in [N, NE, E, SE, S, SW, W, NW]:
        if charInDirection in SYMBOL_LIST:
            return True
    return False


def part2search(board, r, c):
    # 8 spaces to search

    # N, NE, E, SE, S, SW, W, NW

    UP = max(r - 1, 0)
    DOWN = min(r + 1, len(board) - 1)
    LEFT = max(c - 1, 0)
    RIGHT = min(c + 1, len(board[r]) - 1)

    # board default is board[r][c]
    N = board[UP][c]
    NE = board[UP][RIGHT]
    E = board[r][RIGHT]
    SE = board[DOWN][RIGHT]
    S = board[DOWN][c]
    SW = board[DOWN][LEFT]
    W = board[r][LEFT]
    NW = board[UP][LEFT]

    charDirArr = [N, NE, E, SE, S, SW, W, NW]
    posArr = [(UP, c), (UP, RIGHT), (r, RIGHT), (DOWN, RIGHT), (DOWN, c), (DOWN, LEFT), (r, LEFT), (UP, LEFT)]
    adjArr = []

    for i, charInDirection in enumerate(charDirArr):
        if charInDirection.isdigit():
            adjArr.append(posArr[i])
    if len(adjArr) > 0:
        return adjArr
    return []


def buildNumber(board, initCoord):
    # get a coordinate, search left, search right to get the arr
    coordArr = {initCoord}
    # search left
    leftSearchCoord = initCoord
    # HERE WAS THE BUG!!! IT WAS AN OFF BY ONE ERROR
    # LESSON? TEST YOUR CORNER CASES!!!!
    while leftSearchCoord[1] >= 0:
        if board[leftSearchCoord[0]][leftSearchCoord[1]].isdigit():
            coordArr.add(leftSearchCoord)
            leftSearchCoord = (leftSearchCoord[0], leftSearchCoord[1] - 1)
        else:
            break

    rightSearchCoord = initCoord
    while rightSearchCoord[1] < len(board[0]):
        if board[rightSearchCoord[0]][rightSearchCoord[1]].isdigit():
            coordArr.add(rightSearchCoord)
            rightSearchCoord = (rightSearchCoord[0], rightSearchCoord[1] + 1)
        else:
            break

    coordArr = list(coordArr)
    coordArr.sort(key=lambda x: x[1])

    num = []
    for coord in coordArr:
        num.append(board[coord[0]][coord[1]])
    return int("".join(num)), coordArr[0][0], coordArr[0][1], coordArr[len(coordArr) - 1][0], \
    coordArr[len(coordArr) - 1][1]


def main():
    board = []
    total = 0
    with open("./day3input.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            board.append([*line.strip("\n")])
    for r, row in enumerate(board):
        numberArr = []
        numberPending = False
        numberAdjacent = False

        for c, char in enumerate(row):
            # Part 2
            """
            if char == "*":
                adjArr = part2search(board, r, c)
                if not len(adjArr):
                    continue
                adjNumbers = []
                for startCoordinates in adjArr:
                    adjNumbers.append(buildNumber(board, startCoordinates))
                adjNumbers = set(adjNumbers)
                if len(adjNumbers) == 2:
                    print(r,c, adjNumbers)
                    adjNumbers = list(adjNumbers)
                    total += adjNumbers[0][0] * adjNumbers[1][0]
                else:
                    #print(r, c, adjNumbers)
                    pass
            """

            if char.isdigit():
                numberArr.append(char)
                if numberPending and numberAdjacent:
                    continue  ## Speedhack
                # SEARCH
                isAdjacent = search(board, r, c)
                if isAdjacent:
                    numberAdjacent = True
                numberPending = True
            else:
                if numberPending:
                    if numberAdjacent:
                        print('NUM:', "".join(numberArr))
                        total += int("".join(numberArr))
                numberArr = []
                numberAdjacent = False
                # NUmber has just ended
                numberPending = False

        if numberPending:
            if numberAdjacent:
                print('NUM:', "".join(numberArr))
                total += int("".join(numberArr))

    print(total)


# rip line width and defined adjecency
# adjacency is for each digit of the number
#


if __name__ == '__main__':
    main()

""" PArt 2

   board = []
    total = 0
    with open("./day3input.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            board.append([*line.strip("\n")])
    for r, row in enumerate(board):
        numberArr = []
        numberPending = False
        numberAdjacent = False

        for c, char in enumerate(row):
            # Part 2

            if char == "*":
                adjArr = part2search(board, r, c)
                if not len(adjArr):
                    continue
                adjNumbers = []
                for startCoordinates in adjArr:
                    adjNumbers.append(buildNumber(board, startCoordinates))
                adjNumbers = set(adjNumbers)
                if len(adjNumbers) == 2:
                    print(r,c, adjNumbers)
                    adjNumbers = list(adjNumbers)
                    total += adjNumbers[0][0] * adjNumbers[1][0]
                else:
                    #print(r, c, adjNumbers)
                    pass

            '''
            if char.isdigit():
                numberArr.append(char)
                if numberPending and numberAdjacent:
                    continue  ## Speedhack
                # SEARCH
                isAdjacent = search(board, r, c)
                if isAdjacent:
                    numberAdjacent = True
                numberPending = True
            else:
                if numberPending:
                    if numberAdjacent:
                        print('NUM:', "".join(numberArr))
                        total += int("".join(numberArr))
                numberArr = []
                numberAdjacent = False
                # NUmber has just ended
                numberPending = False

        if numberPending:
            if numberAdjacent:
                print('NUM:', "".join(numberArr))
                total += int("".join(numberArr))
        '''
    print(total)
"""

""" Part 1
def main():
    board = []
    total = 0
    with open("./day3input.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            board.append([*line.strip("\n")])
    for r, row in enumerate(board):
        numberArr = []
        numberPending = False
        numberAdjacent = False

        for c, char in enumerate(row):
            # Part 2
            '''
            if char == "*":
                adjArr = part2search(board, r, c)
                if not len(adjArr):
                    continue
                adjNumbers = []
                for startCoordinates in adjArr:
                    adjNumbers.append(buildNumber(board, startCoordinates))
                adjNumbers = set(adjNumbers)
                if len(adjNumbers) == 2:
                    print(r,c, adjNumbers)
                    adjNumbers = list(adjNumbers)
                    total += adjNumbers[0][0] * adjNumbers[1][0]
                else:
                    #print(r, c, adjNumbers)
                    pass
            '''
            if char.isdigit():
                numberArr.append(char)
                if numberPending and numberAdjacent:
                    continue  ## Speedhack
                # SEARCH
                isAdjacent = search(board, r, c)
                if isAdjacent:
                    numberAdjacent = True
                numberPending = True
            else:
                if numberPending:
                    if numberAdjacent:
                        print('NUM:', "".join(numberArr))
                        total += int("".join(numberArr))
                numberArr = []
                numberAdjacent = False
                # NUmber has just ended
                numberPending = False

        if numberPending:
            if numberAdjacent:
                print('NUM:', "".join(numberArr))
                total += int("".join(numberArr))
        
    print(total)
"""