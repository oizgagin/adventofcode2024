def solution(machines):

    def solve(machine):
        (ax, ay), (bx, by), (prizex, prizey) = machine

        # A * ax + B * bx = prizex
        # A * ay + B * by = prizey

        # A * ax * ay + B * bx * ay = prizex * ay
        # A * ay * ax + B * by * ax = prizey * ax

        # B * (bx * ay - by * ax) = prizex * ay - prizey * ax

        # B = (prizex * ay - prizey * ax) / (bx * ay - by * ax)
        # A = (prizex * ay - B * bx * ay) / (ax * ay)

        v1 = prizex * ay - prizey * ax
        v2 = bx * ay - by * ax

        if v1 % v2 != 0: return 0, 0

        B = v1 // v2

        v3 = prizex * ay - B * bx * ay
        v4 = ax * ay

        if v3 % v4 != 0: return 0, 0

        return v3 // v4, B

    res = 0
    for machine in machines:
        a, b = solve(machine)
        res += 3 * a + b
    return res


def parse(input):
    machines = []
    for block in input.split("\n\n"):
        lines = block.splitlines()
        button_a = tuple(map(lambda s: int(s.strip()[2:]), lines[0][len("Button A: "):].split(",")))
        button_b = tuple(map(lambda s: int(s.strip()[2:]), lines[1][len("Button B: "):].split(",")))
        prize = tuple(map(lambda s: 10000000000000 + int(s.strip()[2:]), lines[2][len("Prize: "):].split(",")))
        machines.append((button_a, button_b, prize))
    return machines


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
