def solution(map_):
    move_p = lambda p, d: (p[0] + d[0], p[1] + d[1])
    get_p = lambda p: map_[p[0]][p[1]]
    in_p = lambda p: 0 <= p[0] < len(map_) and 0 <= p[1] < len(map_[p[0]])

    dirs = ((-1, 0), (0, 1), (1, 0), (0, -1))

    currp = [(i, j) for i in range(0, len(map_)) for j in range(0, len(map_[1])) if map_[i][j] == '^'][0]

    currd, visited = 0, set([currp])
    while True:
        nextp = move_p(currp, dirs[currd])
        if not in_p(nextp):
            return len(visited)

        if get_p(nextp) in '.^':
            visited.add(nextp)
            currp = nextp
            continue

        assert get_p(nextp) == '#', (nextp, get_p(nextp))

        currd = (currd + 1) % len(dirs)


def parse(input):
    return [list(s) for s in input.splitlines()]


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
