from statistics import median as med

def parse_input(input):
    with open(input) as f:
        input = [int(num) for num in f.read().split(',')]
    
    return input

if __name__ == '__main__':
    input = parse_input('../input_1.txt')
    
    median = int(med(input))
    fuel = []
    for distance in input:
        if distance > median:
            fuel.append(distance-median)
        elif distance < median:
            fuel.append(median-distance)
    
    print(sum(fuel), median)
