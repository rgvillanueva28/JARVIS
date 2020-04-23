import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from JARVIS import JARVIS
from time import sleep
import threading
from kivy.core.window import Window

Window.clearcolor = (1, 1, 1, 1)

class MainWindow(Screen):
    lbltalk = ObjectProperty(None)
    jarvis = JARVIS()

    def btnTalk(self):
        self.lbltalk.text = "Talk now"

        thread1 = threading.Thread(target = self.getCommand)
        thread1.setDaemon(True)
        thread1.start()
        
    def getCommand(self):
        text = self.jarvis.getCommand()
        self.lbltalk.text = str(text)
        #threading.Timer(3.0, self.checkCommand).start()
        thread2 = threading.Thread(target = self.checkCommand)
        thread2.setDaemon(True)
        thread2.start()

    def checkCommand(self):
        response = self.jarvis.checkCommand()
        self.lbltalk.text = str(response)
        threading.Timer(5.0, self.finished).start()
    
    def finished(self):
        self.lbltalk.text = "Press Talk to start"


class SettingsWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

class BottomButton(Button):
    pass

jarvis = Builder.load_file("jarvis.kv")

class JarvisApp(App):
    def build(self):
        return jarvis


if __name__ == "__main__":
    JarvisApp().run()