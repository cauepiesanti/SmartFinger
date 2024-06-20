from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from kivy.lang import Builder
import requests
import user_data

Builder.load_file('create_user_screen.kv')

# Substitua 'your_public_ip_or_domain' pelo seu endereço IP público ou domínio
#SERVER_URL = 'http://192.168.0.23:5000' #'http://192.168.0.34:5000' 

class CreateUserScreen(Screen):

    def returnLogin(self, instance):
        username = self.ids.userName_input.text
        password = self.ids.password_input.text
        
        if not username or not password:
            self.ids.message.text = 'Usuário e senha não podem ser vazios!'
            Clock.schedule_once(lambda dt: self.set_message(''),2)
            return
        
        data = {
            'username': username,
            'password': password,
        }
        
        #response = requests.post(f'{SERVER_URL}/signup', json=data)
        response = requests.post(f'{user_data.get_server_url()}/signup', json=data)
        
        if response.status_code == 201:
            self.ids.message.text = 'Cadastro bem-sucedido!'
            Clock.schedule_once(self.load_login_screen, 1)
            self.ids.userName_input.text = ''
            self.ids.password_input.text = ''
            Clock.schedule_once(lambda dt: self.set_message(''),2)
        elif response.status_code == 409:
            self.set_message('Nome de usuário já existe. Escolha outro nome.')
            Clock.schedule_once(lambda dt: self.set_message(''),2)
        else:
            self.ids.message.text = 'Erro no cadastro!'
            Clock.schedule_once(lambda dt: self.set_message(''),2)

    
    def load_login_screen(self, dt):
        self.manager.current='login'
        self.ids.message.text=''

    def back(self, instance):
        self.manager.current='login'#'signup'
        self.ids.userName_input.text = ''
        self.ids.password_input.text = ''

    def remove_spaces(self, text_input):
        text_input.text = text_input.text.replace(' ', '').replace('\t', '')

    def set_message(self,message):
        self.ids.message.text = message
