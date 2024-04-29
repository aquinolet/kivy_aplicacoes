from kivy.app import App 
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=10)

        botao1 = Button(text='Botão 1', background_color=(0.2,0.7,0.3,1), font_size=20)
        layout.add_widget(botao1)
        botao2 = Button(text='Clique aqui!', haling='center')
        layout.add_widget(botao2)
        botao3 = Button(text='Clique para continuar', bavkground_color=(0.9,0.5,0.1,1), font_size=30)
        layout.add_widget(botao3)

        def acao_botao(instance):
            instance.text = 'Botão Pressionado!'
        
        botao4 = Button(text='Botão 4')
        botao4.bind(on_press=acao_botao)
        layout.add_widget(botao4)

        info_label = Label(text='Pressione os botões para ver diferentes propriedades em ação.')
        layout.add_widget(info_label)

        return layout
    
if __name__=='__main__':
    MyApp().run()
