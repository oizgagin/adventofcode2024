from itertools import chain


def solution(initials):

    def apply(secret):
        secret = (secret ^ (secret * 64)) % 16777216
        secret = (secret ^ (secret // 32)) % 16777216
        secret = (secret ^ (secret * 2048)) % 16777216
        return secret

    dicts = []

    for secret in initials:
        dict_ = {}

        secrets = [secret % 10]
        changes = [secret % 10]

        for _ in range(0, 2000):
            secret = apply(secret)

            changes.append(secret % 10 - secrets[-1])
            secrets.append(secret % 10)

        for i, t in enumerate(zip(changes, changes[1:], changes[2:], changes[3:])):
            if t not in dict_:
                dict_[t] = secrets[i+4-1]

        dicts.append(dict_)

    allkeys = set(k for k in chain(*(dict_.keys() for dict_ in dicts)))

    max_ = float("-inf")
    for k in allkeys:
        res = 0
        for d in dicts:
            res += d.get(k, 0)
        max_ = max(max_, res)
    return max_


def parse(input):
    return map(int, input.splitlines())


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
