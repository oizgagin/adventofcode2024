def solution(eqs):

    def calibration(eq):
        expected, numbers = eq

        def recurse(curr, i):
            if i >= len(numbers):
                return curr == expected

            return any([
                recurse(curr * numbers[i], i+1),
                recurse(curr + numbers[i], i+1),
                recurse(int(str(curr) + str(numbers[i])), i+1)
            ])

        return expected if recurse(numbers[0], 1) else 0

    return sum(list(map(calibration, eqs)))


def parse(input):
    return list(map(lambda s: (int(s.split(":")[0]), tuple(map(int, s.split(":")[1].split()))), input.splitlines()))


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
