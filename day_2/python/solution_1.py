def parse_file(file):
    f = open(file, "r")
    input = []
    for line in f:
        line = line.strip("\n")
        commands, value = line.split(" ")
        input.append([commands, int(value)])
    f.close()

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
