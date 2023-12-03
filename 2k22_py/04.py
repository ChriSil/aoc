def part_one(data):
    overlap = lambda r1, r2: r1.issubset(r2) or r2.issubset(r1)
    return sum(overlap(set(range(x[0], x[1] + 1)), set(range(y[0], y[1] + 1))) for x, y in data)


def part_two(data):
    return sum(len(set(range(x[0], x[1] + 1)) & set(range(y[0], y[1] + 1))) > 0 for x, y in data)


if __name__ == "__main__":
    # with open("03input.txt", "r", encoding="utf-8") as input_values:
    #     inp_ut = input_values.read().splitlines()

    with open("04input.txt") as f:
        data = [y for y in [x.split(",") for x in f.read().splitlines()]]
        data = [(tuple(map(int, x.split("-"))), tuple(map(int, y.split("-")))) for x, y in data]
    print(f"Part One: {part_one(data)}")
    print(f"Part Two: {part_two(data)}")
