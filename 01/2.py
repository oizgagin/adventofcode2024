from collections import Counter


def solution(lists):
    c = Counter(map(lambda t: t[1], lists))
    return sum(n * c[n] for n in map(lambda t: t[0], lists))


def parse(input):
    return list(map(lambda s: tuple(map(int, s.split())), input.splitlines()))


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
