def solution(gates, wires):
    calculated = gates

    ops = {
        "OR": lambda x, y: x | y,
        "AND": lambda x, y: x & y,
        "XOR": lambda x, y: x ^ y,
    }

    zs = set(key for key in wires.keys() if key.startswith("z"))

    while not all(zkey in calculated for zkey in zs):
        for gate3, (gate1, gate2, op) in wires.items():
            if gate3 not in calculated:
                if gate1 in calculated and gate2 in calculated:
                    calculated[gate3] = ops[op](calculated[gate1], calculated[gate2])

    res = 0
    for zkey in sorted(zs, reverse=True):
        res = (res << 1) | calculated[zkey]
    return res


def parse(input):
    blocks = input.split("\n\n")

    gates = dict()
    for initial in blocks[0].splitlines():
        gate, value = initial.split(": ")
        gates[gate] = int(value)

    wires = dict()
    for wire in blocks[1].splitlines():
        gate1, op, gate2, _, gate3 = wire.split()
        wires[gate3] = (gate1, gate2, op)

    return gates, wires


def main():
    input = open("input", "r").read()
    print(solution(*parse(input)))


main()
