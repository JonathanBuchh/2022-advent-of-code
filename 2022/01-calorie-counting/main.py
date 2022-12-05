def main():
    with open('input.txt') as file:
        data = [i for i in file.read().strip().split("\n")]

    temp_sum = 0
    sums = []

    for i in data:
        if i == "":
            sums.append(temp_sum)
            temp_sum = 0
        else: temp_sum += int(i)

    print(f"Part 1: {sorted(sums)[-1]}") # 74198
    print(f"Part 2: {sum(sorted(sums)[-3:])}") # 209914

if __name__ == "__main__":
    main()
