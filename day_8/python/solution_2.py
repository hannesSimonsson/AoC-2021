with open('../input_2.txt') as f:
    input = [[line] for line in f.read().splitlines()]
    input = [seq[0].split(' | ') for seq in input]
    output = []
    for line in input:
        output.append([line[0].split(' '), line[1].split(' ')])


def contains_number(sequence, number, controll):
    return sum(section in number for section in sequence) == controll

def decode_number(sequence, decoded_list):
    for i in range(len(decoded_list)):
        if len(decoded_list[i]) <= len(sequence):
            if sum(char in decoded_list[i] for char in sequence) == len(sequence):
                return i
        else:
            if sum(char in decoded_list[i] for char in sequence) == len(decoded_list[i]):
                return i


acc = 0
decoded = 10*['0']
for line in output:
    number = ''
    for instruction in line[0]:
        chars = len(instruction)
        if chars == 7:
            decoded[8] = instruction
        elif chars == 4:
            decoded[4] = instruction
        elif chars == 3:
            decoded[7] = instruction
        elif chars == 2:
            decoded[1] = instruction
    
    for instruction in line[0]:
        chars = len(instruction)
        if chars == 6:
            if contains_number(instruction, decoded[1], 1):
                decoded[6] = instruction
            elif contains_number(instruction, decoded[4], 4):
                decoded[9] = instruction
            else:
                decoded[0] = instruction

        elif chars == 5:
            if contains_number(instruction, decoded[1], 2):
                decoded[3] = instruction
            elif contains_number(instruction, decoded[4], 3):
                decoded[5] = instruction
            else:
                decoded[2] = instruction

    for output in line[1]:
        print(output)
        number += str(decode_number(output, decoded))

    print(int(number)) 
    acc += int(number)

print(acc)