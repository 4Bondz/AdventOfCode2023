from itertools import chain
from multiprocessing import Process, Pool, TimeoutError
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

def crcWrapper(dataList, crc, i):
    x = crcCheckHelper(dataList, crc)
    print(i)
    print("FOUND", x)
    return x

def main():
    with open("./day12input.txt", "r") as f:
        lines = f.readlines()
    lines = [l.strip("\n") for l in lines]

    resolver = []

    for line in lines:
        # Gross parsing, clean up later
        [datagram, crcpacket] = line.split(" ")

        datagram = (datagram + "?") * 5
        datagram = datagram[:-1]

        crcpacket = (crcpacket + ",") * 5
        crcpacket = crcpacket[:-1]

        crcpacket = crcpacket.split(',')
        crcpacket = [[int(each), "*"] for each in crcpacket]
        crcpacket = list(chain.from_iterable(crcpacket))
        crcpacket.pop()

        resolver.append((list(datagram), crcpacket))

    count = 0
    input = []
    total = 0

    for i,line in enumerate(resolver):
        crc = line[1]
        dataList = line[0]
        print(line)
        input.append((dataList, crc, i))

        crcSum = 0

        for maybeInt in crc:
            if type(maybeInt) == int:
                crcSum += maybeInt


    with Pool(processes=4) as pool:
        for i in pool.starmap(crcWrapper, input):
            total += i
    print(total)

if __name__ == "__main__":
    main()

# 12886 is too high
# 9266 is too high
# Too many options slipped through
# GOT IT


# TEST THE OTHER WAY TOMORROW! #
# THe  other way being "use the periods as breakpoints

