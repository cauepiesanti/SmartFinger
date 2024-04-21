from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from kivy.lang import Builder

#testar comentado para ver se o padrão de nome está correto
Builder.load_file('login_screen.kv')

class LoginScreen(Screen):

    def signin(self,instance):
        self.manager.current = 'signup'

    def login(self,instance): #autenticação
        username = self.ids.username_input.text
        password = self.ids.password_input.text
        # Somente para teste
        self.ids.message_label.text = 'Login successful!'
        Clock.schedule_once(self.load_main_menu,1)
        # Fazer lógica de autenticação
        '''if username == 'user' and password == 'password':
            self.ids.message_label.text = 'Login successful!'
            Clock.schedule_once(self.load_main_menu,1)
        else:
            self.ids.message_label.text = 'Login failed!'
        '''
    def load_main_menu(self,dt):
        self.manager.current = 'mainMenu' # - vai para o menu principal
        self.ids.message_label.text=''