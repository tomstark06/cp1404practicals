from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM_CONVERSION_RATE = 1.609344


class ConvertMilesKm(App):
    number_input = StringProperty()
    number_output = StringProperty()

    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file("convert_miles_km.kv")
        return self.root

    def handle_convert(self):
        try:
            kilometres = float(self.root.ids.user_input.text) * MILES_TO_KM_CONVERSION_RATE
        except ValueError:
            kilometres = 0.0
        self.number_output = str(kilometres)

    def handle_increment(self, value):
        if self.root.ids.user_input.text == "":
            number = 0 + value
        else:
            number = int(self.root.ids.user_input.text) + value
        self.number_input = str(number)


ConvertMilesKm().run()
