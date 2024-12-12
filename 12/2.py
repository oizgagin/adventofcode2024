from collections import defaultdict
from itertools import product, groupby


def solution(map_):
    m = defaultdict(lambda: '.')
    for i, j in product(range(0, len(map_)), range(0, len(map_[0]))):
        m[(i, j)] = map_[i][j]

    def dfs(i, j, visited):
        visited.add((i, j))
        area = 0
        for di, dj in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            if m[(i+di, j+dj)] == m[(i, j)] and (i+di, j+dj) not in visited:
                area += dfs(i+di, j+dj, visited)
        return area+1

    def exterior(i, j, visited, ups, lefts, rights, downs):
        visited.add((i, j))

        if m[(i-1, j)] != m[(i, j)]:
            ups.add((i, j))
        if m[(i+1, j)] != m[(i, j)]:
            downs.add((i, j))
        if m[(i, j-1)] != m[(i, j)]:
            lefts.add((i, j))
        if m[(i, j+1)] != m[(i, j)]:
            rights.add((i, j))

        for di, dj in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            if m[(i+di, j+dj)] == m[(i, j)] and (i+di, j+dj) not in visited:
                exterior(i+di, j+dj, visited, ups, lefts, rights, downs)

    def conseq(it):
        res = 1
        for i in range(1, len(it)):
            if it[i-1]+1 != it[i]: res += 1
        return res

    def calc_sides(ups, lefts, rights, downs):
        sides = 0

        # for each row in ups check how many consequtive columns
        for row, cols in groupby(sorted(ups), key=lambda t: t[0]):
            sides += conseq(list(sorted(map(lambda t: t[1], cols))))

        # same for downs
        for row, cols in groupby(sorted(downs), key=lambda t: t[0]):
            sides += conseq(list(sorted(map(lambda t: t[1], cols))))

        # for each column in lefts check how many consequitve rows
        for col, rows in groupby(sorted(lefts, key=lambda t: t[1]), key=lambda t: t[1]):
            sides += conseq(list(sorted(map(lambda t: t[0], rows))))

        # same for rights
        for col, rows in groupby(sorted(rights, key=lambda t: t[1]), key=lambda t: t[1]):
            sides += conseq(list(sorted(map(lambda t: t[0], rows))))

        return sides

    areas = {}

    visited = set()
    for i, j in product(range(0, len(map_)), range(0, len(map_[0]))):
        if (i, j) not in visited:
            areas[(i, j)] = dfs(i, j, visited)

    res = 0

    visited = set()
    for i, j in product(range(0, len(map_)), range(0, len(map_[0]))):
        if (i, j) not in visited:
            ups, lefts, rights, downs = set(), set(), set(), set()
            exterior(i, j, visited, ups, lefts, rights, downs)
            res += areas[(i, j)] * calc_sides(ups, lefts, rights, downs)

    return res


def parse(input):
    return list(map(list, input.splitlines()))


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
