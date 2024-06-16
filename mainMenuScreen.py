from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.clock import Clock
import user_data
import products_data

Builder.load_file('main_menu_screen.kv')

class MainMenuScreen(Screen):   

    def on_enter(self):
        self.init_balance()
        self.init_table()
        Clock.schedule_interval(self.update_table,5)   

    def init_table(self):
        self.ids.nome_produto_1.text = products_data.get_product_name(0)
        self.ids.nome_produto_2.text = products_data.get_product_name(1)
        self.ids.nome_produto_3.text = products_data.get_product_name(2)

        self.ids.preco_produto_1.text = str(products_data.get_product_price(0))
        self.ids.preco_produto_2.text = str(products_data.get_product_price(1))
        self.ids.preco_produto_3.text = str(products_data.get_product_price(2))

        self.ids.estoque_produto_1.text = str(products_data.get_product_stock(0))
        self.ids.estoque_produto_2.text = str(products_data.get_product_stock(1))
        self.ids.estoque_produto_3.text = str(products_data.get_product_stock(2))

    def update_table(self,dt):
        products_data.update_products_data()
        #Inicia novamente a tabela com os valores atualizados
        self.init_table()

    def change_screen(self, screen_name):
        self.manager.current = screen_name
    
    def increment_qtd(self, produto_id):
        quantidade_id = f'qtd_produto_{produto_id}'
        quantidade_input = self.ids[quantidade_id]
        quantidade = int(quantidade_input.text) + 1
        quantidade_input.text = str(quantidade)

    def decrement_qtd(self, produto_id):
        quantidade_id = f'qtd_produto_{produto_id}'
        quantidade_input = self.ids[quantidade_id]
        quantidade = int(quantidade_input.text)
        if quantidade > 0:
            quantidade -= 1
        quantidade_input.text = str(quantidade)

    def reset_text(self, dt):
        self.manager.current = 'shopping_cart' #'login'
        self.ids.add_to_cart_button.text = "Adicionar ao carrinho"

    def change_text(self):
        self.ids.add_to_cart_button.text = "Itens adicionados ao carrinho!"
        Clock.schedule_once(self.reset_text, 2)

    def update_balance(self, new_balance):
        self.ids.balance_button.text = f'Saldo: ${new_balance:.2f}'

    def init_balance(self):
        balance = user_data.get_current_user_balance()
        self.ids.balance_button.text = f'Saldo: ${balance:.2f}'
