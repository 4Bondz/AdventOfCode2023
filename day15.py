def main():
    with open("./day15input.txt", "r") as f:
        lines = f.readlines()
    lines = [l.strip("\n") for l in lines]

    resolver = lines[0].split(",")
    total = 0

    for string in resolver:
        hashValue = 0
        for char in string:
            hashValue += ord(char)
            hashValue *= 17
            hashValue = hashValue % 256
        total += hashValue

    print(total)



    print("X")


if __name__ == "__main__":
    main()
