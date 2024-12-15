from collections import defaultdict
from itertools import product


def solution(map_, dirs):
    m = defaultdict(lambda: None)
    for i, j in product(range(0, len(map_)), range(0, len(map_[0]))):
        m[(i, j)] = map_[i][j]

    move = lambda p, d: (p[0] + d[0], p[1] + d[1])

    ds = {">": (0, 1), "<": (0, -1), "v": (1, 0), "^": (-1, 0)}

    def apply(p, d):
        pp = move(p, d)

        if m[pp] == "#":
            return p

        if m[pp] == ".":
            return pp

        assert m[pp] == "O", m[pp]

        while m[pp] == "O":
            pp = move(pp, d)

        if m[pp] == "#":
            return p

        assert m[pp] == ".", m[pp]

        m[pp] = "O"
        m[move(p, d)] = "."

        return move(p, d)

    p = [(i, j) for i, j in m if m[(i, j)] == "@"][0]
    m[p] = "."
    for d in dirs:
        p = apply(p, ds[d])

    res = 0
    for i, j in product(range(0, len(map_)), range(0, len(map_[0]))):
        if m[(i, j)] == "O": res += 100 * i + j
    return res


def parse(input):
    map_, dirs = input.split("\n\n")
    map_ = map_.splitlines()
    dirs = tuple("".join(dirs.splitlines()))
    return map_, dirs


def main():
    input = open("input", "r").read()
    print(solution(*parse(input)))


main()
