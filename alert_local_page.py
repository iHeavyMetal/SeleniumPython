import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("file://C:/Users/godte/Desktop/Projects/SeleniumPython/files/Test.html")

driver.find_element(By.ID, "clickOnMe").click()
time.sleep(1)
driver.switch_to.alert.accept()
time.sleep(3)
driver.find_element(By.ID, "clickOnMe").click()
time.sleep(1)
driver.switch_to.alert.dismiss()


time.sleep(3)