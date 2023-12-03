from itertools import count
from string import ascii_letters

# from adventofcode.inputs import get_input
# from adventofcode.utils import aoc_timer

CHARMAP = dict(zip(ascii_letters, count(1)))


def parse_input(input_str):
    return input_str.splitlines()


# @aoc_timer(1, 3, 2022)
def solve_first(rucksacks):
    priorities = 0
    for sack in rucksacks:
        mid = len(sack) // 2
        first = set(sack[:mid])
        second = set(sack[mid:])
        common = first.intersection(second).pop()
        priorities += CHARMAP[common]
    return priorities


# @aoc_timer(2, 3, 2022)
def solve_second(rucksacks):
    priorities = 0
    for i in range(0, len(rucksacks) - 2, 3):
        group = map(set, rucksacks[i: i + 3])
        common = set.intersection(*group).pop()
        priorities += CHARMAP[common]
    return priorities


if __name__ == "__main__":
    with open("03input.txt", "r", encoding="utf-8") as input_values:
        inp_ut = input_values.read().splitlines()
    # Test later= input2 = aocd.get_data(year=2022, day=3).splitlines()

    pri1 = solve_first(inp_ut)
    pri2 = solve_second(inp_ut)
    print(pri2)
