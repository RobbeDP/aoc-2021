def read_input(file_name):
    with open(file_name) as input_file:
        return [list(map(lambda x: int(x), line.rstrip('\n'))) for line in input_file]


def increment_grid(grid):
    for i, row in enumerate(grid):
        for j, _ in enumerate(row):
            grid[i][j] += 1


def in_bounds(position, n_rows, n_cols):
    row, col = position

    return 0 <= row < n_rows and 0 <= col < n_cols


offsets = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]


def get_neighbours(position, grid):
    row, col = position
    neighbours = set()

    for row_offset, col_offset in offsets:
        neighbour_position = (row + row_offset, col + col_offset)
        if in_bounds(neighbour_position, len(grid), len(grid[0])):
            neighbours.add(neighbour_position)

    return neighbours


def positions_to_flash(grid):
    positions = set()

    # Find all positions with energy level higher than 9
    for i, row in enumerate(grid):
        for j, value in enumerate(row):
            if value > 9:
                positions.add((i, j))

    return positions


def flash(grid):
    positions = positions_to_flash(grid)
    flashed = set()

    while positions:
        flashed = flashed.union(positions)
        new_positions = set()
        for position in positions:
            neighbours = get_neighbours(position, grid)
            for neighbour in neighbours:
                if neighbour not in flashed:
                    n_row, n_col = neighbour
                    grid[n_row][n_col] += 1

                    if grid[n_row][n_col] > 9:
                        new_positions.add(neighbour)

        positions = new_positions

    for flashed_position in flashed:
        row, col = flashed_position
        grid[row][col] = 0

    return len(flashed)


def step(grid):
    increment_grid(grid)
    starting_positions = positions_to_flash(grid)

    return flash(grid)


def simulate(grid, steps):
    flashes = 0

    for _ in range(steps):
        flashes += step(grid)

    return flashes


if __name__ == '__main__':
    print(simulate(read_input('input.txt'), 100))
