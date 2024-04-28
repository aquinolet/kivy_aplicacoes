from kivy.app import App 
from kivy.uix.button import Button

#função de retornar resposta quando o botãa for clicado

def botao_pressionado(instance):
    print("Botão pressionado!")

class MyApp(App):
    def build(self):
        botao = Button(text='Clique Aqui')
        botao.bind(on_press=botao_pressionado)
        return botao
    
if __name__ == '__main__':
    MyApp().run()
