if __name__ == '__main__':
    with open('input.txt') as input_file:
        increased = 0
        prev_val = None

        for line in input_file:
            curr_val = int(line.rstrip('\n'))
            if prev_val is not None and curr_val > prev_val:
                increased += 1

            prev_val = curr_val

        print(increased)
