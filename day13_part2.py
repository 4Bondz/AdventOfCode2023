import itertools


def listDiffBy1(l1, l2):
    # We have smudge
    diffs = 0
    pair = zip(l1, l2)
    for a, b in pair:
        if a != b:
            diffs += 1
    if diffs == 1:
        return True
    else:
        return False


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
                isOff = listDiffBy1(sampleR[start], sampleR[next])
                if sampleR[start] == sampleR[next] or isOff:
                    hasSmudgeAvailable = True
                    for k in range(1, len(sampleR)):
                        if start + k == len(sampleR) or next - k == -1:  # end of the road
                            if not hasSmudgeAvailable:  # only if we've gone to the end AND used our smudge
                                a[ansI].append(int(next))
                            break
                        elif sampleR[start + k] == sampleR[next - k]:  # Lines are equal, keep rollowing
                            continue
                        else:
                            isOffByOne = listDiffBy1(sampleR[start + k], sampleR[next - k])  # lines are not equal
                            if not isOffByOne:  # if they're not off by 1 they can't be reconciled, break
                                break
                            elif isOffByOne:  # if they are off by one, set smudge to 0 or break
                                if hasSmudgeAvailable:
                                    hasSmudgeAvailable = False
                                    continue
                                else:
                                    break
        s = 0
        print(a)
        if len(a[0]):
            s += a[0][0] * 100
        if len(a[1]):
            s += a[1][0]
        total += s
        # print(s)
    print("TOTAL", total)


if __name__ == "__main__":
    main()
