def solution(program):
    # 2 4 - B = A & 7
    # 1 1 - B = B ^ 1
    # 7 5 - C = A >> B
    # 1 5 - B = B ^ 5
    # 4 3 - B = B ^ C
    # 5 5 - out B
    # 0 3 - A = A >> 3
    # 3 0 - jnz A, 0

    # while A != 0:
    #   B = (a ^ 1) ^ 5 ^ (A >> (a ^ 1))
    #   out B & 7
    #   A >>= 3

    AA = [0]
    for num in program[::-1]:
        nexts = []
        for a in range(0, (1 << 3)):
            for A in AA:
                if ((a ^ 1) ^ 5 ^ (((A << 3) | a) >> (a ^ 1))) & 7 == num:
                    nexts.append((A << 3) | a)
        AA = nexts
    return min(AA)


def parse(input):
    program = list(map(int, input.splitlines()[4][len("Program: "):].split(",")))
    return program


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
