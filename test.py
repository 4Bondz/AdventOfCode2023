from itertools import combinations


def top(x):
    s = sum(y[1] for y in x[1])
    return s


def main():
    l = [(12.34, 3), (28.99, 4), (22.99, 6), (25.04, 7), (33.90, 8), (17.56, 5), (20, 1), (15, 2)]
    TOTAL_PRICE = 75
    t = []
    for i in range(1, len(l)):
        s = list(combinations(l, i))
        for s_i in s:
            t.append((TOTAL_PRICE - sum(x[0] for x in s_i), s_i))
    t.sort(key=lambda x: abs(x[0]))
    print(t)
    # t.sort(key=top)
    # print(t)


if __name__ == "__main__":
    main()
