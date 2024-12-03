import re
from functools import reduce


def solution(memory):
    eval_ = lambda mul: reduce(lambda acc, x: acc * x,  map(int, mul[len("mul("):-1].split(",")), 1)
    return sum(map(eval_, re.findall(r'mul\(\d+,\d+\)', memory)))


def parse(input):
    return input


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
