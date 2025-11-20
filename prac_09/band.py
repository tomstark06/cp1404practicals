"""Band class definition."""

class Band:
    """Represent a Band object."""

    def __init__(self, name=""):
        """Initialise a Band."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a formatted string of a Band instance."""
        return f"{self.name} ({self.musicians})"  # Could not figure out how to remove the list brackets

    def add(self, musician):
        """Add a member to the band."""
        self.musicians.append(musician)

    def play(self):
        """Print the result of the band playing."""
        for musician in self.musicians:
            print(musician.play())
        return ""  # Not sure if this solution is correct or not