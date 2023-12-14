from itertools import combinations


def main():
    with open("./day11input.txt", "r") as f:
        lines = f.readlines()
    lines = [l.strip("\n") for l in lines]

    resolver = [[0 for i in range(len(lines[0]))] for j in range(len(lines))]
    for x, line in enumerate(lines):
        for y, v in enumerate(line):
            resolver[x][y] = v

    galaxyList = []
    for x, line in enumerate(resolver):
        for y, char in enumerate(line):
            if char == "#":
                galaxyList.append((x, y))

    expandedRows = []
    expandedColumns = []

    for i, line in enumerate(resolver):
        if "#" not in line:
            expandedRows.append(i)

    for y in range(len(resolver[0])):
        isColumnEmpty = True
        for x in range(len(resolver)):
            if resolver[x][y] == "#":
                isColumnEmpty = False
                break
        if isColumnEmpty:
            expandedColumns.append(y)

    combos = combinations(galaxyList, 2)
    total = 0
    DUP_CONST = 1_000_000


    for combo in combos:
        count = 0
        first = combo[0]
        second = combo[1]
        minX = min(first[0], second[0])
        maxX = max(first[0], second[0])
        minY = min(first[1], second[1])
        maxY = max(first[1], second[1])

        for row in expandedRows:
            if minX <= row <= maxX:
                count += 1

        for column in expandedColumns:
            if minY <= column <= maxY:
                count += 1

        print(count)

        total += (abs(first[0] - second[0]) + abs(first[1] - second[1]) + count * (DUP_CONST - 1))


    print(total)



    # with open("./day11test_step2.txt", "r") as f:
    #     lines = f.readlines()
    # lines = [l.strip("\n") for l in lines]
    #
    # solver = [[0 for i in range(len(lines[0]))] for j in range(len(lines))]
    # for x, line in enumerate(lines):
    #     for y, v in enumerate(line):
    #         solver[x][y] = v
    #
    # for x, line in enumerate(solver):
    #     for y, char in enumerate(line):
    #         try:
    #             if solver[x][y] != resolver[x][y]:
    #                 print(f"Bad Resolver at ({x},{y})! Solver Says:{solver[x][y]} Resolver Says:{resolver[x][y]} ")
    #         except:
    #             print(f"Bad Value at {x},{y}")



    print('x')


if __name__ == "__main__":
    main()

    """
    def main():
    with open("./day11input.txt", "r") as f:
        lines = f.readlines()
    lines = [l.strip("\n") for l in lines]

    resolver = [[0 for i in range(len(lines[0]))] for j in range(len(lines))]
    for x, line in enumerate(lines):
        for y, v in enumerate(line):
            resolver[x][y] = v

    expandedRows = []

    for i, line in enumerate(resolver):
        if "#" not in line:
            expandedRows.append(i)
    offset = 0
    for row in expandedRows:
        resolver.insert(row + offset, ["." for i in range(len(resolver[0]))])
        offset += 1

    expandedColumns = []

    for y in range(len(resolver[0])):
        isColumnEmpty = True
        for x in range(len(resolver)):
            if resolver[x][y] == "#":
                isColumnEmpty = False
                break
        if isColumnEmpty:
            expandedColumns.append(y)

    for x, row in enumerate(resolver):
        offset = 0
        for y in range(len(row)):
            if y in expandedColumns:
                row.insert(y + offset, ".")
                offset += 1

    # with open("./day11test_step2.txt", "r") as f:
    #     lines = f.readlines()
    # lines = [l.strip("\n") for l in lines]
    #
    # solver = [[0 for i in range(len(lines[0]))] for j in range(len(lines))]
    # for x, line in enumerate(lines):
    #     for y, v in enumerate(line):
    #         solver[x][y] = v
    #
    # for x, line in enumerate(solver):
    #     for y, char in enumerate(line):
    #         try:
    #             if solver[x][y] != resolver[x][y]:
    #                 print(f"Bad Resolver at ({x},{y})! Solver Says:{solver[x][y]} Resolver Says:{resolver[x][y]} ")
    #         except:
    #             print(f"Bad Value at {x},{y}")

    galaxyList = []
    for x, line in enumerate(resolver):
        for y, char in enumerate(line):
            if char == "#":
                galaxyList.append((x,y))

    combos = combinations(galaxyList, 2)
    total = 0

    for combo in combos:
        first = combo[0]
        second = combo[1]
        print(first, second, abs(first[0] - second[0]) + abs(first[1] - second[1]))
        total += abs(first[0] - second[0]) + abs(first[1] - second[1])
    print(total)


    print('x')

    """
