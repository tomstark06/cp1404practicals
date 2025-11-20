"""Taxi class test code."""

from prac_09.taxi import Taxi


def run_tests():
    """Run tests on taxi class."""
    my_taxi = Taxi("Prius 1", 100)
    my_taxi.drive(40)
    print(f"Fare 1:\n{my_taxi}, Current fare: ${my_taxi.get_fare()}")
    my_taxi.start_fare()
    my_taxi.drive(100)
    print(f"\nFare 2:\n{my_taxi}, Current fare: ${my_taxi.get_fare()}")


run_tests()
