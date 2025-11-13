"""Project class definition."""


class Project:
    """Represent a Project Object."""

    def __init__(self, name, start_date, priority=0, cost_estimate=0.0, completion_percentage=0):
        """Initialise a Project instance."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __repr__(self):
        """Return a formatted string of a Project object."""
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: {self.cost_estimate:.2f}, completion: {self.completion_percentage}%"

    def __lt__(self, other):
        """Return the result of comparing two Project objects, compare by priority."""
        return self.priority < other.priority

    def is_older(self, after_date):
        """Return a boolean for if a Project object is on or after a given date."""
        return self.start_date >= after_date