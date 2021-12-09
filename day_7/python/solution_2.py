from solution_1 import parse_input

input = parse_input('../input_1.txt')

mean = int(sum(input)/len(input))
fuel = []
for distance in input:
    if distance > mean:
        for cost in range(distance-mean+1):
            fuel.append(cost)
    elif distance < mean:
        for cost in range(mean-distance+1):
            fuel.append(cost)

print(sum(fuel), mean)