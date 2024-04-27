from kivy.uix.screenmanager import Screen 
from kivy.lang import Builder

Builder.load_file('settings_screen.kv')

class SettingsScreen(Screen):

    def change_screen(self,screen_name):
        self.manager.current = screen_name

    def toggle_dark_mode(self):
        pass