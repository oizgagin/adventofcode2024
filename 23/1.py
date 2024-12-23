from collections import defaultdict


def solution(lan):
    res = set()
    for key in lan.keys():
        if key.startswith("t"):
            for neigh in list(lan[key]):
                for v in lan[neigh] & lan[key]:
                    res.add(tuple(sorted((key, neigh, v))))
    return len(res)


def parse(input):
    lan = defaultdict(set)
    for v1, v2 in map(lambda s: s.split("-"), input.splitlines()):
        lan[v1].add(v2)
        lan[v2].add(v1)
    return lan


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
