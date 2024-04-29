from kivy.app import App 
from kivy.uix.image import Image

#importar imagem do notebook

class MyApp(App):
    def build(self):
        return Image(source='gatito.jpg')
    
if __name__ == '__main__':
    MyApp().run()
