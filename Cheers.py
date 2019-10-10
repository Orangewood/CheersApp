import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.pagelayout import PageLayout
from kivy.uix.progressbar import ProgressBar
from kivy.properties import ObjectProperty
from kivy.core.text import Label as CoreLabel
from kivy.lang.builder import Builder
from kivy.graphics import Color, Ellipse, Rectangle
from kivy.clock import Clock
import LoadIcon


#Root widget of application
class MainRoot(PageLayout):
    pass

#App class
class Cheers(App):

    def build(self):
         return MainRoot()



CheersApp = Cheers()

if __name__ == '__main__':
    CheersApp.run()
