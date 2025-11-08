"""Project Management Client Side Code.
Estimate: 60 minutes
Actual: 2.5 hours over 3 days
"""

from prac_07.project import Project
import datetime

MENU = "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new project\n- (U)pdate project\n- (Q)uit"
FILENAME = "projects.txt"
HEADER_LINE = "Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage"


def main():
    """Load projects, then alter/display/load projects in different ways, then save and/or quit."""
    print("Welcome to Pythonic Project Management")
    projects = load_projects()
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            load_filename = get_valid_input("Load file name: ")
            projects = load_projects(load_filename)
        elif choice == "S":
            save_filename = get_valid_input("Save file name: ")
            save_projects(save_filename, projects)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_by_date(projects)
        elif choice == "A":
            add_project(projects)
        elif choice == "U":
            update_project(projects)
        else:
            print("Invalid input")
        print(MENU)
        choice = input(">>> ").upper()
    print(f"Would you like to save to {FILENAME}? no, I think not.")
    print("Thank you for using custom-built project management software.")


def load_projects(filename=FILENAME):
    """Load projects from a file."""
    projects = []
    try:
        with open(filename, "r") as in_file:
            in_file.readline()  # Ignore header line
            for line in in_file:
                parts = line.strip("\n").split("\t")
                project = Project(parts[0], datetime.datetime.strptime(parts[1], "%d/%m/%Y").date(), int(parts[2]),
                                  float(parts[3]), int(parts[4]))
                projects.append(project)
        print(f"Loaded {len(projects)} projects from {filename}")
        return projects
    except FileNotFoundError:
        print("Specified file does not exist, please try again.")


def get_valid_input(prompt):
    """Get a valid input given a prompt."""
    choice = input(prompt)
    while choice == "":
        print("Invalid input")
        choice = input(prompt)
    return choice


def save_projects(filename, projects):
    """Save projects to a file."""
    with open(filename, "w") as out_file:
        print(HEADER_LINE, file=out_file)
        for project in projects:
            project_to_save = [project.name, project.start_date.strftime("%d/%m/%Y"), str(project.priority),
                               str(project.cost_estimate),
                               str(project.completion_percentage)]
            print("\t".join(project_to_save), file=out_file)
    print(f"Saved {len(projects)} projects to {filename}")


def display_projects(projects):
    """Display projects, sorted by priority and sectioned as incomplete and complete."""
    print("Incomplete projects:")
    incomplete_projects = [project for project in projects if project.completion_percentage != 100]
    incomplete_projects.sort()
    for incomplete_project in incomplete_projects:
        print(f"  {incomplete_project}")
    print("Complete projects:")
    complete_projects = [project for project in projects if project.completion_percentage == 100]
    complete_projects.sort()
    for complete_project in complete_projects:
        print(f"  {complete_project}")


def get_valid_number(prompt, minimum, maximum):
    """Get a valid number given a prompt and a maximum and minimum value."""
    is_valid_number = False
    while not is_valid_number:
        try:
            choice = int(input(prompt))
            if choice < minimum or choice > maximum:
                print(f"Input must be between {minimum} and {maximum} inclusive.")
            else:
                is_valid_number = True
        except ValueError:
            print("Invalid input - must be an integer")
    return choice


def get_valid_float(prompt):
    """Get a valid float given a prompt."""
    is_valid_float = False
    while not is_valid_float:
        try:
            choice = float(input(prompt))
            if choice < 0:
                print("Input must be >= 0")
            else:
                is_valid_float = True
        except ValueError:
            print("Invalid input - must be a float")
    return choice


def add_project(projects):
    """Add a project to the list of projects"""
    print("Let's add a new project")
    name = get_valid_input("Name: ")
    start_date = input("Start date (dd/mm/yy): ")
    priority = get_valid_number("Priority: ", 1, 10)
    cost_estimate = get_valid_float("Cost Estimate: $")
    percentage_complete = get_valid_number("Percent complete: ", 0, 100)
    projects.append(Project(name, start_date, priority, cost_estimate, percentage_complete))


def get_valid_index(prompt, projects):
    """Get a valid index given a prompt."""
    is_valid_index = False
    while not is_valid_index:
        try:
            choice = int(input(prompt))
            if choice < 0 or choice > (len(projects) - 1):
                print("Invalid project choice.")
            else:
                is_valid_index = True
        except ValueError:
            print("Invalid input - must be an integer")
    return choice


def get_new_number(prompt, minimum, maximum):
    """Get a new number given a minimum and maximum number"""
    choice = input(prompt)
    if choice != "":
        while int(choice) < minimum or int(choice) > maximum:
            print(f"Input must be between {minimum} and {maximum} inclusive.")
            choice = input(prompt)
    return choice


def filter_by_date(projects):
    """Filter projects after a user inputted date."""
    after_date = datetime.datetime.strptime(get_valid_input("Show projects that start after date (dd/mm/yyyy): "),
                                            "%d/%m/%Y").date()
    for project in projects:
        if project.is_older(after_date):
            print(project)


def update_project(projects):
    """Update a project's priority and/or completion percentage."""
    for i, project in enumerate(projects):
        print(i, project)
    project_index = get_valid_index("Project choice: ", projects)
    print(projects[project_index])
    new_percentage = get_new_number("New Percentage: ", 0, 100)
    if new_percentage != "":
        projects[project_index].completion_percentage = new_percentage
    new_priority = get_new_number("New Priority: ", 1, 10)
    if new_priority != "":
        projects[project_index].completion_percentage = new_priority


main()
