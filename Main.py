from selenium import webdriver
from time import sleep
from pass import pw,uname
import sys

class github:
    def __init__(self, username, pw, pname):
        self.driver = webdriver.Chrome()
        self.username = username
        self.driver.get("https://github.com/login")
        sleep(2)
        self.driver.find_element_by_id("login_field")\
            .send_keys(username)
        sleep(2)
        self.driver.find_element_by_id("password")\
            .send_keys(pw)
        self.driver.find_element_by_xpath("/html/body/div[3]/main/div/form/div[4]/input[9]")\
            .click()
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[4]/div/aside[1]/div[2]/div[2]/div/h2/a")\
            .click()
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[4]/main/div/form/div[2]/auto-check/dl/dd/input")\
            .send_keys(pname)
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[4]/main/div/form/div[3]/button")\
            .click()
        sleep(2)
        self.driver.find_element_by_class_name("Header-link")\
            .click()
        sleep(2)
        self.driver.find_element_by_class_name("dropdown-item dropdown-signout")\
            .click()
        sleep(10)

       
        
        
pname = sys.argv[1]
github(uname,pw,pname)
