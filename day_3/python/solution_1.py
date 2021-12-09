def parse_file(file):
    with open(file) as f:
        input = f.read().splitlines()

    return input

def get_gamma_epsilon(input):
    gamma_acc = [0]*len(input[0])
    epsilon_acc = [0]*len(input[0])
    for binary in input:
        index = 0
        for bit in binary:
            gamma_acc[index] += int(bit)
            epsilon_acc[index] += not int(bit)

            index += 1

    input_length = len(input)/2

    return map(lambda bit: '1' if bit > input_length else '0', gamma_acc), map(lambda bit: '0' if bit > input_length else '1', gamma_acc)

if __name__ == "__main__":
    input = parse_file("../input_1.txt")
    input = [[int(bit) for bit in list(binary)] for binary in input]

#    gamma = "".join([
#        ('1' if sum(couple) > len(input)/2 else '0')
#        for couple in zip(*input)
#    ])
#    epsilon = "".join([str(int(not int(bit))) for bit in gamma])
#
#    print(int(gamma,2)*int(epsilon,2))

    gamma, epsilon = get_gamma_epsilon(input)

    print(int(''.join(gamma),2)*int(''.join(epsilon),2))
