import solution_1 as parser

input = parser.parse_file("../input_1.txt")  # [int]

window = 3
preDepth = sum(input[0:window])
acc = 0

for i in range(0, len(input)):
    depth = sum(input[i:i+window])

    if depth > preDepth:
        acc += 1

    preDepth = depth

print(acc)
