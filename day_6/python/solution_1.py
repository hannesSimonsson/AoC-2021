def parse_input(input_text):
    with open(input_text) as f:
        input = f.read().split(',')
        return [int(num) for num in input]

def population(fish, days):
    for _ in range(days):
        for i in range(len(fish)): 
            fish[i] -= 1
    
            if fish[i] == -1:
                fish[i] = 6
                fish.append(8)
    
    return fish
        

if __name__ == '__main__':
    fish = parse_input('../input_1.txt')
    days = 80
    fish = population(fish, days)
    print(len(fish))