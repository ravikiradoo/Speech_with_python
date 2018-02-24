import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
from urllib.parse import  urlparse
import sys

class Fetcher:
    def __init__(self,url):
        self.driver=webdriver.Chrome(r'C:\Users\Student\Downloads\chromedriver_win32\chromedriver.exe')
        self.driver.wait=WebDriverWait(self.driver,5)
        self.url=url
        self.lookup()

    def lookup(self):
        self.driver.get(self.url)
        try:
            ip=self.driver.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME,"gsfi")))
        except:
            print("Failed")

        soup=BeautifulSoup(self.driver.page_source,"html.parser")
        answer=soup.findAll(class_="_sPg")
        if not answer:
            answer=soup.findAll(class_="_m3b")
        print(answer[0].get_text())





