def parse_file(text_file):
    f = open(text_file, "r")
    input = []
    for line in f:
        input.append(int(line))
    f.close()

    return input


if __name__ == "__main__":

    input = parse_file("../input_1.txt")

    preDepth = input[0]
    acc = 0

    for depth in input:
        if depth > preDepth:
            acc += 1

        preDepth = depth

    print(acc)
