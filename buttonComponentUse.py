from kivy.app import App
from kivy.uix.button import Button


class MainApp(App):
    def build(self):
        return Button()

    def on_press_button(self, instance):
        print("Você apertou o botão!")


if __name__ == "__main__":
    app = MainApp()
    app.run()
