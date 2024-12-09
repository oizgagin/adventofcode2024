def solution(disk):
    blocks = []

    id_ = -1
    for i in range(0, len(disk)):
        block = None

        if i % 2 == 0:
            id_ += 1
            block = id_

        blocks.append([block, disk[i]])

    r = len(blocks)-1
    while r >= 0:
        rid, rl = blocks[r]
        if rid is None:
            r -= 1
            continue

        for l in range(0, r):
            lid, ll = blocks[l]
            if lid is not None: continue
            if ll < rl: continue

            assert lid is None
            assert ll >= rl

            blocks[l] = [rid, rl]

            if ll > rl:
                blocks.insert(l+1, [None, ll - rl])
                r += 1

            blocks[r] = [None, rl]
            break

        r -= 1


    bb = []
    for id_, len_ in blocks:
        for i in range(0, len_):
            bb.append(id_)

    res = 0
    for i, v in enumerate(bb):
        if v is not None:
            res += i * v
    return res


def parse(input):
    return tuple(map(int, input))


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
