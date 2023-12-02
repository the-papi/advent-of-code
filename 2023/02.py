import re
from collections import defaultdict
from functools import reduce

BAG_CONFIGURATION = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def is_game_possible(str_hands):
    for str_hand in str_hands:
        for str_color in str_hand.strip().split(","):
            count, color = str_color.split()
            count = int(count)

            if count > BAG_CONFIGURATION[color]:
                return False

    return True


def main():
    with open("02.txt") as f:
        total = 0
        for line in f.readlines():
            result = re.search(r"Game (\d+):(.*)", line).groups()
            game_id = int(result[0])
            str_data = result[1]
            str_hands = str_data.split(";")

            if is_game_possible(str_hands):
                total += game_id  # game is possible

        print(total)


def find_minimum_set_main():
    with open("02.txt") as f:
        total = 0
        for line in f.readlines():
            min_set = defaultdict(lambda: 0)
            result = re.search(r"Game (\d+):(.*)", line).groups()
            str_data = result[1]
            str_hands = str_data.split(";")
            for str_hand in str_hands:
                for str_color in str_hand.strip().split(","):
                    count, color = str_color.split()
                    count = int(count)
                    min_set[color] = max(min_set[color], count)

            total += reduce(lambda a, b: a * b, min_set.values())

        print(total)


if __name__ == '__main__':
    main()
    find_minimum_set_main()
