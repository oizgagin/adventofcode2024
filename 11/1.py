def solution(stones):

    def apply():
        i = 0
        while i < len(stones):
            s = str(stones[i])

            if stones[i] == 0:
                stones[i] = 1
                i += 1
            elif len(s) % 2 == 0:
                stones[i] = int(s[:len(s)//2])
                stones.insert(i+1, int(s[len(s)//2:]))
                i += 2
            else:
                stones[i] *= 2024
                i += 1

    for _ in range(0, 25): apply()
    return len(stones)


def parse(input):
    return list(map(int, input.split()))


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
