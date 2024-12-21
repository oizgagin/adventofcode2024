from itertools import product
from functools import wraps


def cache(f):
    memo = {}

    @wraps(f)
    def wrapper(*args):
        if args in memo: return memo[args]
        v = f(*args)
        memo[args] = v
        return v

    return wrapper


def solution(codes):
    get = lambda keypad, pos: keypad[pos[0]][pos[1]]
    in_ = lambda keypad, pos: 0 <= pos[0] < len(keypad) and 0 <= pos[1] < len(keypad[0]) and get(keypad, pos) is not None
    move = lambda pos, dir_: (pos[0] + dir_[0], pos[1] + dir_[1])

    dirs = {(0, 1): ">", (0, -1): "<", (1, 0): "v", (-1, 0): "^"}

    numeric = (("7", "8", "9"), ("4", "5", "6"), ("1", "2", "3"), (None, "0", "A"))
    directional = ((None, "^", "A"), ("<", "v", ">"))

    @cache
    def find(keypad, ch):
        for i, j in product(range(0, len(keypad)), range(0, len(keypad[0]))):
            if keypad[i][j] == ch: return (i, j)
        assert False, "unreachable"

    @cache
    def shortest(keypad, pos1, pos2): # returns all shortest paths between pos1 and pos2
        q = [("", pos1)]

        while len(q) > 0:
            q2 = []

            if any(n == pos2 for _, n in q): return [p for p, n in q if n == pos2]

            for p, n in q:
                for dir_, ch in dirs.items():
                    nn = move(n, dir_)
                    if in_(keypad, nn): q2.append((p + ch, nn))

            q = q2

    @cache
    def solve(keypad, code, pos):
        partials = []

        for ch in code:
            nextpos = find(keypad, ch)
            partials.append(shortest(keypad, pos, nextpos))
            pos = nextpos

        res = []
        for pp in product(*partials):
            res.append("A".join(pp) + "A")
        return res

    res = 0

    for code in codes:
        min_ = float("inf")

        for code1 in solve(numeric, code, find(numeric, "A")):
            for code2 in solve(directional, code1, find(directional, "A")):
                for code3 in solve(directional, code2, find(directional, "A")):
                    min_ = min(min_, len(code3))

        res += int("".join(filter(str.isnumeric, list(code)))) * min_

    return res


def parse(input):
    return input.splitlines()


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
