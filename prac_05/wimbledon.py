"""
Wimbledon exercise
Estimate: 30 min
Actual: 25 min
"""

FILENAME = "wimbledon.csv"
ENCODING = "utf-8-sig"


def main():
    """Print the wimbledon winner, with how many times they have won and which countries have won."""
    records = load_records()
    champion_to_number_of_wins, winning_countries = process_records(records)
    print_results(champion_to_number_of_wins, winning_countries)


def print_results(champion_to_number_of_wins, winning_countries):
    print("Wimbledon Champions:")
    for champion, number_of_wins in champion_to_number_of_wins.items():
        print(champion, number_of_wins)
    print()
    print(f"These {len(winning_countries)} countries have won Wimbledon:")
    print(", ".join(winning_countries))


def process_records(records):
    champion_to_number_of_wins = {}
    winning_countries = set()
    for record in records:
        number_of_wins = champion_to_number_of_wins.get(record[2], 0)
        champion_to_number_of_wins[record[2]] = number_of_wins + 1
        winning_countries.add(record[1])
    return champion_to_number_of_wins, winning_countries


def load_records():
    records = []
    with open(FILENAME, "r", encoding=ENCODING) as in_file:
        in_file.readline()
        for line in in_file:
            records.append(line.strip().split(","))
    return records


main()
