def parse_input(input_text):
    with open(input_text) as f:
        input = f.read().splitlines()
        draw_numbers = [int(number) for number in input.pop(0).split(',')]
    
        boards = []
        board = []
        for row in input:
            if row != '':
                row = row.split(' ')
                row = list(filter(lambda num: num != '', row))
                
                board.append([[int(num), False] for num in row])
            else:
                if board != []:
                    boards.append(board)
                    board = []
        
        return boards, draw_numbers


def check_winning_board(board):
    rows = []
    columns = []

    row_index = 0
    for row in board:
        column_index = 0
        for num in row:
            if num[1]:
                rows.append(row_index)
                columns.append(column_index)
            column_index += 1
        row_index += 1
   
    
    columns.sort()

    acc_row = 1
    acc_column = 1
    for i in range(len(rows)-1):
        if rows[i] == rows[i+1]:
            acc_row += 1
        else:
            acc_row = 1
        
        if columns[i] == columns[i+1]:
            acc_column += 1
        else:
            acc_column = 1

        if acc_row >= 5 or acc_column >= 5:
            return True
    
    return False

def find_bingo(boards, draw_numbers):
    for d_num in draw_numbers:
        for board in boards:
            for row in board:
                for num in row:
                    if num[0] == d_num:
                        num[1] = True

            if check_winning_board(board):
                return (d_num, board)
    
    return boards

def calculate_board(winner):    
    # winner [int(winning_number), board[[[int, bool]]]
    board = winner[1]
    board_sum = 0
    for row in board:
        for num in row:
            if not num[1]:
                board_sum += num[0]

    return board_sum*winner[0]


if __name__ == '__main__':
    boards, draw_numbers = parse_input('../input_1.txt')
    winner = find_bingo(boards, draw_numbers)
    print(calculate_board(winner))