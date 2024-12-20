from itertools import product


def solution(map_):
    ds = ((-1, 0), (1, 0), (0, -1), (0, 1))

    move = lambda p, d: (p[0] + d[0], p[1] + d[1])
    in_ = lambda p: 0 <= p[0] < len(map_) and 0 <= p[1] < len(map_)
    get = lambda p: map_[p[0]][p[1]]
    def set_(p, ch): map_[p[0]][p[1]] = ch
    all_ = lambda: product(range(0, len(map_)), range(0, len(map_[0])))
    emptys = lambda p: len(list(move(p, d) for d in ds if in_(move(p, d)) and get(move(p, d)) == "."))

    s = [(i, j) for i, j in all_() if get((i, j)) == 'S'][0]
    set_(s, ".")

    e = [(i, j) for i, j in all_() if get((i, j)) == 'E'][0]
    set_(e, ".")

    def bfs(s, e):
        qs, qe = set([s]), set([e])
        visiteds, visitede = set([s]), set([e])

        c = 0

        while len(qs) > 0 or len(qe) > 0:
            if qs & qe:
                return 2 * c

            c += 1

            nextqs = set()
            for n, d in product(qs, ds):
                nn = move(n, d)
                if get(nn) == "." and nn not in visiteds:
                    nextqs.add(nn)
                    visiteds.add(nn)

            nextqe = set()
            for n, d in product(qe, ds):
                nn = move(n, d)
                if get(nn) == "." and nn not in visitede:
                    nextqe.add(nn)
                    visitede.add(nn)

            qs, qe = nextqs, nextqe

        return None

    dist = bfs(s, e)

    res = 0
    for i, j in all_():
        if get((i, j)) == "#" and emptys((i, j)) >= 2:
            set_((i, j), ".")
            d = bfs(s, e)
            set_((i, j), "#")

            if dist - d >= 100:
                res += 1

    return res


def parse(input):
    return list(map(list, input.splitlines()))


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
