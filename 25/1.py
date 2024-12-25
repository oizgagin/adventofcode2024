from itertools import product


def solution(locks, keys):
    overlap = lambda lock, key: max(k + l for k, l in zip(lock, key)) >= 6
    return len(list(filter(lambda p: not overlap(*p), product(locks, keys))))


def parse(input):
    blocks = map(str.splitlines, input.split("\n\n"))

    is_lock = lambda block: all(ch == "#" for ch in block[0]) and all(ch == "." for ch in block[-1])
    is_key = lambda block: all(ch == "." for ch in block[0]) and all(ch == "#" for ch in block[-1])

    def parse(block, start, d):
        res = []
        for j in range(0, len(block[start])):
            i, c = start, 0
            while 0 <= i < len(block):
                if block[i][j] == "#": c += 1
                i += d
            res.append(c)
        return tuple(res)

    locks, keys = [], []
    for block in blocks:
        if is_lock(block):
            locks.append(parse(block, 1, 1))
        else:
            assert is_key(block)
            keys.append(parse(block, len(block)-2, -1))

    return locks, keys


def main():
    input = open("input", "r").read()
    print(solution(*parse(input)))


main()
