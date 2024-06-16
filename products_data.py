import requests
import user_data

server_url = user_data.get_server_url()

# Informações sobre os produtos, inicializando vazios
products = [
    {
        'name': '',
        'price': 0,
        'stock': 0
    },
    {
        'name': '',
        'price': 0,
        'stock': 0
    },
    {
        'name': '',
        'price': 0,
        'stock': 0
    }
]

def update_products_data():
    response = requests.get(f"{server_url}/list_products")
    if response.status_code == 200:
        product_list = response.json()
        for i, product in enumerate(product_list):
            if i < len(products):  # Garantir que não vamos tentar acessar um índice fora do range
                products[i]['name'] = product[1]
                products[i]['price'] = product[2]
                products[i]['stock'] = product[3]

# Função para obter o nome do produto
def get_product_name(product_index):
    if 0 <= product_index < len(products):
        return products[product_index]['name']
    return "Produto não encontrado."

# Função para obter o preço do produto
def get_product_price(product_index):
    if 0 <= product_index < len(products):
        return products[product_index]['price']
    return "Produto não encontrado."

# Função para obter o estoque do produto
def get_product_stock(product_index):
    if 0 <= product_index < len(products):
        return products[product_index]['stock']
    return "Produto não encontrado."

# Atualizar informações dos produtos ao iniciar
update_products_data()
