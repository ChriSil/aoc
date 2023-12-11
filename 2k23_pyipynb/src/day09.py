file_path = 'C:\\Users\\CSILLER\\code\\aoc\\2k23_pyipynb\\input\\day09.in'

with open(file_path) as file:
    data = file.read()


def get_extensions(seq: list[int]) -> tuple[int, int]:
    if not any(seq):
        return 0, 0
    pre, post = get_extensions([v2 - v1 for v1, v2 in zip(seq, seq[1:])])
    return seq[0] - pre, seq[-1] + post


def solve(text: str) -> None:
    sequences = [[int(x) for x in line.split()]
                 for line in text.strip().splitlines()]
    pre_post_list = [get_extensions(seq) for seq in sequences]
    print(sum(post for _, post in pre_post_list))
    print(sum(pre for pre, _ in pre_post_list))


solve(data)
