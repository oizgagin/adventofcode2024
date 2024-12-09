def solution(disk):
    blocks = []

    id_ = -1
    for i in range(0, len(disk)):
        block = None

        if i % 2 == 0:
            id_ += 1
            block = id_

        for _ in range(0, disk[i]):
            blocks.append(block)

    l, r = disk[0], len(blocks)-1
    while l <= r:
        if blocks[l] is not None:
            l += 1
            continue

        if blocks[r] is None:
            r -= 1
            continue

        blocks[l] = blocks[r]
        l += 1
        r -= 1

    res = 0
    for i, v in enumerate(blocks[:l]):
        res += i * v
    return res


def parse(input):
    return tuple(map(int, input))


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
