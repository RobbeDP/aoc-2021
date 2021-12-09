def remove_indices(lst, indices):
    for idx in sorted(indices, reverse=True):
        del lst[idx]


binary_numbers = []
with open('input.txt') as input_file:
    for line in input_file:
        binary_numbers.append(line.rstrip('\n'))


def filter_list(lst, most_common):
    lst = lst[:]
    i = 0

    while len(lst) > 1:
        indices_0 = []
        indices_1 = []

        for index, binary_number in enumerate(lst):
            if binary_number[i] == '0':
                indices_0.append(index)
            else:
                indices_1.append(index)

        if (most_common and len(indices_0) > len(indices_1)) or (not most_common and len(indices_0) <= len(indices_1)):
            remove_indices(lst, indices_1)
        else:
            remove_indices(lst, indices_0)

        i += 1

    return lst


oxygen = filter_list(binary_numbers, True)
co2 = filter_list(binary_numbers, False)

print(int(''.join(oxygen), 2) * int(''.join(co2), 2))
