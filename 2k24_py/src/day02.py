import os


def solve_part_1(inp: list) -> str:
    # number of lines that evaluate to true
    sol = 0
    for line in inp:
        deltas = [line[i + 1] - line[i] for i in range(len(line) - 1)]
        if (all(x > 0 for x in deltas) or all(x < 0 for x in deltas)) and all(1 <= abs(x) <= 3 for x in deltas) and all(x != 0 for x in deltas):
            sol += 1

    return f'solution_part_1: {sol}'


# [4, 5, 6, 2, -2](3*1=3)
# [4, 5, 6, 2, 2](5*0) = 0
# [4, 5, 6, -2, -2](3*2=6)


# (if min(sum(1 for x in deltas if x > 0),
#  sum(1 for x in deltas if x < 0)) > 1, 1 else 0)
# (sum(1 for x in deltas if x > 0) *
#               sum(1 for x in deltas if x < 0))


def solve_part_2(inp: list) -> str:
    """
    flawed logic, passing one penalty is not good enough.
    instead, try same func for each list variant with one element removed
    """
    sol = 0
    for line in inp:
        deltas = [line[i + 1] - line[i] for i in range(len(line) - 1)]
        c1 = (min(sum(1 for x in deltas if x > 0),
              sum(1 for x in deltas if x < 0)))
        c2 = sum(1 for x in deltas if not 0 <= abs(x) <= 3)
        c3 = sum(1 for x in deltas if x == 0)

        s = (c1+c2+c3)
        if s <= 1:
            sol += 1
    return f'solution_part_2: {sol}'


if __name__ == '__main__':
    file_path = os.path.join(os.path.dirname(__file__), '../input/day02.txt')
    with open(file_path, 'r') as f:
        data = f.readlines()

    # strip linebreaks, convert each elem to int, split by whitespaces
    stripped_data = [[int(x) for x in line.strip().split()] for line in data]

    print(solve_part_1(stripped_data))

    print(solve_part_2(stripped_data))

    def is_safe(row):
        inc = [row[i + 1] - row[i] for i in range(len(row) - 1)]
        if set(inc) <= {1, 2, 3} or set(inc) <= {-1, -2, -3}:
            return True
        return False

    # data = [[int(y) for y in x.split(' ')] for x in open('02.txt').read().split('\n')]
    data = stripped_data
    safe_count = sum([is_safe(row) for row in data])
    print(safe_count)

    safe_count = sum([any([is_safe(row[:i] + row[i + 1:])
                     for i in range(len(row))]) for row in data])
    print(safe_count)
