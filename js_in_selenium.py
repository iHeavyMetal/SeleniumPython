import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("file://C:/Users/godte/Desktop/Projects/SeleniumPython/files/Test.html")

driver.execute_script("arguments[0].click();",driver.find_element(By.ID, "newPage"))

something = "Selenium"
driver.execute_script("arguments[0].setAttribute('value','" + something +"')",driver.find_element(By.ID, "fname"))


time.sleep(3)