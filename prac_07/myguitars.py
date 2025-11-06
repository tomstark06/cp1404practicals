"""My Guitars exercise."""

from prac_07.guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """"""
    guitars = read_file()
    for guitar in guitars:
        print(guitar)


def read_file():
    """Read the guitars from a file and save them as a list of objects."""
    guitars = []
    with open(FILENAME, 'r') as in_file:
        for line in in_file:
            parts = in_file.readline().strip().split(",")
            year = float(parts[2])
            guitar = Guitar(parts[0], parts[1], year)
            guitars.append(guitar)
    return guitars


main()
