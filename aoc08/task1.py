class Entry:
    def __init__(self, in_signals, out_digits):
        self.in_signals = in_signals
        self.out_digits = out_digits

    def __repr__(self):
        return f'{" ".join(self.in_signals)} | {" ".join(self.out_digits)}'


# Mapping from amount of segments to digits with this amount of segments
segment_amounts = {
    2: {1},
    3: {7},
    4: {4},
    5: {2, 3, 5},
    6: {0, 6, 9},
    7: {8}
}


def read_input(file_name):
    with open(file_name) as input_file:
        entries = []
        for line in input_file:
            parts = line.rstrip('\n').split(' | ')
            entries.append(Entry(
                parts[0].split(' '),
                parts[1].split(' ')
            ))

        return entries


def easy_digits_amount(entries):
    amount = 0
    for entry in entries:
        for digit in entry.out_digits:
            possible_digits = segment_amounts[len(digit)]

            if len(possible_digits) == 1:
                amount += 1

    return amount


if __name__ == '__main__':
    print(easy_digits_amount(read_input('input.txt')))
