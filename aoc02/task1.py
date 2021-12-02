with open('input.txt') as input_file:
    commands = []
    for line in input_file:
        command_arr = line.rstrip('\n').split(' ')
        commands.append((command_arr[0], int(command_arr[1])))

    depth = 0
    horizontal = 0

    for command in commands:
        if command[0] == 'down':
            depth += command[1]
        elif command[0] == 'up':
            depth -= command[1]
        elif command[0] == 'forward':
            horizontal += command[1]

    print(depth * horizontal)
