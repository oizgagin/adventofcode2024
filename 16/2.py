import heapq
from collections import defaultdict
from itertools import product


def solution(m):
    cw = lambda d: {"E": "S", "S": "W", "W": "N", "N": "E"}[d]
    ccw = lambda d: {"E": "N", "N": "W", "W": "S", "S": "E"}[d]
    dirs = ("E", "S", "W", "N")
    ds = lambda d: {"E": (0, 1), "W": (0, -1), "S": (1, 0), "N": (-1, 0)}[d]

    move = lambda p, d: (p[0] + ds(d)[0], p[1] + ds(d)[1])

    def dijkstra(s, d):
        h = [(0, (s, d))]
        dists = defaultdict(lambda: float("inf"))

        intree = set()

        while len(h) > 0:
            dist, (p, d) = heapq.heappop(h)
            if (p, d) in intree:
                continue

            intree.add((p, d))
            dists[(p, d)] = min(dists[(p, d)], dist)

            if m[move(p, d)] == ".":
                heapq.heappush(h, (dist + 1, (move(p, d), d)))

            heapq.heappush(h, (dist + 1000, (p, cw(d))))
            heapq.heappush(h, (dist + 1000, (p, ccw(d))))
            heapq.heappush(h, (dist + 2000, (p, cw(cw(d)))))

        return dists

    s = [(i, j) for i, j in m if m[(i, j)] == "S"][0]
    m[s] = "."

    e = [(i, j) for i, j in m if m[(i, j)] == "E"][0]
    m[e] = "."

    distss = dijkstra(s, "E")

    diste = min(distss[(e, dir_)] for dir_ in dirs)
    dirse = [dir_ for dir_ in dirs if distss[(e, dir_)] == diste]

    assert len(dirse) == 1

    distse = dijkstra(e, cw(cw(dirse[0])))

    res = set()
    for i, j in m:
        for d1, d2 in product(dirs, dirs):
            if distss[((i, j), d1)] + distse[((i, j), d2)] == diste:
                res.add((i, j))
    return len(res)


def parse(input):
    map_ = list(map(list, input.splitlines()))
    m = defaultdict(lambda: None)
    for i, j in product(range(0, len(map_)), range(0, len(map_[0]))):
        m[(i, j)] = map_[i][j]
    return m


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()