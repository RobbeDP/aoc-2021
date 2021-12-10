from task1 import read_input, find_overlap_amount


if __name__ == '__main__':
    input_lines = read_input('input.txt')
    print(find_overlap_amount(input_lines, True))
