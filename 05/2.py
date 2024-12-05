from collections import defaultdict


def solution(order, updates):

    def is_valid(update):
        for i, p1 in enumerate(update):
            for p2 in update[i+1:]:
                if (p2, p1) in order:
                    return False
        return True

    def fix(update):
        update = list(update)
        for i in range(0, len(update)):
            for j in range(i+1, len(update)):
                pi, pj = update[i], update[j]
                if (pj, pi) in order:
                    update[i], update[j] = update[j], update[i]
        return update

    res = 0
    for update in updates:
        if not is_valid(update):
            fixed = fix(update)
            res += fixed[len(fixed)//2]
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
