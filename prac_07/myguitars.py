"""My Guitars exercise."""

from prac_07.guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Load guitars from a file, add new guitars, sort them, then save the file."""
    guitars = load_guitars()
    get_new_guitars(guitars)
    guitars.sort()
    for guitar in guitars:
        print(guitar)
    save_guitars(guitars)


def load_guitars():
    """Read the guitars from a file and save them as a list of objects."""
    guitars = []
    with open(FILENAME, 'r') as in_file:
        for line in in_file:
            parts = line.strip().split(",")
            guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
            guitars.append(guitar)
    return guitars


def get_new_guitars(guitars):
    """Get new guitars until a blank name is entered."""
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar_to_add = Guitar(name, year, cost)
        guitars.append(guitar_to_add)
        print(guitar_to_add.name, "added.")
        name = input("Name: ")


def save_guitars(guitars):
    """Save guitars to a file."""
    with open(FILENAME, "w") as out_file:
        for guitar in guitars:
            guitar_to_add = [guitar.name, str(guitar.year), str(guitar.cost)]
            print(",".join(guitar_to_add), file=out_file)


main()
