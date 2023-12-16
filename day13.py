import itertools


def main():
    with open("./day13input.txt", "r") as f:
        lines = f.readlines()
    lines = [l.strip("\n") for l in lines]

    puzzles = [[]]
    puzzleIndex = 0
    for line in lines:
        if line == "":
            puzzleIndex += 1
            puzzles.append(list())
        else:
            puzzles[puzzleIndex].append(line)

    total = 0
    for P, puzzle in enumerate(puzzles):
        resolver = [[0 for i in range(len(puzzle[0]))] for j in range(len(puzzle))]
        for x, line in enumerate(puzzle):
            for y, v in enumerate(line):
                resolver[x][y] = v

        resolverT = list(itertools.zip_longest(*resolver))

        a = [[], []]

        for ansI, sampleR in enumerate([resolver, resolverT]):
            for start, splitRow in enumerate(sampleR):
                if start == len(sampleR) - 1:  # No break possible on this row
                    continue
                next = start + 1
                if sampleR[start] == sampleR[next]:
                    # Base row matches, expand outwards
                    for k in range(0, len(sampleR)):
                        if sampleR[start + k] != sampleR[next - k]:
                            break
                        if start + k == len(sampleR) - 1 or next - k == 0:
                            a[ansI].append(int(next))
                            break

        s: int
        s = 0
        print(a)
        if len(a[0]):
            s += a[0][0]*100
        if len(a[1]):
            s += a[1][0]
        total += s
        #print(s)
    print("TOTAL", total)




if __name__ == "__main__":
    main()

# 23264 is too Low
# 31005 is too low
# 38163 is too low
