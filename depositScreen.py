from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from kivy.lang import Builder
import user_data
import requests

Builder.load_file('deposit_screen.kv')

class DepositScreen(Screen):

    def on_enter(self):
        self.update_balance_display()

    def update_balance_display(self):
        current_balance = user_data.get_current_user_balance()
        self.ids.balance.text = f'Saldo: ${current_balance:.2f}'

    def update_future_balance(self, instance, value):
        try:
            deposit_amount = (value.replace(',', '.'))
            if (deposit_amount == ''):
                deposit_amount = float(0)
            else:
                deposit_amount = float(deposit_amount)
            future_balance = user_data.get_current_user_balance() + deposit_amount
            self.ids.future_balance.text = f'Saldo futuro: ${future_balance:.2f}'
        except ValueError:
            pass

    def print_message_change_screen(self, instance):
        deposit_input = self.ids.deposit_input.text.strip()
        
        if deposit_input:
            deposit_input = deposit_input.replace(',', '.')
            
            try:
                deposit_amount = float(deposit_input)
                
                if 0.01 <= deposit_amount <= 1000.00:
                    new_balance = user_data.get_current_user_balance() + deposit_amount
                    user_data.update_current_user_balance(new_balance)

                    self.update_balance_db(user_data.get_current_user(), new_balance)
                    
                    main_menu_screen = self.manager.get_screen('mainMenu')
                    main_menu_screen.update_balance(new_balance)
                    
                    future_balance = new_balance + float(deposit_input)
                    self.ids.balance.text = f'Saldo: ${new_balance:.2f}'
                    self.ids.future_balance.text = f'Saldo futuro: ${future_balance:.2f}'
                    self.ids.message_label.text = 'Depósito bem-sucedido!'
                    
                    Clock.schedule_once(lambda dt: self.load_screen(), 1)

                else:
                    self.ids.message_label.text = 'Valor de depósito deve estar entre $0.01 e $1000.00'
                    Clock.schedule_once(lambda dt: self.set_message(''),2)
            except ValueError:
                self.ids.message_label.text = 'Valor de depósito inválido'
                Clock.schedule_once(lambda dt: self.set_message(''),2)
        else:
            self.set_message('Por favor, insira um valor de depósito válido')
            Clock.schedule_once(lambda dt: self.set_message(''),2)
        
        self.ids.deposit_input.text = ''
        self.ids.future_balance.text = f'Saldo futuro: ${user_data.get_current_user_balance():.2f}'

    def load_screen(self):
        self.manager.current = 'mainMenu'
        self.ids.message_label.text = ''
        self.ids.deposit_input.text = ''

    def update_balance_db(self, username, new_balance):
        try:
            print(f"Atualizando saldo para usuário: {username} com novo saldo: {new_balance}")
            #response = requests.post('http://192.168.0.23:5000/update_balance', json={'username': username, 'new_balance': new_balance})
            response = requests.post(f'{user_data.get_server_url()}/update_balance', json={'username': username, 'new_balance': new_balance})
            if response.status_code == 200:
                print('Saldo atualizado no banco de dados com sucesso.')
            else:
                print(f'Erro ao atualizar saldo no banco de dados. Status code: {response.status_code}')
        except Exception as e:
            print(f'Erro ao conectar ao servidor: {e}')
    
    def set_message(self,message):
        self.ids.message_label.text = message
