import re


def replace_with_numeric_values(text):
    # did not work because iterates over dict and finds matcehs in order of string. thus eightwoada will turn into eigh2ada, not 8woada.
    numbers_map = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    # Iterate through the dictionary keys and replace occurrences in the text
    for word, number in numbers_map.items():
        text = text.replace(word, str(number))
    return text


def solve_part_1(data):
    solution = 0
    for line in data:

        nums = re.findall(r'\d', line)
        first_digit = str(nums[0])
        last_digit = str(nums[-1])
        concat_num = int(first_digit + last_digit)
        solution += concat_num
    return (solution)


def solve_part_2(data):
    solution = 0
    digits = ["zero", "one", "two", "three", "four",
              "five", "six", "seven", "eight", "nine"]  # very clever. list index equals int value of text
    for line in data:
        nums = []
        for i in range(len(line)):
            if line[i] >= '0' and line[i] <= '9':
                nums.append(int(line[i]))
            p = line[i:]
            for d in range(10):
                if p.startswith(digits[d]):
                    nums.append(d)
        solution += nums[0]*10 + nums[-1]
    return solution


if __name__ == '__main__':
    file_path = 'input/day01.txt'
    with open(file_path, 'r') as f:
        data = f.readlines()

    print(solve_part_1(data))
    print(solve_part_2(data))

    print('done')
