"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    subjects = load_subject_data(FILENAME)
    print_subject_data(subjects)


def load_subject_data(filename=FILENAME):
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(filename)
    subjects = []
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        subjects.append(parts)
    input_file.close()
    return subjects


def print_subject_data(subjects):
    """Print the subject data."""
    for subject in subjects:
        print(f"{subject[0]} is taught by {subject[1]:<12} and has {subject[2]:>3} students")


main()
