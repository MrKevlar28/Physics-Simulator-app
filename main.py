from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout

class BoxLayoutExample(BoxLayout):
    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)

    #     self.orientation = "vertical"

    #     b1 = Button(text="Button1")
    #     b2 = Button(text="Button2")
    #     b3 = Button(text="Button3")

    #     self.add_widget(b1)
    #     self.add_widget(b2)
    #     self.add_widget(b3)
    def on_button_click(self):
        print("Button clicked")

class MainWidget(Widget):
    pass

class PhysicsApp(App):
    pass

PhysicsApp().run()
