from collections import deque

with open('06input.txt') as file:
    line = file.read()


def solve(length):
    q = deque()
    for i, c in enumerate(line):
        q.append(c)
        if len(q) > length:
            q.popleft()
        if len(set(q)) == length:
            return i + 1


if __name__ == "__main__":
    # Part 1
    print(solve(4))

    # Part 2
    print(solve(14))
