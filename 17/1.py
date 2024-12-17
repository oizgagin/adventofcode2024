def solution(A, B, C, program):
    computer = {
        "A": A,
        "B": B,
        "C": C,
        "ip": 0,
        "outputs": [],
    }

    def combo(operand):
        if 0 <= operand <= 3: return operand
        if 4 <= operand <= 6: return computer["ABC"[operand-4]]
        assert False, "unreachable"

    def adv(operand):
        computer["A"] = int(computer["A"] / (2 ** combo(operand)))
        computer["ip"] += 2

    def bxl(operand):
        computer["B"] = computer["B"] ^ operand
        computer["ip"] += 2

    def bst(operand):
        computer["B"] = combo(operand) % 8
        computer["ip"] += 2

    def jnz(operand):
        if computer["A"] != 0:
            computer["ip"] = operand
        else:
            computer["ip"] += 2

    def bxc(operand):
        computer["B"] = computer["B"] ^ computer["C"]
        computer["ip"] += 2

    def out(operand):
        computer["outputs"].append(combo(operand) % 8)
        computer["ip"] += 2

    def bdv(operand):
        computer["B"] = int(computer["A"] / (2 ** combo(operand)))
        computer["ip"] += 2

    def cdv(operand):
        computer["C"] = int(computer["A"] / (2 ** combo(operand)))
        computer["ip"] += 2

    def eval_(instruction, operand):
        return [
            adv,
            bxl,
            bst,
            jnz,
            bxc,
            out,
            bdv,
            cdv,
        ][instruction](operand)

    while computer["ip"] < len(program):
        instruction, operand = program[computer["ip"]], program[computer["ip"]+1]
        eval_(instruction, operand)
    return ",".join(map(str, computer["outputs"]))


def parse(input):
    lines = input.splitlines()

    A = int(lines[0][len("Register A: "):])
    B = int(lines[1][len("Register B: "):])
    C = int(lines[2][len("Register C: "):])
    program = list(map(int, lines[4][len("Program: "):].split(",")))

    return A, B, C, program


def main():
    input = open("input", "r").read()
    print(solution(*parse(input)))


main()
