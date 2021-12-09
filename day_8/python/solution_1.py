with open('../input_1.txt') as f:
    input = f.read().splitlines()
    output = []
    for seq in input:
        output += seq.split(' ')

acc = 0
for sequence in output:
    if (len(sequence) in [7, 4, 3, 2]):
        acc += 1

print(acc)