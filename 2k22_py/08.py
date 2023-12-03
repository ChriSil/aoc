# 2022 Advent of Code Day 8
import os

# from File_Location import Day8_2022
Day08_2022 = open("08input.txt", "r").read()


def visible_trees(data: str, part: int) -> int:
    # If input looks like a file, open file. Read resulting tree grid info.
    if isinstance(data, str) and os.path.isfile(data):
        with open(data) as f:  # Reading input file.
            data = f.read().splitlines()
        f.close()
    else:
        data = data.splitlines()  # Read test data.

    scenic_max: int = 0
    tree_count: int = 0
    tree_rows: int = len(data)
    tree_cols: int = len(data[0])
    tree_perimeter: int = (tree_cols * 2 + tree_rows * 2) - 4  # Minus overlap.

    for rows in range(1, tree_rows - 1):
        for cols in range(1, tree_cols - 1):
            tree_size = data[rows][cols]  # Individual tree.
            scenic_list: list = []  # Reset scenic score calc.

            # If length of filtered list in is zero, tree is visible from direction. Outside in.
            left: int = len([x for x in data[rows][:cols] if x >= tree_size])  # (1 to x-1)
            right: int = len([x for x in data[rows][cols + 1:] if x >= tree_size])  # (x+1 to nx_trees-1)
            up: int = len([y[cols] for y in data[:rows] if y[cols] >= tree_size])  # (1 to y-1)
            down: int = len([y[cols] for y in data[rows + 1:] if y[cols] >= tree_size])  # (y+1 to ny_trees-1)

            # Count trees visible from given point and mult to get scenic score. Inside out.
            left_2: list = list(reversed([x for x in data[rows][:cols]]))  # (x-1 to 1)
            right_2: list = [x for x in data[rows][cols + 1:]]  # (x+1 to nx_trees-1)
            up_2: list = list(reversed([y[cols] for y in data[:rows] if y[cols]]))  # (y-1 to 1)
            down_2: list = [y[cols] for y in data[rows + 1:] if y[cols]]  # (y+1 to ny_trees-1)
            scenic_grid: list = [left_2, right_2, up_2, down_2]

            # Determine if any outside view lines to the tree exist, count+ if so.
            if left == 0 or right == 0 or up == 0 or down == 0:
                tree_count += 1  # Count visible trees P1.
            # Determine trees for scenic view score. If grid tree >= tree_size: break & count.
            for dir in scenic_grid:
                for d in range(len(dir)):
                    if dir[d] >= tree_size: break
                scenic_list.append(d + 1)

            scenic_score = scenic_list[0] * scenic_list[1] * scenic_list[2] * scenic_list[3]
            scenic_max = max(scenic_max, scenic_score)  # Find highest score P2

    if part == 1: total_visible_trees = tree_count + tree_perimeter
    if part == 2: total_visible_trees = scenic_max
    return total_visible_trees


if __name__ == "__main__":
    # Part 1 - How many trees are visible from outside the grid?
    print("P1 - Visible trees from outside grid: %d" % visible_trees(Day08_2022, 1))
    # Part 2 - What is the highest scenic score possible for any tree?
    print("P2 - Highest scenic score: %d" % visible_trees(Day08_2022, 2))
