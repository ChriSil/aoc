# A = Rock
# B = Paper
# C = Scissors
#
# X = Rock     ?
# Y = Paper   ?
# Z = Scissors    ?
#
# Total Score =   shape:  Rock = 1
#                         Paper = 2
#                         Scissors = 3
#                 score:  loss = 0
#                         draw = 3
#                         win = 6
#
#


def part_one(data):
    '''
    A, X = Rock 1 point
    B, Y = Paper 2 points
    C, Z = Scissors 3 points
    win = 6 points
    lose = 0 points
    draw = 3 points
    '''
    guide = {'A X': 1 + 3, 'A Y': 2 + 6, 'A Z': 3 + 0,
             'B X': 1 + 0, 'B Y': 2 + 3, 'B Z': 3 + 6,
             'C X': 1 + 6, 'C Y': 2 + 0, 'C Z': 3 + 3
             }  # dict with explicit results, calcs automatically. could also create mapped dict with just the sums
    sum = 0
    for rnd in data:
        a = guide[rnd]
        sum = sum + a
    return sum

    # return sum([guide[rnd] for rnd in data])


def part_two(data):
    '''
    A, X = Rock 1 point
    B, Y = Paper 2 points
    C, Z = Scissors 3 points
    win = 6 points
    X= lose = 0 points
    draw = 3 points
    '''
    guide = {'A X': 0 + 3, 'A Y': 3 + 1, 'A Z': 6 + 2,
             'B X': 0 + 1, 'B Y': 3 + 2, 'B Z': 6 + 3,
             'C X': 0 + 2, 'C Y': 3 + 3, 'C Z': 6 + 1
             }  # dict with explicit results, calcs automatically. could also create mapped dict with just the sums
    return sum([guide[rnd] for rnd in data])


if __name__ == "__main__":
    with open("02input.txt", "r", encoding="utf-8") as input_values:
        input = input_values.read().splitlines()

    a = part_one(input)
    print(a)
    b = part_two(input)
    print(b)
    print('Fertig du Wassersack')

# for item in rounds:
#     sum = sum + calcsum(item)


# def process_input(input: str) -> list[str]:
#     """Read the text file and read into a list of lists containing calories for each elf"""
#     pairs = input.split("\n")
#
#     return pairs

# def calcsum(elem: str) -> int:
#     # A = X
#     # B = Y
#     # C = Z
#     list = elem.split()
#     # if list[0] == 'A':
#
#     if elem is not None:
#         add = 1
#     else:
#         add = 0
#     return add
