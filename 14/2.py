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

    def tree_coeff(robots):
        xs = list(map(lambda r: r[0][0], robots))
        meanx = sum(xs) / len(xs)

        ys = list(map(lambda r: r[0][1], robots))
        meany = sum(ys) / len(ys)

        return (
            sum(map(lambda x: ((x - meanx) ** 2) / (len(xs) - 1), xs)) *
            sum(map(lambda y: ((y - meany) ** 2) / (len(ys) - 1), ys))
        )

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
