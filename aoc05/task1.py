import re


class Line:
    def __init__(self, x1, y1, x2, y2):
        self.fst = (x1, y1)
        self.snd = (x2, y2)

    def __str__(self):
        return f'Line({self.fst}, {self.snd})'

    def __repr__(self):
        return f'Line({self.fst}, {self.snd})'


def read_input(file_name):
    with open(file_name) as input_file:
        lines = []
        for line in input_file:
            match = re.match(r'(\d+),(\d+) -> (\d+),(\d+)', line)
            lines.append(Line(int(match[1]), int(match[2]), int(match[3]), int(match[4])))

        return lines


def get_size(lines):
    max_x = 0
    max_y = 0
    for line in lines:
        if line.fst[0] > max_x:
            max_x = line.fst[0]
        if line.snd[0] > max_x:
            max_x = line.snd[0]

        if line.fst[1] > max_y:
            max_y = line.fst[1]
        if line.snd[1] > max_y:
            max_y = line.snd[1]

    return max_x + 1, max_y + 1


def init_grid(width, height):
    grid = []
    for _ in range(height):
        grid.append([0] * width)

    return grid


def positions_equal(pos1, pos2):
    return pos1[0] == pos2[0] and pos1[1] == pos2[1]


def get_offset(val1, val2):
    if val1 < val2:
        return 1
    elif val1 > val2:
        return -1
    else:
        return 0


def draw_lines(grid, lines, consider_diagonal):
    for line in lines:
        if consider_diagonal or \
                (not consider_diagonal and (line.fst[0] == line.snd[0] or line.fst[1] == line.snd[1])):
            x_offset = get_offset(line.fst[0], line.snd[0])
            y_offset = get_offset(line.fst[1], line.snd[1])

            current_pos = list(line.fst)
            while not positions_equal(current_pos, line.snd):
                grid[current_pos[1]][current_pos[0]] += 1
                current_pos[0] += x_offset
                current_pos[1] += y_offset

            grid[current_pos[1]][current_pos[0]] += 1


def find_overlap_amount(lines, consider_diagonal):
    width, height = get_size(lines)

    grid = init_grid(width, height)
    draw_lines(grid, lines, consider_diagonal)

    overlap_amount = 0
    for row in grid:
        for col in row:
            if col > 1:
                overlap_amount += 1

    return overlap_amount


if __name__ == '__main__':
    input_lines = read_input('input.txt')
    print(find_overlap_amount(input_lines, False))
