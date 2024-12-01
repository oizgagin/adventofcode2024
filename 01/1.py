def solution(lists):
    return sum(
        map(
            lambda t: abs(t[0] - t[1]),
            zip(
                sorted(map(lambda t: t[0], lists)),
                sorted(map(lambda t: t[1], lists)),
            ),
        )
    )


def parse(input):
    return list(map(lambda s: tuple(map(int, s.split())), input.splitlines()))


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
