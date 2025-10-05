"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
    A value error will occur when an unexpected value is inputted by the user (for
    example when the input is expecting an integer but the user inputs a string).
2. When will a ZeroDivisionError occur?
    The ZeroDivisionError occurs when the denominator of the fraction is a zero.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
    Yes, you can add a while loop to check if the number zero was inputted (see below).
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Cannot divide by zero!")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
# except ZeroDivisionError:
#     print("Cannot divide by zero!")
print("Finished.")
