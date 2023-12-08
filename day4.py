cardInfo = {"#": int, "q": int, "w": int}
cardList = list[cardInfo]


def main():
    total = 0
    cardList = []
    # part 1, 8 mins
    with open("./day4input.txt", "r") as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            splitLine = line.split("|")
            winnersWithHeader = splitLine[0].strip("\n")
            scratchOffNumbers = splitLine[1].strip("\n")
            winnersString = winnersWithHeader.split(":")[1]

            winnersList = winnersString.split(" ")
            winnersList = list(filter(lambda x: x != "", winnersList))
            scratchOffList = scratchOffNumbers.split(" ")
            scratchOffList = list(filter(lambda x: x != '', scratchOffList))
            card = {"#": i + 1, "q": 1, "w": 0}
            numWinners = 0
            for winner in winnersList:
                if winner in scratchOffList:
                    numWinners += 1
            card["w"] = numWinners
            cardList.append(card)
            # Part 1
            # if numWinners == 1:
            #     total += 1
            # elif numWinners > 1:
            #     total += 2 ** (numWinners - 1)
    print("total:", cardList)

    for i, card in enumerate(cardList):
        winners = card["w"]
        while winners > 0:
            cardList[i + winners]["q"] += card["q"]
            winners -= 1

    total = 0
    for card in cardList:
        total += card["q"]

    print(total)

if __name__ == "__main__":
    main()

""" Part 1

 total = 0
    cardList = []
    # part 1, 8 mins
    with open("./day4input.txt", "r") as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            splitLine = line.split("|")
            winnersWithHeader = splitLine[0].strip("\n")
            scratchOffNumbers = splitLine[1].strip("\n")
            winnersString = winnersWithHeader.split(":")[1]

            winnersList = winnersString.split(" ")
            winnersList = list(filter(lambda x: x != "", winnersList))
            scratchOffList = scratchOffNumbers.split(" ")
            scratchOffList = list(filter(lambda x: x != '', scratchOffList))
            card = {"#": i + 1, "q": 1, "w": 0}
            numWinners = 0
            for winner in winnersList:
                if winner in scratchOffList:
                    numWinners += 1
            # Part 2
            # card["w"] = numWinners
            # cardList.append(card)
            # Part 1
            if numWinners == 1:
                total += 1
            elif numWinners > 1:
                total += 2 ** (numWinners - 1)
    print("total:", cardList)

    # Part 2
    # for i, card in enumerate(cardList):
    #     winners = card["w"]
    #     while winners > 0:
    #         cardList[i + winners]["q"] += card["q"]
    #         winners -= 1
    # 
    # total = 0
    # for card in cardList:
    #     total += card["q"]

    print(total)



"""

""" Part 2

def main():
    total = 0
    cardList = []
    # part 1, 8 mins
    with open("./day4input.txt", "r") as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            splitLine = line.split("|")
            winnersWithHeader = splitLine[0].strip("\n")
            scratchOffNumbers = splitLine[1].strip("\n")
            winnersString = winnersWithHeader.split(":")[1]

            winnersList = winnersString.split(" ")
            winnersList = list(filter(lambda x: x != "", winnersList))
            scratchOffList = scratchOffNumbers.split(" ")
            scratchOffList = list(filter(lambda x: x != '', scratchOffList))
            card = {"#": i + 1, "q": 1, "w": 0}
            numWinners = 0
            for winner in winnersList:
                if winner in scratchOffList:
                    numWinners += 1
            card["w"] = numWinners
            cardList.append(card)
            # Part 1
            # if numWinners == 1:
            #     total += 1
            # elif numWinners > 1:
            #     total += 2 ** (numWinners - 1)
    print("total:", cardList)

    for i, card in enumerate(cardList):
        winners = card["w"]
        while winners > 0:
            cardList[i + winners]["q"] += card["q"]
            winners -= 1

    total = 0
    for card in cardList:
        total += card["q"]

    print(total)


"""