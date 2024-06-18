from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget

class BoxLayoutExample(BoxLayout):
    def __init__(self, screen_manager, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.screen_manager = screen_manager
        self.initialize_buttons()

    def initialize_buttons(self):
        self.clear_widgets()

        # Add a spacer widget at the top to push buttons to the center vertically
        self.add_widget(Widget(size_hint_y=None, height=0.5*self.height))

        button_width = 300  # Adjust the width as needed
        b1 = Button(text="Create Graphs")
        b2 = Button(text="Simulator with Graphs")
        b3 = Button(text="Simulator without Graphs")
        b1.bind(on_press=self.on_button1_press)
        b2.bind(on_press=self.on_button2_press)
        b3.bind(on_press=self.on_button3_press)
        self.add_widget(b1)
        
        # Add a spacer widget between buttons to increase the spacing
        self.add_widget(Widget(size_hint_y=None, height=50))
        self.add_widget(b2)
        
        # Add another spacer widget between buttons
        self.add_widget(Widget(size_hint_y=None, height=50))
        self.add_widget(b3)

        # Add a spacer widget at the bottom to push buttons to the center vertically
        self.add_widget(Widget(size_hint_y=None, height=0.5*self.height))

    def on_button1_press(self, instance):
        print("Button1 pressed")

    def on_button2_press(self, instance):
        self.create_initial_buttons()

    def on_button3_press(self, instance):
        print("Button3 pressed")

    def create_initial_buttons(self):
        self.clear_widgets()
        button_texts = [
            "Single Object Simulation",
            "Multiple Objects Simulation with Camera",
            "Interactive/Drawable Polygon Simulation",
            "Outwoods Simulation",
            "Pendulum Simulation",
            "Planetary Motion Simulation"
        ]
        button_callbacks = [
            self.onButton1_press,
            self.onButton2_press,
            self.onButton3_press,
            self.onButton4_press,
            self.onButton5_press,
            self.onButton6_press
        ]

class FirstScreen(Screen):
    def __init__(self, screen_manager, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayoutExample(screen_manager)
        float_layout = FloatLayout()
        with float_layout.canvas:
            self.bg_image = Image(source='Main Files\physics_background.jpg', allow_stretch=True, keep_ratio=False)
        self.layout.bind(size=self.update_bg_image_size, pos=self.update_bg_image_pos)
        float_layout.add_widget(self.bg_image)
        float_layout.add_widget(self.layout)
        self.add_widget(float_layout)

    def update_bg_image_size(self, instance, value):
        self.bg_image.size = instance.size

    def update_bg_image_pos(self, instance, value):
        self.bg_image.pos = instance.pos

class SecondScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        label = Label(text="This is the second screen")
        layout.add_widget(label)
        self.add_widget(layout)

class PhysicsApp(App):
    def build(self):
        screen_manager = ScreenManager()

        first_screen = FirstScreen(screen_manager, name='first')
        screen_manager.add_widget(first_screen)

        second_screen = SecondScreen(name='second')
        screen_manager.add_widget(second_screen)

        return screen_manager

if __name__ == "__main__":
    PhysicsApp().run()
