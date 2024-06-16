from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from kivy.lang import Builder
import requests
import user_data

Builder.load_file('login_screen.kv')


# Substitua 'your_public_ip_or_domain' pelo seu endereço IP público ou domínio
#SERVER_URL = 'http://192.168.0.23:5000' #'http://192.168.0.34:5000' 

class LoginScreen(Screen):

    def signup(self, instance):
        self.manager.current = 'createUser'

    def login(self, instance):
        username = self.ids.username_input.text
        password = self.ids.password_input.text
        
        # Enviar solicitação para autenticação no servidor
        data = {
            'username': username,
            'password': password,
        }
        #response = requests.post(f'{SERVER_URL}/login', json=data)
        response = requests.post(f'{user_data.get_server_url()}/login', json=data)
        
        # Verificar se a resposta foi bem-sucedida e atualizar interface
        if response.status_code == 200:
            user_data.update_current_user(username)
            # Obter o saldo do usuário e atualizar o user_data
            balance_response = requests.post(f'{user_data.get_server_url()}/get_balance', json=data)
            if balance_response.status_code == 200:
                balance_data = balance_response.json()
                user_data.update_current_user_balance(balance_data['balance'])

            self.ids.message_label.text = 'Login bem-sucedido!'
            Clock.schedule_once(self.load_main_menu, 1)
        else:
            self.ids.message_label.text = 'Login falhou! Usuário ou senha inválidos.'
        
    def load_main_menu(self, dt):
        self.manager.current = 'mainMenu'
        self.ids.message_label.text = ''
        print(f"\n{user_data.get_current_user()}\n")

    def remove_spaces(self, text_input):
        text_input.text = text_input.text.replace(' ', '').replace('\t', '')
