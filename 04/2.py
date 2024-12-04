def solution(wordsearch):

    is_valid = lambda i, j: 0 <= i < len(wordsearch) and 0 <= j < len(wordsearch[i])

    def neighs(i, j):
        coords = [(i + di, j + dj) for di in (-1, 1) for dj in (-1, 1)]
        if all(is_valid(*c) for c in coords):
            return coords

    res = 0
    for i in range(0, len(wordsearch)):
        for j in range(0, len(wordsearch[i])):
            if wordsearch[i][j] == 'A':
                ns = neighs(i, j)
                if not ns: continue

                w1 = (wordsearch[nsi][nsj] for nsi, nsj in (ns[0], ns[3]))
                w2 = (wordsearch[nsi][nsj] for nsi, nsj in (ns[1], ns[2]))

                if sorted(w1) == ['M', 'S'] and sorted(w2) == ['M', 'S']:
                    res += 1
    return res


def parse(input):
    return list(map(list, input.splitlines()))


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
