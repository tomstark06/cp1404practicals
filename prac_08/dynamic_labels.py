from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):

    def __init__(self):
        super().__init__()
        self.names = ["Tom", "Lindsay", "Jessica", "Steph", "Lebron", "Micheal"]

    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file("dynamic_labels.kv")
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for name in self.names:
            name_label = Label(text=name)
            self.root.ids.main.add_widget(name_label)


DynamicLabelsApp().run()
