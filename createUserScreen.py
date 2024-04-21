from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from kivy.lang import Builder

Builder.load_file('create_user_screen.kv')

class CreateUserScreen(Screen):

    def returnLogin(self,instance):
        self.ids.message.text = 'returning to login...'
        Clock.schedule_once(self.load_signup_screen,1)
    
    def load_signup_screen(self,dt):
        self.manager.current='login'
        self.ids.message.text=''

    def back(self,instance):
        self.manager.current='signup'
