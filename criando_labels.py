from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

#criar 3 labels (Negrito, italico e sublinhado)

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.lab1 = Label(
            text="SENAI", color=[1,0,0,1], #cor vermelho
            font_size =40, bold=True #bold - colocar em destaque
        )
        self.lab2 = Label(
            text="SESI", color=[0,1,0,1], #cor verde
            font_size=40, italic=True #italic - itálico
        )
        self.lab3 = Label(
            text="ENEM", color=[0,0,1,1], #cor azul
            font_size=40, font_name='Arial', 
            underline=True #underline - colocar texto sublinhado
        )

        layout.add_widget(self.lab1)
        layout.add_widget(self.lab2)
        layout.add_widget(self.lab3)
        return layout
    
if __name__ =='__main__':
    MyApp().run()
