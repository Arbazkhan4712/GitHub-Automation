from selenium import webdriver
from time import sleep
from pass import pw,uname
import sys

class github:
    def __init__(self, username, pw, pname, path):
        self.driver = webdriver.Chrome(path)
        self.driver.get("https://github.com/login")
        sleep(2)
        self.driver.find_element_by_id("login_field")\
            .send_keys(username)
        sleep(2)
        self.driver.find_element_by_id("password")\
            .send_keys(pw)
        self.driver.find_element_by_name("commit")\
            .click()
        sleep(2)
        self.driver.find_element_by_partial_link_text("New")\
            .click()
        sleep(2)
        self.driver.find_element_by_id("repository_name")\
            .send_keys(pname)
        sleep(2)
        self.driver.find_element_by_xpath("//button[normalize-space()='Create repository']")\
            .click()
        sleep(2)
        self.driver.find_element_by_xpath("//summary[@aria-label='View profile and more']//span[@class='dropdown-caret']")\
            .click()
        sleep(2)
        self.driver.find_element_by_xpath("//button[@class='dropdown-item dropdown-signout']")\
            .click()
        sleep(10)

       
        
        
pname = sys.argv[1]
github(uname,pw,pname,path)
