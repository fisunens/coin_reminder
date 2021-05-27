from kivy.app import App
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget

Config.set("graphics", "resizable", 0)
Config.set("graphics", "width", 512)
Config.set("graphics", "height", 768)


class CoinReminderApp(App):
    def build(self):
        layout = BoxLayout(orientation="vertical", padding=25, spacing=12)
        btn1 = Button(text="Принять")
        btn2 = Button(text="Напомнить")
        coin_name = TextInput(text="Введи название крипты")
        curr_name = TextInput(text="Введи название валюты")

        layout.add_widget(coin_name)
        layout.add_widget(curr_name)
        layout.add_widget(btn1)
        layout.add_widget(Widget())
        layout.add_widget(Widget())
        layout.add_widget(btn2)
        layout.add_widget(Widget())

        return layout


if __name__ == "__main__":
    CoinReminderApp().run()
