"""Guitar class definition
Estimate: 30 minutes
Actual:
"""

CURRENT_YEAR = 2025
VINTAGE_THRESHOLD = 50


class Guitar:
    """Represent a Guitar object."""

    def __init__(self, name="", year=0, cost=0.0):
        """Initialise a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a formatted string of a Guitar object."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def __repr__(self):
        """Return a formatted string of a Guitar object."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def __lt__(self, other):
        """Return the result of comparing two Guitar objects with less than."""
        return self.year < other.year

    def get_age(self):
        """Get the age of a guitar based on the current year."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine if the guitar is vintage based on the current age of the guitar."""
        return Guitar.get_age(self) >= 50
