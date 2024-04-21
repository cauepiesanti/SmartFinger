from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

#importing classes

from createUserScreen import CreateUserScreen
from signupScreen import SignupScreen 
from loginScreen import LoginScreen          
from mainMenuScreen import MainMenuScreen  

class MyApp(App):
    def build(self):
        sm =ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(SignupScreen(name='signup'))
        sm.add_widget(CreateUserScreen(name='createUser'))
        sm.add_widget(MainMenuScreen(name='mainMenu'))
        return sm

if __name__ == '__main__':
    MyApp().run()
