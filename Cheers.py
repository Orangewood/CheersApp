import kivy
from kivy.app import App
from kivy.uix.pagelayout import PageLayout
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.animation import Animation
from kivymd.theming import ThemeManager
from kivymd.uix.dialog import MDDialog

from plyer import gps



#Root widget of application
class MainRoot():
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
    Settings screen for ideas such as changing location status,
    themes, colors, and info about me and the application version.
    """
    pass


class Cheers(App, Screen):
    theme_cls = ThemeManager()
    # theme_cls.primary_palette = "Amber"
    # theme_cls.accent_palette = "Gray"
    title = "Cheers"

    #Kivy App initializing method, gps
    # def on_start(self):
    #     gps.configure(on_location = self.on_gps_location)
    #     gps.start()
    # def on_gps_location(self, **kwargs):
    #     print(kwargs['lat'])



    # def build(self):
    #     return MainRoot()
    pass

#Make this entire section design in Kivy instead, but for now that'll'do laddy
    def aboutPopUp(self):
        about_app = MDDialog(title = "About Cheers!",
                    text = "Created by Orangewood using KivyMD",
                    size_hint = [.5,.5],
                    events_callback = self.close_about_me)
        about_app.open()

    def close_about_me(self, text_of_selection, popup_widget):
        print(text_of_selection)
        print(popup_widget)


CheersApp = Cheers()

if __name__ == '__main__':
    CheersApp.run()
