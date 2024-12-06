def solution(map_):
    move_p = lambda p, d: (p[0] + d[0], p[1] + d[1])
    get_p = lambda p: map_[p[0]][p[1]]
    in_p = lambda p: 0 <= p[0] < len(map_) and 0 <= p[1] < len(map_[p[0]])
    def set_p(p, ch): map_[p[0]][p[1]] = ch

    dirs = ((-1, 0), (0, 1), (1, 0), (0, -1))

    def walk(p, d):
        while True:
            nextp = move_p(p, dirs[d])
            if not in_p(nextp):
                return

            if get_p(nextp) in '.^':
                yield (nextp, d)
                p = nextp
                continue

            assert get_p(nextp) == '#', (nextp, get_p(nextp))
            d = (d + 1) % len(dirs)

    def loops(p, d):
        visited = set()
        for pp, dd in walk(p, d):
            if (pp, dd) in visited:
                return True
            visited.add((pp, dd))
        return False

    start = [(i, j) for i in range(0, len(map_)) for j in range(0, len(map_[1])) if map_[i][j] == '^'][0]

    obstructions = set()
    for p, d in walk(start, 0):
        if get_p(p) in '.^':
            set_p(p, '#')
            if loops(start, 0):
                obstructions.add(p)
            set_p(p, '.')
    return len(obstructions)


def parse(input):
    return [list(s) for s in input.splitlines()]


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
