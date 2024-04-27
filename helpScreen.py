from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

Builder.load_file('help_screen.kv')

class HelpScreen(Screen):
    def back(self,screen_name):
        self.manager.current = screen_name
    
