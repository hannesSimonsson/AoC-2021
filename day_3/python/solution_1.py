def parse_file(file):
    with open(file) as f:
        input = f.read().splitlines()

    return input


if __name__ == "__main__":
    input = parse_file("../input_1.txt")

    gamma_acc = [0]*len(input[0])
    epsilon_acc = [0]*len(input[0])
    for binary in input:
        index = 0
        for bit in binary:
            if bit == '1':
                gamma_acc[index] += 1
            else:
                epsilon_acc[index] += 1

            index += 1

    input_length = len(input)/2
    gamma = ''.join(map(lambda bit: '1' if bit > input_length else '0', gamma_acc))
    epsilon = ''.join(map(lambda bit: '0' if bit > input_length else '1', gamma_acc))

    print(int(gamma,2)*int(epsilon,2))