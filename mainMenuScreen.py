from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label

#constantes

BOTTOM_ICON_SIZE = 100
BOTTOM_LAYOUT_WIDTH = 1000
BOTTOM_LAYOUT_HEIGHT = 100
TOP_ICON_SIZE = 50
TOP_LAYOUT_WIDTH = 500
TOP_LAYOUT_HEIGHT = 100
PRODUCT_ICON_SIZE = 250

#testando o menu principal

class MainMenuScreen(Screen):
    def __init__(self, **kwargs):
        super(MainMenuScreen, self).__init__(**kwargs)

        # Layout principal
        main_layout = FloatLayout()

        # Adicionar produtos como botões grandes
        for i in range(3):  # Supondo 3 produtos, você pode ajustar conforme necessário
            product_button = Button(text=f'Produto {i+1}\nEstoque: 10\nPreço: $10', size_hint=(None, None), size=(PRODUCT_ICON_SIZE, PRODUCT_ICON_SIZE))
            main_layout.add_widget(product_button)

        # Layout para os ícones na parte inferior
        bottom_layout = BoxLayout(orientation='horizontal', spacing=0, size_hint=(None, None), size=(BOTTOM_LAYOUT_WIDTH, BOTTOM_LAYOUT_HEIGHT))
        
        # Adicionar ícones para outras telas
        icons = ['images/perfil.png', 'depositar_fundos.png','buscar_produto.png','horarios_de_pico.png', 'historico_transacoes.png']
        for icon in icons:
            icon_button = Button(background_normal=icon, size_hint=(None, None), size=(BOTTOM_ICON_SIZE,BOTTOM_ICON_SIZE))
            bottom_layout.add_widget(icon_button)
        
        # Ajustando o offset entre os botões
        n_icons = len(icons)
        offset = (BOTTOM_LAYOUT_WIDTH-(BOTTOM_ICON_SIZE*n_icons))/(n_icons-1)
        bottom_layout.spacing = (offset)
        
        # Layout para os ícones no canto superior direito
        top_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint=(None, None), size=(TOP_LAYOUT_WIDTH, TOP_LAYOUT_HEIGHT))

        # Adicionar ícone de ajuda
        help_icon = Button(background_normal='images/ajuda.png', size_hint=(None, None), size=(TOP_ICON_SIZE, TOP_ICON_SIZE))
        top_layout.add_widget(help_icon)

        # Adicionar ícone de saldo
        balance_icon = Label(text='Saldo: $100', size_hint=(None, None), size=(TOP_ICON_SIZE, TOP_ICON_SIZE))
        top_layout.add_widget(balance_icon)

        # Adicionar todos os layouts à tela principal
        main_layout.add_widget(bottom_layout)
        main_layout.add_widget(top_layout)

        # Ajusta a posição dos layouts no layout pai

        bottom_layout.pos_hint = {'center_x':0.5,'y':0}

        self.add_widget(main_layout)
