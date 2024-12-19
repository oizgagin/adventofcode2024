def solution(patterns, designs):

    def check(design):
        memo = {}

        def recurse(i):
            if i == len(design): return 1
            if i > len(design): return 0
            if i in memo: return memo[i]

            v = 0
            for j in range(i+1, len(design)+1):
                if design[i:j] in patterns:
                    v = v + recurse(j)
            memo[i] = v

            return v

        return recurse(0)

    return sum(map(check, designs))


def parse(input):
    patterns, designs = input.split("\n\n")
    patterns = set(patterns.split(", "))
    designs = designs.splitlines()
    return patterns, designs


def main():
    input = open("input", "r").read()
    print(solution(*parse(input)))


main()
