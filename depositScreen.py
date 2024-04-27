from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.clock import Clock

Builder.load_file('deposit_screen.kv')

class DepositScreen(Screen):
    
    def print_message_change_screen(self,instance):
        #Lógica de permissão de depósito (valor mínimo, máximo, somente números,etc)
        self.ids.message_label.text = 'Deposit successful!'
        Clock.schedule_once(self.load_screen,1)

    def load_screen(self,dt):
        self.manager.current = 'mainMenu'
        self.ids.message_label.text = ''