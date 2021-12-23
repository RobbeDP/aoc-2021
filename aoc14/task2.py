from collections import defaultdict


def read_input(file_name):
    with open(file_name) as input_file:
        start_pairs = defaultdict(int)

        polymer_template = input_file.readline().rstrip('\n')
        for i in range(len(polymer_template) - 1):
            start_pairs[polymer_template[i:i + 2]] += 1

        input_file.readline()

        resulting_pairs = {}
        for line in input_file:
            pair, to_insert = line.rstrip('\n').split(' -> ')
            pairs = (f'{pair[0]}{to_insert}', f'{to_insert}{pair[1]}')
            resulting_pairs[pair] = pairs

        return start_pairs, resulting_pairs


def do_step(pairs, pair_insertions):
    new_pairs = defaultdict(int)

    for pair, occurrence in pairs.items():
        p1, p2 = pair_insertions[pair]
        new_pairs[p1] += occurrence
        new_pairs[p2] += occurrence

    return new_pairs


def do_insertions(start_pairs, pair_insertions, steps):
    current_pairs = start_pairs

    for _ in range(steps):
        current_pairs = do_step(current_pairs, pair_insertions)

    return current_pairs


def find_answer(file_name, steps):
    start_pairs, pair_insertions = read_input(file_name)
    resulting_pairs = do_insertions(start_pairs, pair_insertions, steps)

    start_pairs_list = list(start_pairs.keys())
    first_molecule = start_pairs_list[0][0]
    last_molecule = start_pairs_list[-1][-1]

    counts = defaultdict(int)
    counts[first_molecule] += 1
    counts[last_molecule] += 1

    for pair, occurrence in resulting_pairs.items():
        counts[pair[0]] += occurrence
        counts[pair[1]] += occurrence

    return max(counts.values()) // 2 - min(counts.values()) // 2


if __name__ == '__main__':
    print(find_answer('input.txt', 40))
