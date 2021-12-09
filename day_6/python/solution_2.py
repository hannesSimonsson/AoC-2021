from solution_1 import parse_input

fish = parse_input('../input_1.txt')
days = 256

acc = [0]*9
for timer in fish:
    acc[timer] += 1

for _ in range(days):
    acc = acc[1:7] + [acc[7] + acc[0]] + acc[8:9] + [acc[0]]

print(sum(acc))