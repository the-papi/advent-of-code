import re


def parse(file):
    with open(file) as f:
        for line in f.readlines():
            card_id, data = re.findall(r"^Card\s+(\d+):\s(.*)$", line)[0]
            winning_numbers_str, owning_numbers_str = data.split("|")
            winning_numbers = winning_numbers_str.strip().split()
            owning_numbers = owning_numbers_str.strip().split()
            yield card_id, winning_numbers, owning_numbers


def main():
    total = 0
    for card_id, winning_numbers, owning_numbers in parse("04.txt"):
        game_score = 0
        for owning_number in owning_numbers:
            if owning_number in winning_numbers:
                if game_score == 0:
                    game_score = 1
                else:
                    game_score *= 2
        total += game_score

    print(total)


def part_two_main():
    cards = {
        int(card_id): [winning_numbers, owning_numbers, 1]
        for card_id, winning_numbers, owning_numbers in parse("04.txt")
    }

    for card_id, (winning_numbers, owning_numbers, multiplier) in cards.items():
        matching_numbers = len(set(owning_numbers)) - len(set(owning_numbers) - set(winning_numbers))

        for i in range(matching_numbers):
            cards[card_id + i + 1][2] += 1 * multiplier

    total = 0
    for _, _, multiplier in cards.values():
        total += multiplier

    print(total)


if __name__ == '__main__':
    main()
    part_two_main()
