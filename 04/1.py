def solution(wordsearch):

    def neighs(i, j):
        is_valid = lambda i, j: 0 <= i < len(wordsearch) and 0 <= j < len(wordsearch[i])

        for di in (-1, 0, 1):
            for dj in (-1, 0, 1):
                if di == dj == 0: continue

                coords = [(i + di*d, j + dj*d) for d in range(0, 4)]
                if all(map(lambda c: is_valid(*c), coords)):
                    yield coords

    res = 0
    for i in range(0, len(wordsearch)):
        for j in range(0, len(wordsearch[i])):
            for coords in neighs(i, j):
                if [wordsearch[ni][nj] for ni, nj in coords] == ['X', 'M', 'A', 'S']:
                    res += 1

    return res


def parse(input):
    return list(map(list, input.splitlines()))


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
