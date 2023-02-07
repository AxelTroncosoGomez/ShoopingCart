from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivymd.uix.button import MDFloatingActionButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton
from kivymd.uix.boxlayout import BoxLayout

KV = """
MDBoxLayout:
    orientation: "vertical"
    MDScreen:
        MDRectangleFlatButton:
            text: "Alert POPUP!"
            pos_hint: {"center_x": .5, "center_y": .5}
            on_release: app.show_alert_dialog()
        MDLabel:
            id: my_label
            text: "some STUFF"
            pos_hint: {"center_x": .95, "center_y": .45}

<Content>
    orientation: "vertical"
    spacing: "12dp"
    size_hint_y: None
    height: "25dp"

    MDTextField:
        id: password
        hint_text: "Enter a password"
"""

class Content(BoxLayout):
    pass

class MainApp(MDApp):
    dialog = None
    pass_dialog = None
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'DeepPurple'
        return Builder.load_string(KV)

    def close_dialog(self, obj):
        self.dialog.dismiss()

    def check_pass(self, obj):
        if self.root.ids.password.text == 'hola':
            MDDialog(
                title="Perfecto",
                buttons=[
                    MDFlatButton(
                        text="OK",
                        theme_text_color= "Custom",
                        text_color = self.theme_cls.primary_color,
                        on_release = self.close_dialog
                    ),
                ],
            )
        else:
            MDDialog(
                title="Intente otra password",
                buttons=[
                    MDFlatButton(
                        text="OK",
                        theme_text_color= "Custom",
                        text_color = self.theme_cls.primary_color,
                    ),
                ],
            )

    def show_alert_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title = 'Titulo generico',
                type="custom",
                content_cls=Content(),
                buttons = [
                    MDFlatButton(
                        text = "Cancel",
                        text_color = self.theme_cls.primary_color,
                        on_release = self.close_dialog

                    ),
                    MDRectangleFlatButton(
                        text = "Yes",
                        text_color = self.theme_cls.primary_color,
                        on_release = self.check_pass
                    )
                ]
            )
        self.dialog.open()



if __name__ == '__main__':
    MainApp().run()