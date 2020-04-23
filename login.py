from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import os


class Login():

    def __init__(self, url, user, passwd, userSel, passSel):
        #print(os.path.dirname(__file__) + "/chromedriver.exe")
        self.path = os.path.dirname(__file__) + "/chromedriver/chromedriver.exe"
        self.options = Options()
        self.options.add_experimental_option("detach", True)
        self.options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.options.add_experimental_option('useAutomationExtension', False)
        self.options.binary_location = r"C:\Program Files (x86)\BraveSoftware\Brave-Browser\Application\brave.exe"
        #print(os.getcwd())
        self.options.add_argument("start-maximized")
        self.options.add_argument("disable-infobars") ##deprecated
        self.browser = webdriver.Chrome(executable_path = self.path, options=self.options)
        #print(str((os.path.join(os.getcwd(), "\\chromedriver.exe"))))

        #self.browser.maximize_window()

        self.url = url
        self.user = user
        self.passwd = passwd
        self.userSel = userSel
        self.passSel = passSel

        self.browser.get(self.url)

        self.inputCreds()


    def inputCreds(self):
        
        try:
            sleep(1)
            button = self.browser.find_element_by_xpath("/html/body/div[8]/div/div/div/div/div/div/div[2]/button")
            button.click()
        except Exception as ex:
            #print(ex)
            pass

        userElem = self.browser.find_element_by_css_selector(self.userSel)
        userElem.send_keys(self.user)

        passElem = self.browser.find_element_by_css_selector(self.passSel)
        passElem.send_keys(self.passwd)

        try:
            passElem.submit()
        except:
            try:
                signin = self.browser.find_element_by_xpath('/html/body/div[4]/div/div/form/div/ul/li[3]/input')
                signin.click()
            except:
                pass
            
        return self.browser
    

#if __name__ == "__main__":
    #Login("https://mapua.blackboard.com/","rgrvillanueva@mymail.mapua.edu.ph","Nica_082812","#user_id","#password")