from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

#importing classes

from createUserScreen import CreateUserScreen
from signupScreen import SignupScreen 
from loginScreen import LoginScreen          
from mainMenuScreen import MainMenuScreen  
from settingsScreen import SettingsScreen
from helpScreen import HelpScreen
from depositScreen import DepositScreen
from profileScreen import ProfileScreen

class MyApp(App):
    def build(self):
        sm =ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(SignupScreen(name='signup'))
        sm.add_widget(CreateUserScreen(name='createUser'))
        sm.add_widget(MainMenuScreen(name='mainMenu'))
        sm.add_widget(SettingsScreen(name='settings'))
        sm.add_widget(HelpScreen(name='help'))
        sm.add_widget(DepositScreen(name='deposit'))
        sm.add_widget(ProfileScreen(name='profile'))
        #testando
        #sm.add_widget(LoginScreen(name='shopping_cart'))
        #sm.add_widget(LoginScreen(name='historic'))
        #sm.add_widget(LoginScreen(name='help'))
        #sm.add_widget(LoginScreen(name='profile'))
        #sm.add_widget(LoginScreen(name='deposit'))
        #sm.add_widget(LoginScreen(name='peak_times'))
        #sm.add_widget(LoginScreen(name='language'))
        
        return sm

if __name__ == '__main__':
    MyApp().run()
