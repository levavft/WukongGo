from kivy.uix.screenmanager import Screen
from kivy.lang import Builder


class MenuScreen(Screen):

    def __init__(self, **kwargs):
        Builder.load_file("kv/Menu.kv")
        super(MenuScreen, self).__init__(name=kwargs['name'])
