"""Tests for UnreliableCar class."""

from prac_09.unreliable_car import UnreliableCar


def run_tests():
    """Run tests on UnreliableCar class."""
    reliable_car = UnreliableCar("McQueen", 200, 72.54)
    unreliable_car = UnreliableCar("Mater", 200, 34.82)
    print(f"Reliable Car Drive Count: {test_car(reliable_car)}. Should be approximately {reliable_car.reliability}")
    print(f"Reliable Car Drive Count: {test_car(unreliable_car)}. Should be approximately {unreliable_car.reliability}")


def test_car(car):
    drive_count = 0
    for i in range(100):
        distance = car.drive(10)
        if distance != 0:
            drive_count += 1
        car.fuel = 200
    return drive_count


run_tests()
