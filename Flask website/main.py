from website import create_app
import kivy
from kivy.app import App
from kivy.uix.label import Label


class MobileApp(App):
    def build(self):
        return Label(text="Hello World!")
if __name__ == "__MobileApp__":
    MobileApp().run()

class WebsiteApp(App):
    app = create_app()
if __name__ == '__WebsiteApp__':
    app.run(debug=True)
