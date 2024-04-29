from kivy.app import App 
from kivy.uix.image import Image, AsyncImage

# importando imagem da web

class MyApp(App):
    def build(self):
        return AsyncImage(source='https://i.pinimg.com/originals/43/41/27/43412706b372f0eacd42d1bf276306d4.jpg')
    
if __name__ == '__main__':
    MyApp().run()
