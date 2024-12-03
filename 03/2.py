import re
from functools import reduce


def solution(memory):
    eval_ = lambda mul: reduce(lambda acc, x: acc * x,  map(int, mul[len("mul("):-1].split(",")), 1)

    enabled = True

    sum_ = 0
    for instr in re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", memory):
        if 'mul' in instr:
            if enabled: sum_ += eval_(instr)
        elif "don't" in instr:
            enabled = False
        else:
            enabled = True
    return sum_


def parse(input):
    return input


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
