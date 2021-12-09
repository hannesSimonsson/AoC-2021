import solution_1 as parse

def filter_index(input, index, setting):
    acc_1 = 0
    acc_0 = 0
    binary_list = list(input)
    for binary in input:
        if binary[index] == 1:
            acc_1 += 1
        else:
            acc_0 += 1

    if setting:
        check = acc_1 >= acc_0
    else:
        check = acc_1 < acc_0

    if check:
        for binary in input:
            if binary[index] == 0:
                binary_list.remove(binary)
    else:
        for binary in input:
            if binary[index] == 1:
                binary_list.remove(binary)

    return binary_list


def filter(input, setting):
    for index in range(len(input[0])):
        if setting:
            input = filter_index(input, index, setting)
        else:
            input = filter_index(input,index, setting)

        if len(input) == 1:
            break
    
    return input

input = parse.parse_file("../input_1.txt")
input = list([int(bit) for bit in list(binary)] for binary in input)

oxygen_generator_rating = list(input)
co2_scrubber_rating = list(input)

oxygen_generator_rating = filter(oxygen_generator_rating, True)
co2_scrubber_rating = filter(co2_scrubber_rating, False)

oxygen_generator_rating = ''.join([str(bit) for bit in oxygen_generator_rating[0]])
co2_scrubber_rating = ''.join([str(bit) for bit in co2_scrubber_rating[0]])

print(int(oxygen_generator_rating, 2)*int(co2_scrubber_rating, 2))