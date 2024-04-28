from kivy.app import App 
from kivy.uix.label import Label
from kivy.utils import get_color_from_hex

#códigos de label

class MyApp(App):
    def build(self):
        return Label(text="Hello World",
                      font_size=70, #tamanho do texto
                      font_name='Arial', #fonte do texto
                      color=get_color_from_hex('#ED2728'), #cor do texto
                      halign='left', valign='top', #alinhamento na horizontal e vertical
                      size_hint=(None,None), #Desativa o ajuste automático do tamanho
                      size=(380,680), #Define o tamanho do rótulon
                      text_size=(300,400)) #Define a largura máxima do texto
if __name__ == '__main__':
    MyApp().run()
