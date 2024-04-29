from kivy.app import App 
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        layout_float = FloatLayout()

        b1 = Button(text='Botão 1', size_hint=(None,None), size=(100,50), pos_hint={'x':0.1,'y':0.8})
        b2 = Button(text='Botão 2', size_hint=(None,None), size=(100,50), pos_hint={'center_x':0.5,'center_y':0.5})
        b3 = Button(text='Botão 3', size_hint=(None,None), size=(100,50), pos_hint={'right':0.9,'y':0.1})

        layout_float.add_widget(b1)
        layout_float.add_widget(b2)
        layout_float.add_widget(b3)

        return layout_float
    

if __name__ =='__main__':
    MyApp().run()
