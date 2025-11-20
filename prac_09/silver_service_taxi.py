"""Silver service taxi class."""

from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi that includes fanciness."""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness=1.0):
        """Initialise a SilverServiceTaxi instance, based on a parent class Taxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """Return a string like a Taxi but with the additional flagfall."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall}"

    def get_fare(self):
        """Return the price for the taxi trip plus flagfall."""
        return self.flagfall + super().get_fare()
