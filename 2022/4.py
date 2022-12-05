import re

def main():
    with open('inputs/4.txt') as f:
        file = f.readlines()

    complete_overlaps = 0
    overlaps = 0

    for line in file:
        # f = first, s = second
        ff_pattern = re.compile(r"^(\d+)")
        ff = int(re.search(ff_pattern, line).group(1))

        fs_pattern = re.compile(r"-(\d+),")
        fs = int(re.search(fs_pattern, line).group(1))

        sf_pattern = re.compile(r",(\d+)")
        sf = int(re.search(sf_pattern, line).group(1))

        ss_pattern = re.compile(r"-(\d+)$")
        ss = int(re.search(ss_pattern, line).group(1))

        if ff <= sf and fs >= ss or sf <= ff and ss >= fs:
            complete_overlaps += 1

        first = set(range(ff, fs+1))
        second = set(range(sf, ss+1))

        overlap_first = [x for x in first if x in second]

        overlap_second = [x for x in second if x in first]

        if len(overlap_first) > 0 or len(overlap_second) > 0:
            overlaps += 1

    print("Number of complete overlaps: " + str(complete_overlaps)) # 580

    print("Number of overlaps: " + str(overlaps)) # 895

if __name__ == "__main__":
    main()
