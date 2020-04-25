import threading
import time
import sys
import random
import webview
from JARVIS import JARVIS
import json

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
    
    def goTo(self, windowName, title):
        changeWindow(windowName, title)

    def loadUrl(self):
        print(1)
        urlJson = json.dumps(self.jarvis.urlDict)
        response = {
                'type': 'url',
                'message': urlJson
            }
        return response
    
    def loadDir(self):
        print(2)
        dirJson = json.dumps(self.jarvis.dirDict)
        response = {
                'type': 'dir',
                'message': dirJson
            }
        return response

    def loadAcc(self):
        print(3)
        accJson = json.dumps(self.jarvis.accountsDict)
        response = {
                'type': 'acc',
                'message': accJson
            }
        return response
    
    def printSomething(self, something):
        print(something)




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
    #api.loadUrl()