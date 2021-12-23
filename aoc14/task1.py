from collections import Counter


def read_input(file_name):
    with open(file_name) as input_file:
        polymer_template = input_file.readline().rstrip('\n')
        # Read empty line
        input_file.readline()

        pair_insertions = {}
        for line in input_file:
            pair, to_insert = line.rstrip('\n').split(' -> ')
            pair_insertions[pair] = to_insert

        return polymer_template, pair_insertions


def do_insertions(polymer_template, pair_insertions, steps):
    polymer_template = list(polymer_template)

    for _ in range(steps):
        for i in range(len(polymer_template) - 1):
            index = 2 * i
            pair = ''.join(polymer_template[index:index + 2])
            to_insert = pair_insertions[pair]
            polymer_template.insert(index + 1, to_insert)

    return ''.join(polymer_template)


def find_answer(file_name, steps):
    polymer_template, pair_insertions = read_input(file_name)
    polymer = do_insertions(polymer_template, pair_insertions, steps)

    counts = Counter(polymer)

    return max(counts.values()) - min(counts.values())


if __name__ == '__main__':
    print(find_answer('input.txt', 10))
