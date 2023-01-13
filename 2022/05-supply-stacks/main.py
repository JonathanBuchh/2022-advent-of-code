from string import ascii_uppercase
import re
import copy

def main():
    with open("input.txt") as file:
        data = file.readlines()

    crates = []

    # create stacks
    for i in range(len(data)):
        if data[i].strip() == "":
            crates = [list() for i in data[i-1].strip().split("  ")]

    crates_done = False
    crates_two = []
    count = 0

    # put crates in stack
    for i in range(len(data)):
        if data[i].strip() == "":
            crates_done = True
            crates_two = ["".join(i)[::-1] for i in copy.deepcopy(crates)]
        elif not crates_done:
            for j in range(len(data[i])):
                if data[i][j] in ascii_uppercase:
                    col = int((j - 1) / 4)
                    crates[col].append(data[i][j])
        else:
            count += 1
            match = re.compile(r"^move\s(\d+)\sfrom\s(\d+)\sto\s(\d+)$")
            moves = re.search(match, data[i]).groups()

            for i in range(int(moves[0])):
                crates[int(moves[2])-1].insert(0, crates[int(moves[1])-1].pop(0))

            temp = crates_two[int(moves[1])-1]
            print(temp)
            to_move = temp[len(temp)-int(moves[0]):len(temp)]
            print(to_move)
            temp = temp.replace(to_move, "")
            if count == 14: print(temp)
            crates_two[int(moves[1])-1] = temp
            crates_two[int(moves[2])-1] = crates_two[int(moves[2])-1] + to_move
            print(crates_two)

            if len("".join(i for i in crates_two)) != 56: break

    # print(f"Part 1: {''.join([i[0] for i in crates])}") # VPCDMSLWJ
    # print(f"Part 2: {''.join([i[-1] for i in crates_two if len(i) > 0])}")

if __name__ == "__main__":
    main()
