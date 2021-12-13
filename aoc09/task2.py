from task1 import read_input, get_neighbours
from functools import reduce


# Return all low points in the given height map.
# These are positions whose height value is smaller than the height
# values of their neighbours.
def get_low_points(height_map):
    low_points = []

    for i, row in enumerate(height_map):
        for j, height in enumerate(row):
            low_point = True
            position = (i, j)
            neighbours = get_neighbours(position, height_map)

            for n_row, n_col in neighbours:
                if height_map[n_row][n_col] <= height:
                    low_point = False
                    break

            if low_point:
                low_points.append(position)

    return low_points


def search_basin_recursive(position, height_map, seen):
    positions = set()
    row, col = position

    for neighbour in get_neighbours(position, height_map):
        seen.add(neighbour)

        n_row, n_col = neighbour
        if height_map[n_row][n_col] != 9 and height_map[n_row][n_col] > height_map[row][col]:
            positions.add(neighbour)
            positions = positions.union(search_basin_recursive(neighbour, height_map, seen))

    return positions


def find_basins(height_map):
    low_points = get_low_points(height_map)
    sizes = []

    for position in low_points:
        sizes.append(1 + len(search_basin_recursive(position, height_map, {position})))

    return reduce((lambda x, y: x * y), sorted(sizes, reverse=True)[:3])


if __name__ == '__main__':
    print(find_basins(read_input('input.txt')))
