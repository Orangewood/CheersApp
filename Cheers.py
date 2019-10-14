import kivy
from kivy.app import App
from kivy.uix.pagelayout import PageLayout
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
#from LoadIcon import *


#Root widget of application
class MainRoot(PageLayout):
    """
    The main root of the application, to contain a loading
    icon on launch, a search class for local pubs or bars,
    a favorite screen class containing the local drink specials
    and events, location content such as direction map,
    telephone, and webiste. Include a setting screen as well.
    """
    pass

class HomeScreen(Screen):
    """
    Testing this to be the main widget, or to be a widget
    that is it's own child class, of the MainRoot class.
    """
    pass

class SettingsScreen(Screen):
    """
    Settings screen for ideas such as changing location radius,
    themes, colors, and info about me and the application version.
    """
    pass


class Cheers(App):


    def build(self):
         return MainRoot()



CheersApp = Cheers()

if __name__ == '__main__':
    CheersApp.run()
