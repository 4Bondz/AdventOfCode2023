import pprint

def main():
    with open("./day9input.txt", "r") as f:
        lines = f.readlines()

    valueHistory = []

    for i, line in enumerate(lines):
        valueHistory.append(line.strip("\n").split(" "))
        valueHistory[i] = [int(s) for s in valueHistory[i]]

    # This would honestly be easier with recursion but this is fun so we're gonna do iterative

    ans = 0
    sp = 0
    for history in valueHistory:
        total = []
        total.append(history[0])
        toSubtractFrom = int(history[0])
        leftMinList = []
        inputArr = history
        for v in inputArr:
            numDigits = len(str(v))
            print(v, " " * (2 - numDigits), end="")
        print("\n")
        while inputArr.count(0) != len(inputArr) and len(inputArr) != 1:
            # make small arr
            newArr = []
            for i in range(1, len(inputArr)):
                # Pycharm was whining about type specificity, cased to int to resolve
                newArr.append(int(inputArr[i]) - int(inputArr[i - 1]))
            inputArr = newArr
            leftMinList.append(inputArr[0])
            total.append(inputArr[0])
            #print(inputArr)
            for v in inputArr:
                numDigits = len(str(v))
                print(v, " " * (3-numDigits), end="")
            print("\n")
        print(toSubtractFrom - sum(leftMinList))

        next = 0
        for e in range(len(total) - 2, 0, -1):
            next = total[e] - next
        print("NEW FIRST", history[0] - next)
        ans += (history[0] - next)
    print("ANS", ans)


    print(total)







if __name__ == "__main__":
    main()

"""

def main():
    with open("./day9input.txt", "r") as f:
        lines = f.readlines()

    valueHistory = []

    for i, line in enumerate(lines):
        valueHistory.append(line.strip("\n").split(" "))
        valueHistory[i] = [int(s) for s in valueHistory[i]]

    # This would honestly be easier with recursion but this is fun so we're gonna do iterative
    sumOfNextInts = 0
    # Part 1 Extrapolate Right
    for history in valueHistory:
        rightMax = [history[-1]]
        inputArr = history
        print(inputArr)
        while inputArr.count(0) != len(inputArr) and len(inputArr) != 1:
            # make small arr
            newArr = []
            for i in range(0, len(inputArr) - 1):
                # Pycharm was whining about type specificity, cased to int to resolve
                newArr.append(int(inputArr[i + 1]) - int(inputArr[i]))
            inputArr = newArr
            print(inputArr)
            rightMax.append(newArr[-1])
        sumOfNextInts += sum(rightMax)
        print(sum(rightMax))
    print("-" * 20)
    print(sumOfNextInts)

"""