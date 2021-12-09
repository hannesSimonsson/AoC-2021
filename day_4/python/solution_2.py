import solution_1 as sol

def remove_next_bingo(boards, draw_numbers):
    for d_num in draw_numbers:
        index_board = 0
        for board in boards:
            for row in board:
                for num in row:
                    if num[0] == d_num:
                        num[1] = True

            if sol.check_winning_board(board):
                boards.pop(index_board)
                return (d_num, boards)

            index_board += 1

boards, draw_numbers = sol.parse_input('../input_1.txt')

losers = remove_next_bingo(boards, draw_numbers)
while len(losers[1]) > 1:
    losers = remove_next_bingo(boards, draw_numbers)
    boards = losers[1]

loser = sol.find_bingo(boards, draw_numbers)
print(sol.calculate_board(loser))