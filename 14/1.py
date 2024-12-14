from itertools import groupby


def solution(robots):
    X, Y = 101, 103

    def move(robot):
        p, v = robot
        return ((p[0] + v[0]) % X, (p[1] + v[1]) % Y), v

    def moveall(robots):
        return tuple(map(move, robots))

    for _ in range(100):
        robots = moveall(robots)

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

    res = 1
    for _, robots in groupby(filter(lambda robot: q(robot) != 0, sorted(robots, key=q)), key=q):
        res *= len(list(robots))
    return res


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
