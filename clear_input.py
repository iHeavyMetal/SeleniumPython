import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("file://C:/Users/godte/Desktop/Projects/SeleniumPython/files/Test.html")

username_input = driver.find_element(By.NAME, "username")
username_input.clear()                                      #clear input
username_input.send_keys("PonuryAdam")


time.sleep(3)