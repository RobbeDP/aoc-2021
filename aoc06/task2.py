from task1 import read_input
from collections import defaultdict


def simulate(fish_list, days):
    fish_dict = defaultdict(int)

    for timer in fish_list:
        fish_dict[timer] += 1

    for _ in range(days):
        new_dict = defaultdict(int)
        for i in range(9):
            new_dict[i] = fish_dict[(i + 1) % 9]

        new_dict[6] += fish_dict[0]

        fish_dict = new_dict

    return sum(fish_dict.values())


if __name__ == '__main__':
    print(simulate(read_input('input.txt'), 256))
