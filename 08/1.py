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

                if in_(i1-di, j1-dj): antidotes.add((i1-di, j1-dj))
                if in_(i2+di, j2+dj): antidotes.add((i2+di, j2+dj))

                if di % 3 == 0 and dj % 3 == 0:
                    if in_(i1+di//3, j1+dj//3):
                        antidotes.add((i1+di//3, j1+dj//3))
                    if in_(i2-di//3, j2-dj//3):
                        antidotes.add((i2-di//3, j2-dj//3))

    return len(antidotes)


def parse(input):
    return tuple(tuple(s) for s in input.splitlines())


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
