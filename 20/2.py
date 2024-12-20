from itertools import product
from collections import defaultdict
import heapq


def solution(map_):
    dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))

    move = lambda p, d: (p[0] + d[0], p[1] + d[1])
    in_ = lambda p: 1 <= p[0] < len(map_)-1 and 1 <= p[1] < len(map_)-1
    get = lambda p: map_[p[0]][p[1]]
    def set_(p, ch): map_[p[0]][p[1]] = ch
    all_ = lambda: product(range(0, len(map_)), range(0, len(map_[0])))
    dist = lambda p1, p2: abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    s = [(i, j) for i, j in all_() if get((i, j)) == 'S'][0]
    set_(s, ".")

    e = [(i, j) for i, j in all_() if get((i, j)) == 'E'][0]
    set_(e, ".")

    def dijkstra(s, e, p1=None, p2=None):
        dists = defaultdict(lambda: float("inf"))
        intree = set()

        h = [(0, s)]
        while len(h) > 0:
            d, n = heapq.heappop(h)

            dists[n] = d
            intree.add(n)

            if n == p1:
                heapq.heappush(h, (d + dist(p1, p2), p2))
            if n == p2:
                heapq.heappush(h, (d + dist(p1, p2), p1))

            for dir_ in dirs:
                nn = move(n, dir_)
                if in_(nn) and get(nn) == "." and nn not in intree:
                    heapq.heappush(h, (d + 1, nn))

        return dists

    dists = dijkstra(s, e)
    points = list(sorted(dists.keys(), key=lambda p: dists[p]))

    res = 0

    for i, p1 in enumerate(points):
        for p2 in points[i+1:]:
            d = dist(p1, p2)
            if d > 20: continue

            d1, d2 = dists[p1], dists[p2]

            if d > d2 - d1: continue

            newd = dists[e] - dists[p2] + d + dists[p1]
            win = dists[e] - newd
            if win >= 100:
                res += 1

    return res


def parse(input):
    return list(map(list, input.splitlines()))


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
