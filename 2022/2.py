def main():
    with open('inputs/2.txt') as f:
        file = f.readlines()

    initial_score = 0

    for i in range(len(file)):
        opponent = file[i][0]
        me = file[i][2]
        if opponent == 'A':
            if me == 'X': initial_score += 1 + 3
            if me == 'Y': initial_score += 2 + 6
            if me == 'Z': initial_score += 3 + 0
        if opponent == 'B':
            if me == 'X': initial_score += 1 + 0
            if me == 'Y': initial_score += 2 + 3
            if me == 'Z': initial_score += 3 + 6
        if opponent == 'C':
            if me == 'X': initial_score += 1 + 6
            if me == 'Y': initial_score += 2 + 0
            if me == 'Z': initial_score += 3 + 3

    print('Without instructions: ' + str(initial_score)) # 8392
    instructions_score = 0

    for i in range(len(file)):
        opponent = file[i][0]
        me = file[i][2]
        if me == 'X':
            if opponent == 'A': instructions_score += 3
            if opponent == 'B': instructions_score += 1
            if opponent == 'C': instructions_score += 2
        if me == 'Y':
            if opponent == 'A': instructions_score += 3 + 1
            if opponent == 'B': instructions_score += 3 + 2
            if opponent == 'C': instructions_score += 3 + 3
        if me == 'Z':
            if opponent == 'A': instructions_score += 6 + 2
            if opponent == 'B': instructions_score += 6 + 3
            if opponent == 'C': instructions_score += 6 + 1

    print('With instructions: ' + str(instructions_score)) # 10116

if __name__ == "__main__":
    main()
