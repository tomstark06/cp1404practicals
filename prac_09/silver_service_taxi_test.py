"""Test SilverServiceTaxi class."""

from prac_09.silver_service_taxi import SilverServiceTaxi


def run_tests():
    """Run tests on the SilverServiceTaxi class."""
    silver_service_taxi = SilverServiceTaxi("Hummer", 200, 2)
    silver_service_taxi.drive(18)
    print(silver_service_taxi)
    print(f"Total Fare: ${silver_service_taxi.get_fare()}")
    assert silver_service_taxi.get_fare() == 48.78


run_tests()
