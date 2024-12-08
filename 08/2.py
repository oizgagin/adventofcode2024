from collections import defaultdict


def solution(map_):
    antennas = defaultdict(list)
    for i in range(0, len(map_)):
        for j in range(0, len(map_[i])):
            if map_[i][j] != '.': antennas[map_[i][j]].append((i, j))

    in_ = lambda i, j: 0 <= i < len(map_) and 0 <= j < len(map_[i])
    dist = lambda i1, j1, i2, j2: (i1 - i2) ** 2 + (j1 - j2) ** 2

    antidotes = set()
    for antenna, coords in antennas.items():
        for i, (i1, j1) in enumerate(coords):
            for (i2, j2) in coords[i+1:]:
                di, dj = i2-i1, j2-j1

                antidotes.add((i1, j1))

                curri, currj = i1-di, j1-dj
                while in_(curri, currj):
                    antidotes.add((curri, currj))
                    curri, currj = curri-di, currj-dj

                curri, currj = i1+di, j1+dj
                while in_(curri, currj):
                    antidotes.add((curri, currj))
                    curri, currj = curri+di, currj+dj

    return len(antidotes)


def parse(input):
    return tuple(tuple(s) for s in input.splitlines())


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
