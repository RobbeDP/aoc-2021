from math import inf


def read_input(file_name):
    with open(file_name) as input_file:
        return list(map(lambda x: int(x), input_file.readline().rstrip('\n').split(',')))


def find_cost(positions, base, increasing):
    cost = 0
    for position in positions:
        distance = abs(position - base)

        if increasing:
            cost += int((distance * (distance + 1)) / 2)
        else:
            cost += distance

    return cost


def find_cheapest_position(positions, increasing):
    min_cost = inf

    for position in range(min(positions), max(positions) + 1):
        cost = find_cost(positions, position, increasing)
        if cost < min_cost:
            min_cost = cost

    return min_cost


if __name__ == '__main__':
    print(find_cheapest_position(read_input('input.txt'), False))
