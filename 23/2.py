from collections import defaultdict


def solution(lan):

    def build(node):
        curr = set([node])
        for key in lan.keys():
            if key in curr: continue
            if all(key in lan[v] for v in curr):
                curr.add(key)
        return curr

    max_ = set()
    for key in lan.keys():
        component = build(key)
        if len(component) > len(max_): max_ = component
    return ",".join(sorted(max_))


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
