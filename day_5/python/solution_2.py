import solution_1 as sol

input = sol.parse_input('../input_1.txt')
grid = sol.draw_grid_lines(input, True)
print(sol.calculate_grid(grid))