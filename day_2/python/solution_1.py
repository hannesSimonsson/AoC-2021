def parse_file(file):
    with open(file) as f:
        input = [(line.split(" ")[0], int(line.split(" ")[1]))
                 for line in f.read().splitlines()]

    return input


if __name__ == "__main__":
    input = parse_file("../input_1.txt")

    depth = 0
    horizontal = 0

    for command, value in input:
        if command == "forward":
            horizontal += value
        elif command == "down":
            depth += value
        elif command == "up":
            depth -= value

    print(depth*horizontal)
