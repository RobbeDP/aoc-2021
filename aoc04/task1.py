def read_input(file_name):
    with open(file_name) as input_file:
        numbers = list(map(lambda x: int(x), input_file.readline().rstrip('\n').split(',')))

        input_file.readline()

        boards = []
        current_board = []

        line = input_file.readline()
        while line:
            line = line.rstrip('\n')

            if line == '':
                boards.append(current_board)
                current_board = []
            else:
                current_board.append(list(map(lambda x: (int(x), False), line.split())))

            line = input_file.readline()

        boards.append(current_board)
        return numbers, boards


def mark(number, board):
    for i, row in enumerate(board):
        for j, col in enumerate(row):
            if col[0] == number:
                board[i][j] = (col[0], True)


def bingo_row(board):
    for row in board:
        bingo = True
        for col in row:
            if not col[1]:
                bingo = False
                break

        if bingo:
            return True

    return False


def bingo_col(board):
    for i in range(len(board[0])):
        bingo = True
        for j in range(len(board)):
            if not board[j][i][1]:
                bingo = False
                break

        if bingo:
            return True

    return False


def get_score(board):
    score = 0
    for row in board:
        for number, marked in row:
            if not marked:
                score += number

    return score


def get_total_score(numbers, boards):
    for number in numbers:
        for board in boards:
            mark(number, board)
            if bingo_row(board) or bingo_col(board):
                return number * get_score(board)

    return -1


if __name__ == '__main__':
    n, b = read_input('input.txt')
    print(get_total_score(n, b))
