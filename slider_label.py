from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.slider import Slider

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical',padding=20)

        slider = slider(min=0,max=100,value=50,stop=1)
        slider.bind(value=self.atualizar_label)

        self.label = Label(tex='Valor do Slider: {}'.format(int(slider.value)))

        layout.add_widget(slider)
        layout.add_widget(self.label)

        return layout
    
    def atualizar_label(self,instance,valor):
        self.label.text ="Valor do slider: {}".format(int(valor))

if __name__ == "__main__":
    MyApp().run()
