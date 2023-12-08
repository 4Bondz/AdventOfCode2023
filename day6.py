from functools import reduce


def main():
    lines = []
    with open("./day6input.txt", "r") as f:
        lines = f.readlines()
    timeLine = lines[0].strip("\n")
    distanceLine = lines[1]

    # Part 1
    #timeArr = list(filter(lambda x: x != "" and x != "Time:", timeLine.split(" ")))
    #distanceArr = list(filter(lambda x: x != "" and x != "Distance:", distanceLine.split(" ")))

    # Part 2
    timeArr = ["".join(list(filter(lambda x: x != "" and x != "Time:", timeLine.split(" "))))]
    distanceArr = ["".join(list(filter(lambda x: x != "" and x != "Distance:", distanceLine.split(" "))))]

    # CORE FUNC dist <= t*T - t^2
    combos = []
    for timeIndex, timeVal in enumerate(timeArr):
        combos.append(0)
        for i in range(0, int(timeVal)):
            distanceTravelled = (int(timeVal) * i) - (i**2)
            if distanceTravelled > int(distanceArr[timeIndex]):
               combos[timeIndex] += 1

    print(combos)

    print(reduce(lambda x, y: x * y, combos))


if __name__ == "__main__":
    main()
