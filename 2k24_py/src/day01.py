import os


def solve_part_1(inp: list) -> str:
    # split in 2 lists
    split1, split2 = zip(*[map(int, line.split())
                         for line in (line.strip() for line in inp)])

    # sort by size
    split1 = sorted(split1)
    split2 = sorted(split2)

    # sum up absolute distances of each element between two list
    sol = sum(abs(split1[i] - split2[i]) for i in range(len(split1)))

    return f"Part 1 solved {sol}"


def solve_part_2(inp: list) -> str:
    # add up similarity scores
    # sim score is how often element of right list appears in right list
    # split in 2 lists
    split1, split2 = zip(*[map(int, line.split())
                         for line in (line.strip() for line in inp)])

    sim_score = sum(split1[i]*split2.count(split1[i])
                    for i in range(len(split1)))
    return f'Part 2 solved {sim_score}'


if __name__ == '__main__':
    file_path = os.path.join(os.path.dirname(__file__), '../input/day01.txt')
    with open(file_path, 'r') as f:
        data = f.readlines()

    print(solve_part_1(data))

    print(solve_part_2(data))
