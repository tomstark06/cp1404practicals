"""Band class definition."""

class Band:
    """Represent a Band object."""

    def __init__(self, name=""):
        """Initialise a Band."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a formatted string of a Band instance."""
        return f"{self.name} ({",".join([str(musician) for musician in self.musicians])})"

    def add(self, musician):
        """Add a member to the band."""
        self.musicians.append(musician)

    def play(self):
        """Print the result of the band playing."""
        return "\n".join([musician.play() for musician in self.musicians])