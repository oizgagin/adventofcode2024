from itertools import groupby


def solution(robots):
    X, Y = 101, 103

    def move(robot):
        p, v = robot
        return ((p[0] + v[0]) % X, (p[1] + v[1]) % Y), v

    def moveall(robots):
        return tuple(map(move, robots))

    def q(robot):
        px, py = robot[0]

        if px == X // 2 or py == Y // 2:
            return 0
        if px < X // 2 and py < Y // 2:
            return 1
        if px > X // 2 and py < Y // 2:
            return 2
        if px < X // 2 and py > Y // 2:
            return 3
        if px > X // 2 and py > Y // 2:
            return 4

    def symmx(robots):
        res = []
        for x, y in robots:
            assert x < X // 2
            res.append((X // 2 + X // 2 - x, y))
        return res

    def symmy(robots):
        res = []
        for x, y in robots:
            assert y < Y // 2
            res.append((x, Y // 2 + Y // 2 - y))
        return res

    def hash_(robots):
        res = [ list("." * X) for _ in range(0, Y) ]
        for p, _ in robots:
            x, y = p
            res[y][x] = "#"
        return "\n".join(map(lambda r: "".join(r), res)) + "\n"

    def tree_coeff(robots):
        qs = dict(
            (qq, list(map(lambda r: r[0], robots)))
            for qq, robots in groupby(filter(lambda robot: q(robot) != 0, sorted(robots, key=q)), key=q)
        )

        assert all(len(qs[i]) > 0 for i in range(1, 5))

        xq1 = set(symmx(qs[1]))
        q2 = set(qs[2])
        xq3 = set(symmx(qs[3]))
        q4 = set(qs[4])

        return len(xq1 - q2) + len(xq3 - q4)

    states = []

    seen = set([robots])
    states.append((tree_coeff(robots), 0, robots))

    i = 0
    while True:
        i += 1

        seen.add(robots)

        robots = moveall(robots)
        if robots in seen:
            break

        states.append((tree_coeff(robots), i, robots))

    states.sort()
    return states[0][1]


def parse(input):
    tuple_ = lambda s: tuple(map(int, s.split(",")))

    def robot(l):
        p, v = l.split()
        return tuple_(p[len("p="):]), tuple_(v[len("v="):])

    return tuple(map(robot, input.splitlines()))


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
