def crcCheckHelper(dataList, crc):
    # base case
    if len(crc) == 0:
        if "#" in dataList:
            return 0
        return 1

    if len(dataList) == 0:
        return 0

    test = crc[0]
    sub = 0
    if test == "*":
        sub = 1
    else:
        sub = test

    r = 0

    if test == "*":
        if dataList[0] == "?" or dataList[0] == ".":
            # Success!
            r += crcCheckHelper(dataList[1:], crc[1:])
        else:
            return r
    else:
        for i in range(0, len(dataList) - sub + 1):
            # Must be all #/?
            if "." in dataList[i: i + test] or "#" in dataList[0:i]:
                continue
            else:
                r += crcCheckHelper(dataList[i + test:], crc[1:])
    return r


from itertools import chain

def main():
    with open("./day12test.txt", "r") as f:
        lines = f.readlines()
    lines = [l.strip("\n") for l in lines]

    resolver = []

    for line in lines:
        [datagram, crcpacket] = line.split(" ")
        crcpacket = crcpacket.split(',')
        crcpacket = [[int(each), "*"] for each in crcpacket]
        crcpacket = list(chain.from_iterable(crcpacket))
        crcpacket.pop()

        resolver.append((list(datagram), crcpacket))

    count = 0

    for line in resolver:
        crc = line[1]
        dataList = line[0]
        print(line)

        crcSum = 0

        for maybeInt in crc:
            if type(maybeInt) == int:
                crcSum += maybeInt
        out = crcCheckHelper(dataList, crc)
        print(out)

        count += out


    print("X", count)


if __name__ == "__main__":
    main()


"""
def crcCheckHelper(dataList, crc):
    # base case
    if len(crc) == 0:
        if "#" in dataList:
            return 0
        return 1

    if len(dataList) == 0:
        return 0

    test = crc[0]
    sub = 0
    if test == "*":
        sub = 1
    else:
        sub = test

    r = 0

    if test == "*":
        if dataList[0] == "?" or dataList[0] == ".":
            # Success!
            r += crcCheckHelper(dataList[1:], crc[1:])
        else:
            return r
    else:
        for i in range(0, len(dataList) - sub + 1):
            # Must be all #/?
            if "." in dataList[i: i + test] or "#" in dataList[0:i]:
                continue
            else:
                r += crcCheckHelper(dataList[i + test:], crc[1:])
    return r


from itertools import chain

def main():
    with open("./day12input.txt", "r") as f:
        lines = f.readlines()
    lines = [l.strip("\n") for l in lines]

    resolver = []

    for line in lines:
        [datagram, crcpacket] = line.split(" ")
        crcpacket = crcpacket.split(',')
        crcpacket = [[int(each), "*"] for each in crcpacket]
        crcpacket = list(chain.from_iterable(crcpacket))
        crcpacket.pop()

        resolver.append((list(datagram), crcpacket))

    count = 0

    for line in resolver:
        crc = line[1]
        dataList = line[0]
        print(line)

        crcSum = 0

        for maybeInt in crc:
            if type(maybeInt) == int:
                crcSum += maybeInt
        out = crcCheckHelper(dataList, crc)
        print(out)

        count += out


    print("X", count)


if __name__ == "__main__":
    main()

# 12886 is too high
# 9266 is too high
# Too many options slipped through

"""