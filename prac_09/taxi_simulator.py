"""Taxi simulator program."""

from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """"""
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    total_trip_cost = 0.0
    current_taxi = None
    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            current_taxi = choose_taxi(current_taxi, taxis)
        elif choice == "d":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                total_trip_cost = drive_taxi(current_taxi, total_trip_cost)
        else:
            print("Invalid option")
        print(f"Bill to date: ${total_trip_cost:.2f}")
        print(MENU)
        choice = input(">>> ").lower()
    print(f"Total trip cost: ${total_trip_cost:.2f}")
    display_taxis(taxis, "Taxis are now:")


def display_taxis(taxis, title):
    print(title)
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def choose_taxi(current_taxi, taxis):
    display_taxis(taxis, "Taxis available:")
    try:
        taxi_choice = int(input("Choose taxi: "))
        current_taxi = taxis[taxi_choice]
    except (ValueError, IndexError):
        print("Invalid taxi choice")
    return current_taxi


def drive_taxi(current_taxi, total_trip_cost):
    current_taxi.start_fare()
    distance = int(input("Drive how far? "))
    current_taxi.drive(distance)
    fare = current_taxi.get_fare()
    total_trip_cost += fare
    print(f"Your {current_taxi.name} trip cost you ${fare:.2f}")
    return total_trip_cost


main()
