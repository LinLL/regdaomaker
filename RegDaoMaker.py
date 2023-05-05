from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import time

class RegDaoMaker(object):
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="./util/chromedriver113")


    def reg(self, mail, passwd):
        self.driver.get("https://daomaker.com/register")
        time.sleep(1)
        print(mail)
        js_script = f"""document.querySelector("input[type='email']").value="{mail}";document.querySelector("input[type='email']").dispatchEvent(new Event('input'))"""
        self.driver.execute_script(js_script)
        js_script = f"""document.querySelector("input[type='password']").value="{passwd}";document.querySelector("input[type='password']").dispatchEvent(new Event('input'))"""
        self.driver.execute_script(js_script)
        js_script = f"""document.querySelector("input[type='checkbox']").click() """
        self.driver.execute_script(js_script)
        time.sleep(1)

        js_script = f"""document.querySelector("div.form-action>button").click() """
        self.driver.execute_script(js_script)

        wait = WebDriverWait(self.driver, 30)
        wait.until(EC.url_contains("reg-verify-email"))



if __name__ == '__main__':
    testRegDaoMaker = RegDaoMaker()
    #testRegDaoMaker.test()
    testRegDaoMaker.reg("pavasaicob@hotmail.com", "q1w2e3R$")
