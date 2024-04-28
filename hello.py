from kivy.app import App
from kivy.uix.button import Button

#primeiro teste

class MyApp(App):
    def build(self):
        return Button(text="Hello World")
    
if __name__ == '__main__':
    MyApp().run()
