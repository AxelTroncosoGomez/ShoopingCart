from kivy.app import App
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.textfield import MDTextField
from kivy.clock import Clock
from kivy.properties import BooleanProperty
from kivy.metrics import dp
from functools import partial

# Recreamos la Class MDTextField para que se oculte la password de manera dinamica
class MyMDTextField(MDTextField):
    password_mode = BooleanProperty(True)

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            if self.icon_right:
                # icon position based on the KV code for MDTextField
                icon_x = (self.width + self.x) - (self._icon_right_label.texture_size[1]) - dp(8)
                icon_y = self.center[1] - self._icon_right_label.texture_size[1] / 2
                if self.mode == "round":
                    icon_y -= dp(4)
                elif self.mode != 'fill':
                    icon_y += dp(8)

                # not a complete bounding box test, but should be sufficient
                if touch.pos[0] > icon_x and touch.pos[1] > icon_y:
                    if self.password_mode:
                        self.icon_right = 'eye'
                        self.password_mode = False
                        self.password = self.password_mode
                    else:
                        self.icon_right = 'eye-off'
                        self.password_mode = True
                        self.password = self.password_mode

                    # try to adjust cursor position
                    cursor = self.cursor
                    self.cursor = (0,0)
                    Clock.schedule_once(partial(self.set_cursor, cursor))
        return super(MyMDTextField, self).on_touch_down(touch)

    def set_cursor(self, pos, dt):
        self.cursor = pos

KV = """
Screen:
    MDCard:
        size_hint: None, None
        size: 400, 500
        pos_hint: {"center_x": .5, "center_y": .5}
        elevation: 5
        padding: 25
        spacing: 25
        orientation: 'vertical'

        MDLabel:
            id: welcome_label
            text: "Bienvenido"
            font_size: 40
            halign: "center"
            size_hint_y: None
            height: self.texture_size[1]
            padding_y: 15

        MDTextField:
            id: user
            hint_text: "username"
            icon_right: "account"
            size_hint_x: None
            width: 250
            font_size: 18
            pos_hint: {"center_x": .5}
            mode: "round"

        MyMDTextField:
            id: passwordzs
            hint_text: "password"
            icon_right: "eye-off"
            size_hint_x: None
            width: 250
            font_size: 18
            pos_hint: {"center_x": .5}
            mode: "round"
            password: True


        MDRoundFlatButton:
            text: "LOG IN"
            font_size: 12
            pos_hint: {"center_x": .5}
            on_press: app.logger()

        MDRoundFlatButton:
            text: "Register here"
            font_size: 12
            pos_hint: {"center_x": .5}
            on_press: app.register()

        Widget:
            size_hint_y: None
            height: 25
"""

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'DeepPurple'
        return Builder.load_string(KV)

    def logger(self):
        if self.root.ids.user.text == "":
            self.root.ids.welcome_label.text = "Me Apretaste"
        else:
            self.root.ids.welcome_label.text = f"Bienvenido {self.root.ids.user.text}"

    def register(self):
        self.root.ids.welcome_label.text = "Not Implemented"

    def eyes_on(self):
        pass

if __name__ == '__main__':
    MainApp().run()