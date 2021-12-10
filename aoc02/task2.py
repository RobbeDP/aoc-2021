if __name__ == '__main__':
    with open('input.txt') as input_file:
        commands = []
        for line in input_file:
            command_arr = line.rstrip('\n').split(' ')
            commands.append((command_arr[0], int(command_arr[1])))

        aim = 0
        depth = 0
        horizontal = 0

        for command in commands:
            if command[0] == 'down':
                aim += command[1]
            elif command[0] == 'up':
                aim -= command[1]
            elif command[0] == 'forward':
                horizontal += command[1]
                depth += aim * command[1]

        print(depth * horizontal)
