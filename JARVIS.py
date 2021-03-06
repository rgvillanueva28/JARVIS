import os
#import threading
import multiprocessing
import webbrowser as wb
from voiceRecognition import VoiceRecognition as vr
from login import Login
#from gtts import gTTS
import pyttsx3
from io import BytesIO
import pyaudio
import playsound
import threading


class JARVIS():


    
    def __init__(self):
        self.inp = ""
        self.dirDict = {}
        self.urlDict = {}
        self.accountsDict = {}
        self.selectorDict = {}
        self.browser = ""
        self.checkDirectories()
        self.checkUrls()
        self.checkAccounts()
        self.checkSelectors()
        #self.printDicts()
    

    def printDicts(self):
        print(self.dirDict)
        print(self.urlDict)
        print(self.accountsDict)
        print(self.selectorDict)
    

    def getCommand(self):
        #self.inp = input("""Please enter your command: """)
        #print("Say: ")

        print('jarvis getCommand')
        self.inp = vr().recognize()
        #self.inp = "login messenger"
        print(self.inp)
        return self.inp.upper()
        #self.checkCommand()
    

    def checkCommand(self):
        print("self.inp = ", self.inp)
        print(self.inp.lower().split())

        if self.inp.lower().split()[0] == "error":
            print("Can't understand. Sorry")
            print(self.inp)
            return "Can't understand. Sorry"
        else:
            print(self.inp)

            command = self.inp.lower().split()[0]
        
            if command == "nica":
                wb.open_new_tab(r"https://www.facebook.com/alonica28")
            elif command == "open":
                programName = self.inp.lower().split(" ", 1)[1]
                response = self.openCmd()
                return response.upper()
            elif command == "browse":
                self.browseCmd()
            elif command == "login":
                self.loginCmd()
            else:
                
                #print("Command not found")
                self.speak("Command not found")
            

    def openCmd(self):
        programName = self.inp.lower().split(" ", 1)[1]
        if programName in self.dirDict:
            program = self.dirDict[programName]
            try:
                self.speak('Opening ' + programName)
                os.startfile(program)
                return "OPENED %s" % programName.upper()
            except FileNotFoundError as ex:
                print("Program not found")
                return "Program not found".upper()
        else:
            self.speak("Program not found")
            return "Program not found".upper()
        #print(program)


    def browseCmd(self):
        url = self.inp.lower().split(" ", 1)[1]
        if url in self.urlDict:
            urlf = self.urlDict[url]
            self.speak('Browsing ' + url)
            wb.open_new_tab(urlf)
            #print("good")
        else:
            self.speak('Browsing ' + url + ' dot com')
            wb.open_new_tab(r"https://" + url + r".com/")
            #print("bad")
        #print(program)
    

    def loginCmd(self):
        domain = self.inp.lower().split(" ", 1)[1]

        if domain in self.urlDict and domain in self.accountsDict:
            user = self.accountsDict[domain][0]
            passwd = self.accountsDict[domain][1]
            userSel = self.selectorDict[domain][0]
            passSel = self.selectorDict[domain][1]
            url = self.urlDict[domain]

            #print(user,passwd,userSel,passSel,domain)
            #thread1 = threading.Thread(target = Login, args = (url, user, passwd, userSel, passSel))
            #thread1.setDaemon(True)
            #thread1.start()
            self.speak('Logging into ' + domain)
            process = multiprocessing.Process(target = Login, args = (url, user, passwd, userSel, passSel))
            process.start()

            #wb.open_new_tab(url)
            #print("good")
        else:
            #wb.open_new_tab(r"https://" + url + r".com/")
            print("Login credentials not found.")
        #print(program)


    def speak(self, mess):
        #print(os.path.dirname(__file__))
        file = os.path.dirname(__file__)+r'/audio/response.wav'
        file = 'audio/response.wav'

        if (mess == 'Redirecting to JARVIS Dashboard.'):
            playsound.playsound('audio/redirecting.wav')
        else:
            engine = pyttsx3.init()
            engine.setProperty('rate',150)
            engine.save_to_file(mess, file)
            engine.runAndWait()

            playsound.playsound(file)
            #threading.Timer(5.0, os.remove, [file]).start()
            os.remove(file)
            
            # tts = gTTS(mess)
            # tts.save(file)
            # playsound.playsound(file)
            # os.remove(file)


    def checkDirectories(self):
        try:
            file = open(r"database/directories.txt","r")
        except Exception as ex:
            print(ex)

        for line in file:
            lineText = " ".join(line.split())
            lineText = lineText.split("=")
            lineList = [i.strip() for i in lineText]
            lineList = [i.strip(r'"') for i in lineList]
            
            self.dirDict[lineList[0].lower()] = lineList[1].lower()

        file.close()
        #print(self.dirDict)
    

    def checkUrls(self):
        try:
            file = open(r"database/urls.txt","r")
        except Exception as ex:
            print(ex)

        for line in file:
            lineText = " ".join(line.split())
            lineText = lineText.split("=")
            lineList = [i.strip() for i in lineText]
            lineList = [i.strip(r'"') for i in lineList]
            
            self.urlDict[lineList[0].lower()] = lineList[1].lower()

        file.close()
        #print(self.urlDict)


    def checkAccounts(self):
        try:
            file = open(r"database/accounts.txt", "r")
        except Exception as ex:
            print(ex)

        for line in file:
            lineText = " ".join(line.split())
            domain, creds = lineText.split("=")
            domain = domain.strip()
            credsList = creds.strip().split(";")
            credsList = [i.strip() for i in credsList]
            self.accountsDict[domain] = credsList
            #print("'" + domain + "'")
            #print("'" + str(credsList) + "'")

        file.close()
        #print(self.accountsDict)
    

    def checkSelectors(self):
        try:
            file = open(r"database/urlSelector.txt", "r")
        except Exception as ex:
            print(ex)

        for line in file:
            lineText = " ".join(line.split())
            domain, sel = lineText.split("=")
            domain = domain.strip()
            selectorList = sel.strip().split(";")
            selectorList = [i.strip() for i in selectorList]
            self.selectorDict[domain] = selectorList
            #print("'" + domain + "'")
            #print("'" + str(credsList) + "'")

        

        file.close()
        #print(self.selectorDict)
    







    """
    def registerBrowser(self):
        self.browser = wb.get()
        print(self.browser)
"""


if __name__ == '__main__':
    pass
    #JARVIS()

    #main.getCommand() #execute

    #main.checkUrls()
    #main
    #main.registerBrowser()