import threading
import time
import sys
import random
import webview
from JARVIS import JARVIS

class Api:
    jarvis = JARVIS()
    def __init__(self):
        pass
    
    def checkCreds(self, user, passwd):
        if (user=='r') and (passwd=='r'):
            response = {
                'message': 'Redirecting to JARVIS Dashboard.',
                'valid': 'yes'
            }

            threading.Timer(0.1, self.jarvis.speak, [response['message']]).start()
            threading.Timer(3.0, changeWindow, ['templates/index.html', 'JARVIS | Dashboard']).start()

            return response
            

        else:
            response = {
                'message': 'Invalid credentials for {}'.format(user),
                'valid': 'no'
            }
            return response
        
    def talk(self):
        text = self.getCommand()

        response = {
                'message': text
            }
            
        return response

    def getCommand(self):
        text = self.jarvis.getCommand()
        print(text)
        #threading.Timer(3.0, self.checkCommand).start()
        thread2 = threading.Thread(target = self.checkCommand)
        thread2.setDaemon(True)
        thread2.start()
        return text

    def checkCommand(self):
        response = self.jarvis.checkCommand()
        print(response)
    




def changeWindow(windowName, title):
    window.load_url(windowName)
    window.set_title(title)

def changeTitle(title):
    window.set_title(title)


if __name__ == '__main__':
    api = Api()
    #window = webview.create_window('JARVIS | Login', 'templates/login.html', js_api = api, min_size=(900, 700))
    window = webview.create_window('JARVIS | Dashboard', 'templates/index.html', js_api = api, min_size=(900, 700))
    webview.start(debug=True)



'''
def third_window():
    # Create a new window after the loop started
    third_window = webview.create_window('Window #3', html='<h1>Third Window</h1>')



if __name__ == "__main__":
    mainWindow = webview.create_window('JARVIS', html=r"<h1>Hi I'm Jarvis!<h1>")
    loginWindow = webview.create_window('JARVIS | Login', html=r"<h1>Please enter login details!<h1>")
    settingsWindow = webview.create_window('JARVIS | Settings', html=r"<h1>This is the settings window!<h1>")
    webview.start(third_window)
# anything below this line will be executed after program is finished executing

'''
pass