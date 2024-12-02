def solution(reports):

    def is_safe(level):
        inc, dec, maxd = True, True, float("-inf")
        for i in range(1, len(level)):
            dec = dec and (level[i-1] > level[i])
            inc = inc and (level[i-1] < level[i])
            maxd = max(maxd, abs(level[i-1] - level[i]))
        return (inc or dec) and 1 <= maxd <= 3

    def is_safe_problem_dampener(level):
        return any(is_safe(level[:i] + level[i+1:]) for i in range(0, len(level)))

    return len(list(filter(is_safe_problem_dampener, reports)))


def parse(input):
    return list(map(lambda s: tuple(map(int, s.split())), input.splitlines()))


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
