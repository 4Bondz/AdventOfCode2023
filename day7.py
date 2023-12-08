from functools import reduce


def cardToInt(char):
    # Part 1
    # CHAR_TO_INT_MAP = {'T': 10, "J": 11, "Q": 12, "K": 13, "A": 14}
    # Part 2
    CHAR_TO_INT_MAP = {'T': 10, "J": 0, "Q": 12, "K": 13, "A": 14}
    if '1' <= char <= '9':
        return int(char)
    else:
        return CHAR_TO_INT_MAP[char]


def getBucketFromHand(handList):
    handSet = set(handList)
    countList = []
    for card in handSet:
        countList.append(handList.count(card))

    if len(countList) == 1:
        return 6
    else:
        if 4 in countList:
            return 5
        if (3 in countList) and (2 in countList):
            return 4
        if 3 in countList:
            return 3
        if 2 in countList and (countList.count(2) == 2):
            return 2
        if 2 in countList and (countList.count(2) == 1):
            return 1
        else:
            return 0


def getBucketFromHandPart2(handList):
    JACK = 0
    CHARS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14]
    maxBucket = 0
    if JACK in handList:
        tmp = [*handList]
        tmp.pop(tmp.index(JACK))
        for c in CHARS:
            tmpMax = getBucketFromHandPart2([*tmp, c])
            if tmpMax > maxBucket:
                maxBucket = tmpMax

    handSet = set(handList)
    countList = []
    for card in handSet:
        countList.append(handList.count(card))

    if len(countList) == 1:
        return max(maxBucket, 6)
    else:
        if 4 in countList:
            return max(maxBucket, 5)
        if (3 in countList) and (2 in countList):
            return max(maxBucket, 4)
        if 3 in countList:
            return max(maxBucket, 3)
        if 2 in countList and (countList.count(2) == 2):
            return max(maxBucket, 2)
        if 2 in countList and (countList.count(2) == 1):
            return max(maxBucket, 1)
        else:
            return max(maxBucket, 0)


def main():
    hands = []
    buckets = [[] for x in range(7)]
    # 5 of kind
    # 4 of kind
    # full house
    # 3 of a kind
    # 2 pair
    # 1 pair
    # high card
    with open("./day7input.txt", "r") as f:
        lines = f.readlines()

    for line in lines:
        [hand, score] = line.split(" ")
        hand = [cardToInt(char) for char in hand]
        score = int(score)
        bucket = getBucketFromHandPart2(hand)
        buckets[bucket].append([hand, score])

    # SORT_FUNC = [sortHighCard, sort1Pair, sort2Pair, sort3OfKind, sortFulLHouse, sort4OfKind, sort5OfKind]

    # for i in range(len(buckets)):
    #     buckets[i] = SORT_FUNC[i](buckets[i])

    for i in range(len(buckets)):
        buckets[i].sort(key=lambda x: x[0])

    handRank = []
    for x in buckets:
        handRank += x

    total = 0
    i = len(handRank) - 1
    while i >= 0:
        print(handRank[i][1], "*", i + 1)
        total += handRank[i][1] * (i + 1)
        i -= 1

    print(total)


if __name__ == "__main__":
    main()

""" Part 1

from functools import reduce


def cardToInt(char):
    CHAR_TO_INT_MAP = {'T': 10, "J": 11, "Q": 12, "K": 13, "A": 14}
    if '1' <= char <= '9':
        return int(char)
    else:
        return CHAR_TO_INT_MAP[char]


def getBucketFromHand(handList):
    handSet = set(handList)
    countList = []
    for card in handSet:
        countList.append(handList.count(card))

    if len(countList) == 1:
        return 6
    else:
        if 4 in countList:
            return 5
        if (3 in countList) and (2 in countList):
            return 4
        if 3 in countList:
            return 3
        if 2 in countList and (countList.count(2) == 2):
            return 2
        if 2 in countList and (countList.count(2) == 1):
            return 1
        else:
            return 0

    pass

def main():
    hands = []
    buckets = [[] for x in range(7)]
    # 5 of kind
    # 4 of kind
    # full house
    # 3 of a kind
    # 2 pair
    # 1 pair
    # high card
    with open("./day7input.txt", "r") as f:
        lines = f.readlines()

    for line in lines:
        [hand, score] = line.split(" ")
        hand = [cardToInt(char) for char in hand]
        score = int(score)
        bucket = getBucketFromHand(hand)
        buckets[bucket].append([hand, score])

    #SORT_FUNC = [sortHighCard, sort1Pair, sort2Pair, sort3OfKind, sortFulLHouse, sort4OfKind, sort5OfKind]

    # for i in range(len(buckets)):
    #     buckets[i] = SORT_FUNC[i](buckets[i])

    for i in range(len(buckets)):
        buckets[i].sort(key=lambda x: x[0])

    handRank = []
    for x in buckets:
        handRank += x

    total = 0
    i = len(handRank) - 1
    while i >= 0:
        print(handRank[i][1], "*", i + 1)
        total += handRank[i][1] * (i + 1)
        i -= 1

    print(total)


if __name__ == "__main__":
    main()

"""
