from collections import deque


def read_input(file_name):
    with open(file_name) as input_file:
        return list(map(lambda x: x.rstrip('\n'), input_file))


error_scores = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}


def is_opening_bracket(char):
    return char in ['(', '[', '{', '<']


def brackets_correspond(opening_bracket, closing_bracket):
    return (opening_bracket == '(' and closing_bracket == ')') or \
           (opening_bracket == '[' and closing_bracket == ']') or \
           (opening_bracket == '{' and closing_bracket == '}') or \
           (opening_bracket == '<' and closing_bracket == '>')


def check_line(line):
    stack = deque()

    for char in line:
        if is_opening_bracket(char):
            stack.append(char)
        else:
            top_char = stack.pop()
            if not brackets_correspond(top_char, char):
                return error_scores[char]

    return 0


def check_file(file):
    score = 0

    for line in file:
        score += check_line(line)

    return score


if __name__ == '__main__':
    print(check_file(read_input('input.txt')))
