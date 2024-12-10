from collections import defaultdict
from itertools import product


def solution(map_):
    in_ = lambda i, j: 0 <= i < len(map_) and 0 <= j < len(map_[i])

    def dfs(i, j, visited):
        visited.add((i, j))

        if map_[i][j] == 9: return 1

        res = 0
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            if in_(i+di, j+dj) and (i+di, j+dj) not in visited and map_[i+di][j+dj] == map_[i][j] + 1:
                res += dfs(i+di, j+dj, visited)
        return res

    return sum(dfs(i, j, set()) for i, j in product(range(0, len(map_)), range(0, len(map_[0]))) if map_[i][j] == 0)


def parse(input):
    return tuple(map(lambda s: tuple(map(int, s)), input.splitlines()))


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
