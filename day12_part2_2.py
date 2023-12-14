from time import time
from itertools import chain
import re

# LESSONS
# GIGO IS IMPORTANT, REMMEBER IT
# IF YOU HAVE A PROBLEM, MAKE SURE INPUTS ARE SANE

# MEMOIZATION!
# DYNAMIC PROGRAMMING!
# DON"T SOLVE THE SAME PROBLEM TWICE!

memorize = {}
uses = 0
def crcCheckHelper(dataList, crc):
    try:
        global memorize, uses
        r = memorize[("".join(dataList), "".join([str(j) for j in crc]))]
        if r:
            uses += 1
            return r
    except:
        pass
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
            memorize[("".join(dataList), "".join([str(j) for j in crc]))] = r
            return r
    else:
        for i in range(0, len(dataList) - sub + 1):
            # Must be all #/?
            if "." in dataList[i: i + test] or "#" in dataList[0:i]:
                continue
            else:
                r += crcCheckHelper(dataList[i + test:], crc[1:])
    memorize[("".join(dataList), "".join([str(j) for j in crc]))] = r
    return r

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

    resolver.sort(key=lambda x: len(x[0]))



    for line in resolver:
        start = time()
        crc = line[1]
        dataList = line[0]
        print(line)

        crcSum = 0

        for maybeInt in crc:
            if type(maybeInt) == int:
                crcSum += maybeInt
        out = crcCheckHelper(dataList, crc)
        print(out)
        end = time()
        print(end - start, " Seconds")
        global memorize, uses
        print("Memorize has", len(memorize.keys()), " keys remembered")
        print("Memorize has been used", str(uses), "times")

        count += out


    print("X", count)

if __name__ == "__main__":
    main()

# 12886 is too high
# 9266 is too high
# Too many options slipped through