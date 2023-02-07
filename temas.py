from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivymd.uix.button import MDFloatingActionButton

KV = """
Screen:
    MDRaisedButton:
        text:'First Button'
        pos_hint: {"center_x": .5, "center_y": .8}
        md_bg_color: app.theme_cls.primary_light
    MDRaisedButton:
        text:'Second Button'
        pos_hint: {"center_x": .5, "center_y": .5}
    MDRaisedButton:
        text:'Third Button'
        pos_hint: {"center_x": .5, "center_y": .3}
        md_bg_color: app.theme_cls.primary_dark
    MDFloatingActionButton:
        icon: 'plus'
        pos_hint: {"center_x": .9, "center_y": .1}
        type: 'small'
        md_bg_color: "#f8d7e3"
        icon_color: "#6851a5"
"""

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'DeepPurple'
        return Builder.load_string(KV)

if __name__ == '__main__':
    MainApp().run()