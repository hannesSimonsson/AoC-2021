def parse_file(file):
    with open(file) as f:
        input = f.read().splitlines()

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
