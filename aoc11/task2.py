from task1 import read_input, increment_grid, positions_to_flash, flash


def have_all_flashed(grid):
    for row in grid:
        for value in row:
            if value != 0:
                return False

    return True


def step(grid):
    increment_grid(grid)
    flash(grid)

    return have_all_flashed(grid)


def simulate(grid):
    i = 1

    while not step(grid):
        i += 1

    return i


if __name__ == '__main__':
    print(simulate(read_input('input.txt')))
