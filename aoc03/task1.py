binary_numbers = []
with open('input.txt') as input_file:
    for line in input_file:
        binary_numbers.append(line.rstrip('\n'))

gamma = []

for i in range(len(binary_numbers[0])):
    count_0 = 0
    count_1 = 0
    for binary_number in binary_numbers:
        if binary_number[i] == '0':
            count_0 += 1
        else:
            count_1 += 1

    if count_0 > count_1:
        gamma.append('0')
    else:
        gamma.append('1')

gamma = int(''.join(gamma), 2)
epsilon = 2 ** len(binary_numbers[0]) - 1 - gamma

print(gamma * epsilon)
