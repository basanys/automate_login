import time

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pyvirtualdisplay import Display

service = Service(executable_path=r'/usr/bin/chromedriver')
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

with Display(visible=False, size=(1200, 1500)):
    driver = webdriver.Chrome(service=service, options=chrome_options)
    loginid = "username"
    password = "password"

    driver.get("https://login.ruhr-uni-bochum.de/cgi-bin/start")

    driver.find_element(By.NAME, "loginid").send_keys(loginid)
    driver.find_element(By.NAME, "password").send_keys(password)

    driver.find_element(By.NAME, "action").click()

    #time.sleep(10)

    driver.quit()
