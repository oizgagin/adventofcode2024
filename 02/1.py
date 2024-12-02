def solution(reports):

    def is_safe(level):
        inc, dec, maxd = True, True, float("-inf")
        for i in range(1, len(level)):
            dec = dec and (level[i-1] > level[i])
            inc = inc and (level[i-1] < level[i])
            maxd = max(maxd, abs(level[i-1] - level[i]))
        return (inc or dec) and 1 <= maxd <= 3

    return len(list(filter(is_safe, reports)))


def parse(input):
    return list(map(lambda s: tuple(map(int, s.split())), input.splitlines()))


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
