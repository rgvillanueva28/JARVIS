import threading
import time
import sys
import random
import webview
from JARVIS import JARVIS
import json

# from webview.platforms.cef import settings
# settings.update({
#     'persist_session_cookies': True
# })

JARVIS = JARVIS()

class Api:
    
    def checkCreds(self, user, passwd):
        if (user=="r") and (passwd=="r"):
            response = {
                "message": "Redirecting to JARVIS Dashboard.",
                "valid": "yes"
            }

            threading.Timer(0.1, JARVIS.speak, [response["message"]]).start()
            threading.Timer(3.0, changeWindow, ["templates/index.html", "JARVIS | Dashboard"]).start()

            return response
            

        else:
            response = {
                "message": "Invalid credentials for {}".format(user),
                "valid": "no"
            }
            return response
        
    def talk(self):
        text = self.getCommand()

        response = {
                "message": text
            }
            
        return response

    def getCommand(self):
        text = JARVIS.getCommand()
        #print(text)
        #threading.Timer(3.0, self.checkCommand).start()
        thread2 = threading.Thread(target = self.checkCommand)
        thread2.setDaemon(True)
        thread2.start()
        return text

    def jarvisText(self, message):
        #print(message, "here")
        print("message = ", message)
        JARVIS.inp = message
        print("JINP = ",JARVIS.inp)
        thread2 = threading.Thread(target = self.checkCommand)
        thread2.setDaemon(True)
        thread2.start()
        response = {
                "message": message.upper()
            }
        #print(response)
        return response

    def checkCommand(self):
        response = JARVIS.checkCommand()
        #print(response)
    
    def goTo(self, windowName, title):
        changeWindow(windowName, title)

    def loadUrl(self):
        urlJson = json.dumps(JARVIS.urlDict)
        response = {
                "type": "url",
                "message": urlJson
            }
        return response
    
    def loadDir(self):
        dirJson = json.dumps(JARVIS.dirDict)
        response = {
                "type": "dir",
                "message": dirJson
            }
        return response

    def loadAcc(self):
        accJson = json.dumps(JARVIS.accountsDict)
        response = {
                "type": "acc",
                "message": accJson
            }
        return response

    def loadSel(self):
        selJson = json.dumps(JARVIS.selectorDict)
        response = {
                "type": "sel",
                "message": selJson
            }
        return response

    #saving to file
    def saveUrl(self, name, url):
        urlFile=open(r"database/urls.txt", "a+")
        urlFile.write("\n" + name + ' = \"' + url + '\"')
        urlFile.close()

        JARVIS.checkUrls()
    
    def saveDir(self, name, dirr):
        dirFile=open(r"database/directories.txt", "a+")
        dirFile.write("\n" + name + ' = \"' + dirr + '\"')
        dirFile.close()

        JARVIS.checkDirectories()
    
    def saveAcc(self, name, username, passwd):
        accFile=open(r"database/accounts.txt", "a+")
        accFile.write("\n" + name + ' = ' + username + ';' + passwd)
        accFile.close()

        JARVIS.checkAccounts()
    
    def saveSel(self, name, usernameSel, passwdSel):
        selFile=open(r"database/urlSelector.txt", "a+")
        selFile.write("\n" + name + ' = ' + usernameSel + ';' + passwdSel)
        selFile.close()

        JARVIS.checkSelectors()




def changeWindow(windowName, title):
    window.load_url(windowName)
    window.set_title(title)

def changeTitle(title):
    window.set_title(title)

def getElem(elemId):
    window.get_elements(elemId)


if __name__ == "__main__":
    api = Api()
    #window = webview.create_window("JARVIS | Login", "templates/login.html", js_api = api, min_size=(900, 700))
    window = webview.create_window("JARVIS | Dashboard", "templates/index.html", js_api = api, min_size=(1000, 750),text_select=True)
    webview.start(debug=True, gui="cef")
    #api.loadUrl()