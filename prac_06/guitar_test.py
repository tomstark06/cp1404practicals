"""Guitar testing file."""

from prac_06.guitar import Guitar

gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
cool_guitar = Guitar("Mega Shredder", 2013, 40000.24)
print(f"{gibson.name} get_age() - Expected 103. Got {gibson.get_age()}")
print(f"{cool_guitar.name} get_age() - Expected 12. Got {cool_guitar.get_age()}")
print(f"{gibson.name} is_vintage() - Expected True. Got {gibson.is_vintage()}")
print(f"{cool_guitar.name} is_vintage() - Expected False. Got {cool_guitar.is_vintage()}")
