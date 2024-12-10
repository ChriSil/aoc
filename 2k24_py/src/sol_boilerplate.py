import os


def solve_part_1(inp: list) -> str:
    sol = inp[0]

    return f'solution_part_1: {sol}'


def solve_part_2(inp: list) -> str:
    sol = inp[-1]

    return f'solution_part_2: {sol}'


if __name__ == '__main__':
    file_path = os.path.join(os.path.dirname(__file__), '../input/day01.txt')
    with open(file_path, 'r') as f:
        input = f.readlines()

    print(solve_part_1(input))

    print(solve_part_2(input))
