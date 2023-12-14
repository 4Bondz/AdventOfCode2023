def main():
    with open("./dayXtest.txt", "r") as f:
        lines = f.readlines()
    lines = [l.strip("\n") for l in lines]

    resolver = [[0 for i in range(len(lines[0]))] for j in range(len(lines))]
    for x, line in enumerate(lines):
        for y, v in enumerate(line):
            resolver[x][y] = v


if __name__ == "__main__":
    main()
