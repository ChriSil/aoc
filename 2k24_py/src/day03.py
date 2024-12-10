import os
import re


def solve_part_1(inp: str) -> str:
    sol = 0
    test = "mul(12,34) and mul(567,890) and mul(9,12)"
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.findall(pattern, inp)
    tuples = [(int(d1), int(d2)) for d1, d2 in matches]
    sol = sum((t[0]*t[-1])for t in tuples)
    return f'solution: {sol}'


def solve_part_2(inp: str) -> str:

    disable = r"don\'t\(\)"
    enable = r"do\(\)"
    test = "Some text before don't() content to delete do() and some text after."
    # Define invalid passages and remove them from inp
    invalid = f"{disable}.*?{enable}"
    mod_inp = re.sub(invalid, "", inp, flags=re.DOTALL)
    # call part 1 on modified input
    return solve_part_1(mod_inp)


if __name__ == '__main__':
    file_path = os.path.join(os.path.dirname(__file__), '../input/day03.txt')
    with open(file_path, 'r') as f:
        input = f.read().replace("\n", "")  # parse as one string, replacing linebreaks

    print(solve_part_1(input))

    print(solve_part_2(input))
