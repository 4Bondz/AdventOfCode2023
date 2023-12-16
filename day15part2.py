from collections import defaultdict
import re

# LESSON:
# If your code gets gross and unwieldly, you probably weren't paying enoug attention
# Either write better code or delete it and do it again later
def doHash(string):
        hashValue = 0
        for char in string:
            hashValue += ord(char)
            hashValue *= 17
            hashValue = hashValue % 256
        return hashValue
def main():
    with open("./day15input.txt", "r") as f:
        lines = f.readlines()
    lines = [l.strip("\n") for l in lines]

    resolver = lines[0].split(",")
    # end result is dict of lists
    # writing a dict that maps the 2 letter keys to boxes so I can do adds and removals in O(1)
    focusDict = defaultdict(lambda: [])
    lensToBoxDict = defaultdict(lambda: [])


    labelRegex = re.compile(r"([a-z]|[A-Z]){1,}(?=\-|\=)")
    operatorRegex = re.compile(r"(\=|\-)")
    digitRegex = re.compile(r"(?<=\-|\=)[0-9]")
    storedDataDigitRegex = re.compile(r"(?<=([a-z]|[A-Z]))[0-9]")
    storedDataLabelRegex = re.compile(r"([a-z]|[A-Z]){1,}")

    for lens in resolver:
        operator = re.search(operatorRegex, lens)[0]
        label = re.search(labelRegex, lens)[0]
        digit = re.search(digitRegex, lens)

        if digit:
            digit = digit[0]
        else:
            digit = ""
        assert lens == label + operator + digit

        destinationBox = doHash(label)

        if operator == "=":
            potentialMatchesForOldLabelAndDigit = focusDict[destinationBox]
            foundMatch = False
            for testIndex, testMatch in enumerate(potentialMatchesForOldLabelAndDigit):
                if testMatch.split("=")[0] == label:
                    focusDict[destinationBox][testIndex] = lens
                    del lensToBoxDict[testMatch]
                    lensToBoxDict[lens] = destinationBox
                    foundMatch = True
                    break
            if not foundMatch:
                focusDict[destinationBox].append(lens)
                lensToBoxDict[lens] = destinationBox
        elif operator == "-":
            potentialMatchesForOldLabelAndDigit = focusDict[destinationBox]
            for testIndex, testMatch in enumerate(potentialMatchesForOldLabelAndDigit):
                if testMatch.split("=")[0] == label:
                    focusDict[destinationBox].remove(testMatch)
                    try:
                        del lensToBoxDict[testMatch]
                    except:
                        print("COULDN'T FIND", testMatch, "TO REMOVE IN LENSTOBOXDICT")
                    print("REMOVED:", testMatch)
                    break
        else:
            raise Exception("Bad Operator")

    power = 0
    for box in focusDict.keys():
        for lensIndex, lens in enumerate(focusDict[box]):
            digit = lens.split("=")[1]
            tp = (box + 1) * (lensIndex + 1) * int(digit)
            #print(tp)
            power += tp
    print(power)


if __name__ == "__main__":
    main()

    # 655445 is too high
    # 652994 is too high
    # 246771 is too high