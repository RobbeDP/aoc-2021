def read_input(file_name):
    with open(file_name) as input_file:
        height_map = []
        for line in input_file:
            height_map.append(list(map(lambda x: int(x), line.rstrip('\n'))))

        return height_map


# Return all in bound neighbours of the given position.
def get_neighbours(position, height_map):
    neighbours = []
    row, col = position

    if row + 1 < len(height_map):
        neighbours.append((row + 1, col))
    if row - 1 >= 0:
        neighbours.append((row - 1, col))
    if col + 1 < len(height_map[0]):
        neighbours.append((row, col + 1))
    if col - 1 >= 0:
        neighbours.append((row, col - 1))

    return neighbours


def get_risk(height_map):
    risk = 0

    for i, row in enumerate(height_map):
        for j, height in enumerate(row):
            low_point = True
            position = (i, j)

            for n_row, n_col in get_neighbours(position, height_map):
                if height_map[n_row][n_col] <= height:
                    low_point = False
                    break

            if low_point:
                risk += 1 + height

    return risk


if __name__ == '__main__':
    print(get_risk(read_input('input.txt')))
