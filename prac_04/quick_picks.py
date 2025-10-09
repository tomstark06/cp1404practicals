"""Quick picks exercise."""

import random

MINIMUM = 1
MAXIMUM = 45
NUMBERS_PER_QUICK_PICK = 6


def main():
    """Print the number of quick picks requested by the user."""
    number_of_quick_picks = int(input("How many quick picks? "))
    print_quick_picks(number_of_quick_picks)


def print_quick_picks(number_of_quick_picks):
    """Print quick picks."""
    for i in range(number_of_quick_picks):
        quick_picks = []
        for j in range(NUMBERS_PER_QUICK_PICK):
            number = random.randint(MINIMUM, MAXIMUM)
            while number in quick_picks:
                number = random.randint(MINIMUM, MAXIMUM)
            quick_picks.append(number)
        quick_picks.sort()
        print(" ".join(f"{number:>2}" for number in quick_picks))


main()
