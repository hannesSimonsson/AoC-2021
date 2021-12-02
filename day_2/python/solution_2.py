import solution_1 as parser

input = parser.parse_file("../input_1.txt")  # [[string, int]]

depth = 0
horizontal = 0
aim = 0

for command, value in input:

    if command == "forward":
        horizontal += value
        depth += value*aim
    elif command == "down":
        aim += value
    elif command == "up":
        aim -= value

print(depth*horizontal)
