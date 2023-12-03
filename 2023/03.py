import re
from functools import reduce


def parse(file):
    with open(file) as f:
        return [x for x in f.readlines()]


def contains_symbol(text):
    for char in text:
        if char.isdigit() or char == "." or char == "\n":
            continue
        return True
    return False


def main():
    matrix = parse("03.txt")
    total = 0
    for i, row in enumerate(matrix):
        for match in re.finditer(r"\d+", row):
            number = int(row[match.start():match.end()])
            if (
                    (
                        i - 1 >= 0
                        and contains_symbol(
                            matrix[i - 1][max(0, match.start() - 1):min(match.end() + 1, len(row))]
                        )  # check previous line
                    )
                    or (
                        contains_symbol(row[max(0, match.start() - 1):match.start()])  # check previous char
                    )
                    or (
                        contains_symbol(row[match.end():min(match.end() + 1, len(row))])  # check next char
                    )
                    or (
                        i + 1 < len(matrix)
                        and contains_symbol(
                            matrix[i + 1][max(0, match.start() - 1): min(match.end() + 1, len(row))]
                        )  # check next line
                    )
            ):
                total += number

    print(total)


def find_whole_number(row, start_pos):
    i = start_pos
    result = ""
    # find backwards
    while row[i].isdigit():
        result = row[i] + result
        i -= 1

    # find forward
    if len(result) != 0:
        j = start_pos + 1
        while row[j].isdigit():
            result = result + row[j]
            j += 1
    else:
        return None

    return i + 1, j, result


def main_gear_ratio():
    matrix = parse("03.txt")
    total = 0
    for i, row in enumerate(matrix):
        last_pos = -1
        while True:
            asterisk_pos = row.find("*", last_pos + 1)
            if asterisk_pos == -1:
                break
            last_pos = asterisk_pos

            # find adjacent numbers
            # previous line
            numbers_prev_line = []
            if i - 1 >= 0 and (number := find_whole_number(matrix[i - 1], asterisk_pos)):
                numbers_prev_line.append(number)
            if i - 1 >= 0 and (number := find_whole_number(matrix[i - 1], asterisk_pos - 1)):
                numbers_prev_line.append(number)
            if i - 1 >= 0 and (number := find_whole_number(matrix[i - 1], asterisk_pos + 1)):
                numbers_prev_line.append(number)
            # current line
            numbers_cur_line = []
            if number := find_whole_number(matrix[i], asterisk_pos - 1):
                numbers_cur_line.append(number)
            if number := find_whole_number(matrix[i], asterisk_pos + 1):
                numbers_cur_line.append(number)
            # next line
            numbers_next_line = []
            if i + 1 < len(matrix) and (number := find_whole_number(matrix[i + 1], asterisk_pos)):
                numbers_next_line.append(number)
            if i + 1 < len(matrix) and (number := find_whole_number(matrix[i + 1], asterisk_pos - 1)):
                numbers_next_line.append(number)
            if i + 1 < len(matrix) and (number := find_whole_number(matrix[i + 1], asterisk_pos + 1)):
                numbers_next_line.append(number)

            numbers = (
                    [int(n) for _, _, n in set(numbers_prev_line)]
                    + [int(n) for _, _, n in set(numbers_cur_line)]
                    + [int(n) for _, _, n in set(numbers_next_line)]
            )

            if len(numbers) == 2:
                total += reduce(lambda a, b: a * b, numbers)

    print(total)


if __name__ == '__main__':
    # main()
    main_gear_ratio()
