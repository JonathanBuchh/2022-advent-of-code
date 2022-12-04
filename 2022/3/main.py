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
        print(first_half)
        print(second_half)

        unique_first_half = []

        for i in first_half:
            if i not in unique_first_half: unique_first_half.append(i)

        for i in range(len(unique_first_half)):
            if unique_first_half[i] in second_half: duplicates.append(unique_first_half[i])

    sum = 0

    for i in duplicates:
        sum += priorities[i]

    print('Sum: ' + str(sum))

if __name__ == "__main__":
    main()
