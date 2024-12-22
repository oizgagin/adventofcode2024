def solution(initials):

    def apply(secret):
        secret = (secret ^ (secret * 64)) % 16777216
        secret = (secret ^ (secret // 32)) % 16777216
        secret = (secret ^ (secret * 2048)) % 16777216
        return secret

    res = 0

    for secret in initials:
        for _ in range(0, 2000):
            secret = apply(secret)
        res += secret
    return res


def parse(input):
    return map(int, input.splitlines())


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
