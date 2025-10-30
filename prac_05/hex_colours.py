"""Hex colours exercise."""

COLOUR_NAME_TO_HEX = {"army green": "#4b5320", "brown3": "#cd3333", "brunswick green": "#1b4d3e", "crystal": "#a7d8de",
                      "deep cerise": "#da3287", "deep champagne": "#fad6a5", "blue": "#0000ff",
                      "deep saffron": "#ff9933", "rebeccapurple": "#663399", "twilight lavender": "#8a496b"}

colour_name = input("Colour name: ").lower()
while colour_name != "":
    try:
        print(f"The hex code for {colour_name.capitalize()} is {COLOUR_NAME_TO_HEX[colour_name]}.")
    except KeyError:
        print("Invalid colour name.")
    colour_name = input("Colour name: ").lower()
