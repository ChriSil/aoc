import os


def solve_part_1(inp: list) -> str:
    sol = inp[0]

    return f'solution_part_1: {sol}'


def solve_part_2(inp: list) -> str:
    sol = inp[-1]

    return f'solution_part_2: {sol}'


def count_string_in_file(grid, target):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    target_len = len(target)
    reverse_target = target[::-1]
    count = 0

    # Helper to count occurrences of target and reverse in a sequence
    def count_both_directions(sequence):
        return sequence.count(target) + sequence.count(reverse_target)

    # Count in rows
    for row in grid:
        count += count_both_directions(row)

    # Count in columns
    for col in range(cols):
        column = ''.join(grid[row][col]
                         for row in range(rows) if col < len(grid[row]))
        count += count_both_directions(column)

    # Count in diagonals
    def diagonals(grid):
        # All diagonals from top-left to bottom-right
        for d in range(-rows + 1, cols):
            yield ''.join(grid[row][col] for row in range(rows)
                          for col in range(cols)
                          if col - row == d and row < len(grid) and col < len(grid[row]))
        # All diagonals from top-right to bottom-left
        for d in range(rows + cols - 1):
            yield ''.join(grid[row][col] for row in range(rows)
                          for col in range(cols)
                          if row + col == d and row < len(grid) and col < len(grid[row]))

    for diag in diagonals(grid):
        count += count_both_directions(diag)

    return count


def count_valid_diagonals(grid):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    count = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == "A":
                # Collect diagonal values
                diag1 = []  # Top-left to bottom-right
                diag2 = []  # Top-right to bottom-left

                # Check bounds and add characters to diagonal lists
                if row - 1 >= 0 and col - 1 >= 0:
                    diag1.append(grid[row - 1][col - 1])
                if row + 1 < rows and col + 1 < cols:
                    diag1.append(grid[row + 1][col + 1])
                if row - 1 >= 0 and col + 1 < cols:
                    diag2.append(grid[row - 1][col + 1])
                if row + 1 < rows and col - 1 >= 0:
                    diag2.append(grid[row + 1][col - 1])

                # Check conditions for both diagonals
                if diag1.count("M") == 1 and diag1.count("S") == 1 and \
                   diag2.count("M") == 1 and diag2.count("S") == 1:
                    count += 1

    return count


if __name__ == '__main__':
    file_path = os.path.join(os.path.dirname(__file__), '../input/day04.txt')
    with open(file_path, 'r') as f:
        # input = f.readlines()
        grid = [line.strip() for line in f.readlines()]
    print(grid)
    occurrences = count_string_in_file(grid=grid, target='XMAS')
    print(
        f"The string  or its reverse appears {occurrences} times.")
    result = count_valid_diagonals(grid)
    print(f"Count of 'A' that meet the condition: {result}")
    # print(solve_part_1(input))
    # print(solve_part_2(input))
