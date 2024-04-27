from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.clock import Clock

Builder.load_file('profile_screen.kv')

class ProfileScreen(Screen):
    
    def save_return_mainMenu(self,instance):
        self.ids.message_label.text='Changes confirmed!'
        Clock.schedule_once(self.return_mainMenu,1)
        
    def return_mainMenu(self,dt):
        self.manager.current = 'mainMenu'
        self.ids.message_label.text=' '