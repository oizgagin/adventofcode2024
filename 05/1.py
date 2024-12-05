from collections import defaultdict


def solution(order, updates):

    def is_valid(update):
        for i, p1 in enumerate(update):
            for p2 in update[i+1:]:
                if (p2, p1) in order:
                    return False
        return True

    res = 0
    for update in updates:
        if is_valid(update):
            res += update[len(update)//2]
    return res


def parse(input):
    order, updates = input.split("\n\n")

    order = set([tuple(map(int, o.split("|"))) for o in order.splitlines()])
    updates = [tuple(map(int, u.split(","))) for u in updates.splitlines()]

    return order, updates


def main():
    input = open("input", "r").read()
    print(solution(*parse(input)))


main()
