from task1 import read_input, is_opening_bracket, brackets_correspond
from collections import deque

corresponding_brackets = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}


completion_scores = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}


def check_line(line):
    stack = deque()
    score = 0

    for char in line:
        if is_opening_bracket(char):
            stack.append(char)
        else:
            top_char = stack.pop()
            if not brackets_correspond(top_char, char):
                return score

    while stack:
        corresponding_bracket = corresponding_brackets[stack.pop()]
        score = score * 5 + completion_scores[corresponding_bracket]

    return score


def check_file(file):
    scores = []

    for line in file:
        score = check_line(line)

        if score != 0:
            scores.append(score)

    return sorted(scores)[len(scores) // 2]


if __name__ == '__main__':
    print(check_file(read_input('input.txt')))
