from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivymd.uix.button import MDFloatingActionButton

KV = """
MDBoxLayout:
    orientation: "vertical"

    MDTopAppBar:
        title: "Top Toolbar Item"
        left_action_items: [["menu"]]
        right_action_items: [["plus"]]

    MDLabel:
        id: my_label
        text: "some stuffs in here"
        halign: "center"

    MDBottomAppBar:
        MDTopAppBar:
            icon: "check"
            type: "bottom"
            mode: "end"
            on_action_button: app.bbtn_press()
"""

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'DeepPurple'
        return Builder.load_string(KV)

    def bbtn_press(self):
        self.root.ids.my_label.text = "Text changed"

if __name__ == '__main__':
    MainApp().run()