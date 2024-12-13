def solution(machines):

    def solve(machine):
        (ax, ay), (bx, by), (prizex, prizey) = machine

        for a in range(0, 101):
            for b in range(0, 101):
                if a * ax + b * bx == prizex and a * ay + b * by == prizey:
                    return a, b
        return 0, 0

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
        prize = tuple(map(lambda s: int(s.strip()[2:]), lines[2][len("Prize: "):].split(",")))
        machines.append((button_a, button_b, prize))
    return machines


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
