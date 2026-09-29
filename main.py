from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class StoR(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 20
        self.add_widget(Label(text='Sto-R SUPER GUCLU', font_size=32, bold=True))
        self.add_widget(Label(text='Build basarili! APK calisiyor.', font_size=18))
        btn = Button(text='KRAL BUTON', font_size=24, size_hint=(1, 0.3))
        btn.bind(on_press=lambda x: print("KRAL TIKLADI"))
        self.add_widget(btn)

class StoRApp(App):
    def build(self):
        return StoR()

StoRApp().run()
