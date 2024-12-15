from collections import defaultdict
from itertools import product


def solution(map_, dirs):
    m = defaultdict(lambda: None)
    for i, j in product(range(0, len(map_)), range(0, len(map_[0]))):
        if map_[i][j] == "#":
            m[(i, 2*j)] = "#"
            m[(i, 2*j+1)] = "#"
        elif map_[i][j] == "O":
            m[(i, 2*j)] = "["
            m[(i, 2*j+1)] = "]"
        elif map_[i][j] == ".":
            m[(i, 2*j)] = "."
            m[(i, 2*j+1)] = "."
        elif map_[i][j] == "@":
            m[(i, 2*j)] = "@"
            m[(i, 2*j+1)] = "."

    ds = {">": (0, 1), "<": (0, -1), "v": (1, 0), "^": (-1, 0)}

    move = lambda p, d: (p[0] + ds[d][0], p[1] + ds[d][1])

    def apply(p, d):
        pp = move(p, d)

        if m[pp] == "#":
            return p

        if m[pp] == ".":
            return pp

        assert m[pp] in "[]", m[pp]

        if d in "<>":
            while m[pp] in "[]":
                pp = move(pp, d)

            if m[pp] == "#":
                return p

            assert m[pp] == ".", m[pp]

            start, end = pp, p
            revd = "<" if d == ">" else ">"

            currp = start
            while currp != end:
                nextp = move(currp, revd)
                m[currp] = m[nextp]
                currp = nextp

            m[p] = "."
            return move(p, d)

        assert d in "v^", d

        def can_move(p):
            if m[p] == ".": return True
            if m[p] == "#": return False

            assert m[p] in "[]", m[p]

            if m[p] == "[":
                assert m[move(p, ">")] == "]", m[p]
                return can_move(move(p, d)) and can_move(move(move(p, ">"), d))

            if m[p] == "]":
                assert m[move(p, "<")] == "[", m[p]
                return can_move(move(p, d)) and can_move(move(move(p, "<"), d))

        def move_all(p):
            if m[p] == ".":
                return

            p1 = p
            p2 = move(p, ">") if m[p] == "[" else move(p, "<")

            if p1 > p2: p1, p2 = p2, p1

            assert m[p1] + m[p2] == "[]"

            move_all(move(p1, d))
            move_all(move(p2, d))

            assert m[move(p1, d)] == "." and m[move(p2, d)] == "."
            m[move(p1, d)], m[move(p2, d)] = "[", "]"
            m[p1] = m[p2] = "."

        if can_move(pp):
            move_all(pp)
            return move(p, d)

        return p

    p = [(i, j) for i, j in m if m[(i, j)] == "@"][0]
    m[p] = "."
    for d in dirs:
        p = apply(p, d)

    res = 0
    for i, j in product(range(0, len(map_)), range(0, 2 * len(map_[0]))):
        if m[(i, j)] == "[": res += 100 * i + j
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
