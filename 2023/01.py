STR_DIGIT_MAP = {
    str_digit: str(i + 1)
    for i, str_digit in enumerate(["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"])
}


def parse(line):
    output = []
    while len(line) > 0:
        for digit in (list(STR_DIGIT_MAP.keys()) + list(STR_DIGIT_MAP.values())):
            if line.startswith(digit):
                output.append(digit)
                break

        line = line[1:]

    return output


def convert_word_to_number(str_digit):
    return STR_DIGIT_MAP.get(str_digit, str_digit)


with open("01.txt") as f:
    total = 0
    for line in f.readlines():
        result = parse(line)
        total += int(convert_word_to_number(result[0]) + convert_word_to_number(result[-1]))

    print(total)
