from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

Builder.load_file('main_menu_screen.kv')

class MainMenuScreen(Screen):       
    
    def change_screen(self,screen_name):
        self.manager.current = screen_name
    