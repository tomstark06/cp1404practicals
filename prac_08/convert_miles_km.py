from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM_CONVERSION_RATE = 1.609344


class ConvertMilesKmApp(App):
    """Kivy App for converting miles to kilometres."""
    miles_input = StringProperty()
    kilometres_output = StringProperty()

    def build(self):
        """Build Kivy app."""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file("convert_miles_km.kv")
        return self.root

    def handle_convert(self):
        """Convert the inputted miles value to kilometres."""
        try:
            kilometres = float(self.root.ids.miles_input.text) * MILES_TO_KM_CONVERSION_RATE
        except ValueError:
            kilometres = 0.0
        self.kilometres_output = str(kilometres)

    def handle_increment(self, increment):
        """Increment the input value by a given increment."""
        if self.root.ids.miles_input.text == "":
            number = 0 + increment
        else:
            number = int(self.root.ids.miles_input.text) + increment
        self.miles_input = str(number)


ConvertMilesKm().run()
