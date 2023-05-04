from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class RegDaoMaker(object):
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="./util/chromedriver")

    def reg(self):
        self.driver.get("https://daomaker.com/")

