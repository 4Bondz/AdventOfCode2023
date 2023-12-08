import re
import sys
from tqdm import tqdm

SEED_SPLIT = r"seeds: "
REG_SPLIT = r"seed-to-soil map:|soil-to-fertilizer map:|fertilizer-to-water map:|water-to-light " \
            "map:|light-to-temperature map:|temperature-to-humidity map:|humidity-to-location map:"
REG_LIST = ["0STS1", "1S1TF", "2FTW", "3WTL", "4LTT", "5TTH", "6HTL"]
MAP_LINE_REG = r"(\d{1,}\s\d{1,}\s\d{1,})"


# PART 1
# EXCELLENT WORK
# Critique? Little slow my dude, you can get faster

def resolveMap(categoryList, value):
    for categoryRange in categoryList:
        inputRange = categoryRange[0]
        outputRange = categoryRange[1]
        inputLow = inputRange[0]
        inputHigh = inputRange[1]
        outputLow = outputRange[0]
        if inputLow <= value <= inputHigh:
            delta = value - inputLow
            return outputLow + delta
    return value



def makeMapFromLine(inputLine):
    # input a line of start with <dst> <src> <range>
    # output a var with [(src_start, sec_end), (dst_start, dst_end)]
    split = inputLine.strip("\n").split(" ")
    return [(int(split[1]), int(split[1]) + int(split[2]) - 1), (int(split[0]), int(split[0]) + int(split[2]) - 1)]


def getSeed(seedInts):
    for seedIndex in range(0, len(seedInts), 2):
        lowSeedVal = seedInts[seedIndex]
        highSeedVal = seedInts[seedIndex] + seedInts[seedIndex + 1]
        for seedIterVal in tqdm(range(lowSeedVal, highSeedVal)):
            yield seedIterVal


def main():
    total = 0
    cardList = []
    regMap = {"0STS1": [], "1S1TF": [], "2FTW": [], "3WTL": [], "4LTT": [], "5TTH": [], "6HTL": []}
    # part 1, 8 mins
    with open("./day5input.txt", "r") as f:
        seedLine = f.readline().strip("\n")
        seeds = list(re.split(SEED_SPLIT, seedLine)[1].split(" "))
        seedInts = [int(s) for s in seeds]

        newSeedInts = []
        # Part 2 processing!

        mapLines = f.readlines()
        inputSelector = -1

        for line in mapLines:
            if re.match(REG_SPLIT, line):
                inputSelector += 1
            elif re.match(MAP_LINE_REG, line):
                r = makeMapFromLine(line)
                regMap[REG_LIST[inputSelector]].append(r)

        for m in regMap.values():
            m.sort(key=lambda x: x[0])

        minSeed = sys.maxsize
        for seed in getSeed(seedInts):
            resolutionStep = 0
            resolverInput = seed
            while resolutionStep < 7:
                resolutionCategory = REG_LIST[resolutionStep]
                resolverInput = resolveMap(regMap[resolutionCategory], resolverInput)
                resolutionStep += 1
            resolvedValue = resolverInput
            if resolvedValue < minSeed:
                minSeed = resolvedValue
        print(minSeed)


if __name__ == "__main__":
    main()
