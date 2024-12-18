from collections import defaultdict


def solution(coords):
    X, Y = 70, 70

    grid = defaultdict(lambda: ".")

    def bfs():
        c, q, visited = 0, [(0, 0)], set([(0, 0)])
        while len(q) > 0:
            q2 = []
            for i, j in q:
                for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    if grid[(i+di, j+dj)] == "." and (i+di, j+dj) not in visited and 0 <= i+di <= X and 0 <= j+dj <= Y:
                        if i+di == j+dj == 70:
                            return c+1

                        visited.add((i+di, j+dj))
                        q2.append((i+di, j+dj))

            q = q2
            c += 1

        return None

    for coord in coords:
        grid[coord] = "#"
        if bfs() is None:
            return coord


def parse(input):
    return list(map(lambda s: tuple(map(int, s.split(","))), input.splitlines()))


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
