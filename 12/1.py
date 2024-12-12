from itertools import product


def solution(map_):

    def dfs(i, j, visited):
        visited.add((i, j))

        p = 4

        pp = aa = 0

        for di, dj in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            if 0 <= i+di < len(map_) and 0 <= j+dj < len(map_[i+di]):
                if map_[i+di][j+dj] == map_[i][j]:
                    p -= 1
                    if (i+di, j+dj) not in visited:
                        np, na = dfs(i+di, j+dj, visited)
                        pp += np
                        aa += na

        return (pp+p, aa+1)

    res, visited = 0, set()
    for i, j in product(range(0, len(map_)), range(0, len(map_[0]))):
        if (i, j) not in visited:
            p, a = dfs(i, j, visited)
            res += p * a
    return res


def parse(input):
    return list(map(list, input.splitlines()))


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
