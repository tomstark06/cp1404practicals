"""Programming language exercise - ProgrammingLanguage class definition."""


class ProgrammingLanguage:
    """Represent a ProgrammingLanguage object."""

    def __init__(self, name="", typing="", is_reflective=False, year=0):
        """Initialise a ProgrammingLanguage instance."""
        self.name= name
        self.typing = typing
        self.is_reflective = is_reflective
        self.year = year

    def __str__(self):
        """Return a formatted string of the ProgrammingLanguage object."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.is_reflective}, First appeared in {self.year}"

    def is_dynamic(self):
        """Return a boolean if the ProgrammingLanguage is dynamic or not."""
        return self.typing == "Dynamic"
