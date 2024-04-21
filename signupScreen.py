from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

Builder.load_file('signup_screen.kv')

class SignupScreen(Screen):
    
    def back(self,instance):
        self.manager.current = 'login'

    def createUser(self,instance):
        self.manager.current = 'createUser'