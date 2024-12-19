def solution(patterns, designs):

    def check(design):
        memo = {}

        def recurse(i):
            if i == len(design): return True
            if i > len(design): return False
            if i in memo: return memo[i]

            v = False
            for j in range(i+1, len(design)+1):
                if design[i:j] in patterns:
                    v = v or recurse(j)
            memo[i] = v

            return v

        return recurse(0)

    return len(list(filter(check, designs)))


def parse(input):
    patterns, designs = input.split("\n\n")
    patterns = set(patterns.split(", "))
    designs = designs.splitlines()
    return patterns, designs


def main():
    input = open("input", "r").read()
    print(solution(*parse(input)))


main()
