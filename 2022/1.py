def main():
    with open('inputs/1.txt') as f:
        file = f.readlines()

    calories = [0]
    count = 0

    for line in file:
        if len(line.strip()) == 0:
            count += 1
            calories.append(0)
        else:
            calories[count] += int(line.strip())

    print('Max calories: ' + str(max(calories)))

    top_three_total = 0

    for i in range(3):
        top_three_total += max(calories)
        calories.remove(max(calories))

    print('Top three total: ' + str(top_three_total))

if __name__ == "__main__":
    main()
