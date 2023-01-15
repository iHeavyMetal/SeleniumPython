import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("file://C:/Users/godte/Desktop/Projects/SeleniumPython/files/Test.html")

checkbox = driver.find_element(By.XPATH, "//input[@type='checkbox']")

checkbox.click() #remove thit to get "selected" option

if checkbox.is_selected():
    print("Element is unselected")
    checkbox.click()
else:
    print("Element is selected")
    checkbox.click()
time.sleep(3)