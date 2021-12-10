if __name__ == '__main__':
    with open('input.txt') as input_file:
        measurements = []
        for line in input_file:
            measurements.append(int(line.rstrip('\n')))

        increased = 0
        prev_sum = None
        for i in range(len(measurements) - 2):
            curr_sum = measurements[i] + measurements[i + 1] + measurements[i + 2]

            if prev_sum is not None and curr_sum > prev_sum:
                increased += 1

            prev_sum = curr_sum

        print(increased)
