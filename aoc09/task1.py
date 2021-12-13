def read_input(file_name):
    with open(file_name) as input_file:
        height_map = []
        for line in input_file:
            height_map.append(list(map(lambda x: int(x), line.rstrip('\n'))))

        return height_map


def add_positions(pos1, pos2):
    return [pos1[0] + pos2[0], pos1[1] + pos2[1]]


def get_risk(height_map):
    offsets = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    risk_level = 0
    for i, row in enumerate(height_map):
        for j, height_value in enumerate(row):
            low_point = True
            for offset in offsets:
                neighbour_pos = add_positions([i, j], offset)
                if 0 <= neighbour_pos[0] < len(height_map) and 0 <= neighbour_pos[1] < len(height_map[i]):
                    neighbour_val = height_map[neighbour_pos[0]][neighbour_pos[1]]
                    if neighbour_val <= height_value:
                        low_point = False
                        break

            if low_point:
                risk_level += 1 + height_value

    return risk_level


if __name__ == '__main__':
    print(get_risk(read_input('input.txt')))
