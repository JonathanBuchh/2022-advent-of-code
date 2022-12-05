from string import ascii_lowercase
from string import ascii_uppercase

def main():
    priorities = {}

    for i in range(1,53):
        if i < 27:
            priorities[ascii_lowercase[i-1]] = i
        else:
            priorities[ascii_uppercase[i-27]] = i

    with open('input.txt') as f:
        file = f.readlines()

    duplicates = []

    for line in file:
        mid = int(len(line.strip())/2)
        first_half = line.strip()[0:mid]
        second_half =  line.strip()[mid:len(line.strip())]

        unique_first_half = []

        for i in first_half:
            if i not in unique_first_half: unique_first_half.append(i)

        for i in range(len(unique_first_half)):
            if unique_first_half[i] in second_half: duplicates.append(unique_first_half[i])

    sum = 0

    for i in duplicates:
        sum += priorities[i]

    print('Part 1 sum: ' + str(sum)) # 7903

    badges = []
    possibilities = list(ascii_lowercase) + list(ascii_uppercase)

    for i in range(int(len(file)/3)):
        for letter in possibilities:
            if letter in file[3*i] and letter in file[3*i+1] and letter in file[3*i+2]:
                badges.append(letter)
    sum = 0

    for i in badges:
        sum += priorities[i]

    print('Part 2 sum: ' + str(sum)) # 2548

if __name__ == "__main__":
    main()
