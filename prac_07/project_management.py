"""Project Management Client Side Code.
Estimate: 60 minutes
Actual: 3:55 -
"""

from prac_07.project import Project

MENU = "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new project\n- (U)pdate project\n- (Q)uit"
FILENAME = "projects.txt"


def main():
    """"""
    print("Welcome to Pythonic Project Management")
    projects = load_projects()
    print(f"Loaded {len(projects)} projects from {FILENAME}")
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            print()
        elif choice == "S":
            print()
        elif choice == "D":
            print()
        elif choice == "F":
            print()
        elif choice == "A":
            print()
        elif choice == "U":
            print()
        else:
            print("Invalid input")
        print(MENU)
        choice = input(">>> ").upper()
    print()


def load_projects():
    projects = []
    with open(FILENAME, "r") as in_file:
        in_file.readline()  # Ignore header line
        for line in in_file:
            parts = line.strip("\n").split("\t")
            project = Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4]))
            projects.append(project)
    return projects


main()
