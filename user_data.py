import requests

current_user = None
current_user_balance = 0.0
server_url = 'http://192.168.0.23:5000'

def update_current_user(new_user):
    global current_user
    current_user = new_user

def update_current_user_balance(new_balance):
    global current_user_balance
    current_user_balance = new_balance

def get_current_user():
    return current_user

def get_current_user_balance():
    return current_user_balance

def get_server_url():
    return server_url

def update_user_balance_from_db():
    # chamar o endpoint
    username = get_current_user()
        
    # Enviar solicitação para autenticação no servidor
    data = {
        'username': username,
    }        
    # Obter o saldo do usuário e atualizar o user_data
    balance_response = requests.post(f'{server_url}/get_balance', json=data)
    if balance_response.status_code == 200:
        balance_data = balance_response.json()
        update_current_user_balance(balance_data['balance'])

