def read_input(file_name):
    with open(file_name) as input_file:
        return list(map(lambda x: int(x), input_file.readline().rstrip('\n').split(',')))


def simulate(fish_list, days):
    fish_list = fish_list[:]

    for _ in range(days):
        new_fish_amount = 0
        for i, fish in enumerate(fish_list):
            if fish == 0:
                fish_list[i] = 6
                new_fish_amount += 1
            else:
                fish_list[i] -= 1

        fish_list.extend([8] * new_fish_amount)

    return len(fish_list)


if __name__ == '__main__':
    print(simulate(read_input('input.txt'), 80))
