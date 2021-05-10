from selenium.webdriver import Edge
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time


class Spyder:
    def __init__(self):
        self.driver = Edge(executable_path='./msedgedriver.exe')
        self.driver.get('https://coinmarketcap.com/currencies/dogecoin/historical-data/')
        self.run = True
        self.ClickButton()
        while (self.run):
            try:
                self.ClickButton()
            except:
                self.run = False;
                print('escaped')
                break;
        # self.l = WebDriverWait(self.driver, timeout=20).until(lambda d: d.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[2]/div/div[3]/div/div/div[2]/table/tbody'))
        self.f = open('raw-data.txt', 'a')
        # self.f.write(self.l.text)
        # self.f.close()
        self.c = 0
        while (True):
            try:
                self.c = self.c + 1
                self.l = WebDriverWait(self.driver, timeout=20).until(lambda d: d.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[2]/div/div[3]/div/div/div[2]/table/tbody/tr['+str(self.c)+']'))
                self.f.write(self.l.text+'\n')
            except:
                break
        self.f.close()
        #//*[@id="__next"]/div/div[1]/div[2]/div/div[3]/div/div/div[2]/table/tbody/tr[1]
        #//*[@id="__next"]/div/div[1]/div[2]/div/div[3]/div/div/div[2]/table/tbody/tr[2]
        #//*[@id="__next"]/div/div[1]/div[2]/div/div[3]/div/div/div[2]/table/tbody/tr[150]

        #//*[@id="__next"]/div/div[1]/div[2]/div/div[3]/div/div/div[2]
        


    def ClickButton(self):
        #//*[@id="__next"]/div/div[1]/div[2]/div/div[3]/div/div/p[1]/button
        btn = WebDriverWait(self.driver, timeout=20).until(lambda d: d.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[2]/div/div[3]/div/div/p[1]/button'))
        time.sleep(3)
        btn.send_keys(Keys.END)
        time.sleep(3)
        btn.click()
        #print(btn)

        #l = WebDriverWait(self.driver, timeout=20).until(lambda d: d.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[2]/div/div[3]/div/div/div[2]/table/tbody'))
        #print(l.text)
        
if __name__ == "__main__":
    spyder = Spyder()