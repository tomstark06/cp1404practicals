"""Score menu program."""
from score import determine_result

MENU = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""


def main():
    score = get_valid_score()
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            result = determine_result(score)
            print(result)
        elif choice == "S":
            print_symbols(score)
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Farewell.")


def get_valid_score():
    """Get a valid score."""
    score = float(input("Score: "))
    while score < 0 or score > 100:
        print("Invalid score.")
        score = float(input("Score: "))
    return score


def print_symbols(score, symbol="*"):
    """Print symbols."""
    print(symbol * int(score))


main()
