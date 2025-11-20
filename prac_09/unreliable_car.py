"""Unreliable Car subclass."""

from prac_09.car import Car
import random


class UnreliableCar(Car):
    """Specialised version of a Car that includes a reliability value."""

    def __init__(self, name, fuel, reliability=0.0):
        """Initialise an UnreliableCar instance."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car a given distance only if the reliability is high enough (randomly decided)."""
        if random.uniform(0, 100) < self.reliability:
            return super().drive(distance)
        else:
            return 0