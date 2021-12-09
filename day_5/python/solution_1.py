import numpy as np

def parse_input(file):
    # [[[int(x), int(y)],[int(x), int(y)]]]
    with open(file) as f:
        input = f.read().splitlines()
        input = [[[int(num) 
                    for num in coord.split(',')] 
                        for coord in line.split(' -> ')] 
                            for line in input]

    return input


def calculate_grid(grid):
    result = 0
    for line in grid:
        cross_sections = filter((lambda x: x > 1), line)
        result += len(list(cross_sections))

    return result


def draw_grid_lines(input, diagonal):
    grid = np.zeros((1000, 1000), dtype=int)

    for coord in input:
        x = coord[0][0]
        y = coord[0][1]
        end_x = coord[1][0]
        end_y = coord[1][1]  
    
        if (x == end_x or y == end_y) or diagonal:
            grid[y][x] += 1
    
            while(not (x == end_x and y == end_y)):
                if x < end_x:
                    x += 1
                elif x > end_x:
                    x -=1
        
                if y < end_y:
                    y += 1
                elif y > end_y:
                    y -= 1       
        
                grid[y][x] += 1

    return grid

if __name__ == '__main__':
    input = parse_input('../input_1.txt')
    grid = draw_grid_lines(input, False)
    print(calculate_grid(grid))