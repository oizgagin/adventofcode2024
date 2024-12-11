from collections import defaultdict


def solution(stones):
    def apply(c):
        c2 = defaultdict(int)

        c2[1] += c[0]
        c2[2024] += c[1]

        for stone, amount in c.items():
            if amount > 0:
                if len(str(stone)) % 2 == 0:
                    s = str(stone)
                    c2[int(s[:len(s)//2])] += amount
                    c2[int(s[len(s)//2:])] += amount
                elif stone > 1:
                    c2[stone * 2024] += amount

        return c2

    c = defaultdict(int)
    for stone in stones: c[stone] += 1

    for _ in range(0, 75): c = apply(c)
    return sum(c.values())


def parse(input):
    return list(map(int, input.split()))


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
