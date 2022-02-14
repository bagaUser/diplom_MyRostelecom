from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class MyRostelecom(MDApp):
    def build(self):
        return MDLabel(text="Hello, My Rostelecom!", halign="center")


MyRostelecom().run()