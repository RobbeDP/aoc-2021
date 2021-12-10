from task1 import read_input, mark, bingo_row, bingo_col, get_score


def get_total_score(numbers, boards):
    not_won = set(range(len(boards)))

    for number in numbers:
        for index, board in enumerate(boards):
            if index in not_won:
                mark(number, board)

                if bingo_row(board) or bingo_col(board):
                    not_won.remove(index)

                if len(not_won) == 0:
                    return number * get_score(boards[index])

    return -1


if __name__ == '__main__':
    n, b = read_input('input.txt')
    print(get_total_score(n, b))
