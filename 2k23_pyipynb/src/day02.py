from pathlib import Path
import re
# import math

gameRegex = re.compile(r"Game (\d+): (.*)$")
colorRegex = re.compile(r"(\d+) (.*)")
limits = {"red": 12, "green": 13, "blue": 14}


def part1(line):

    match = gameRegex.search(line)  # turns line in regex object
    # splits the body of the match obj into list like '4 green'
    for color in match[2].replace(";", ",").split(", "):
        colorMatch = colorRegex.search(color)
        if int(colorMatch[1]) > limits[colorMatch[2]]:
            return 0
    # =print(int(match[1]))
    return int(match[1])


def part2(line):
    match = gameRegex.search(line)
    minimas = {"red": 0, "green": 0, "blue": 0}
    for color in match[2].replace(";", ",").split(", "):
        colorMatch = colorRegex.search(color)
        value = int(colorMatch[1])
        color = colorMatch[2]
        if value > minimas[color]:
            minimas[color] = value

    return minimas["red"] * minimas["green"] * minimas["blue"]


if __name__ == '__main__':
    file_path = 'input/day02.txt'
    with open(file_path, 'r', encoding="utf-8") as f:
        lines = f.readlines()
    # solve_part_1(data)
    result = [part1(line) for line in lines]
    print("part1: ", sum(result))
    result = [part2(line) for line in lines]
    print("part2: ", sum(result))
