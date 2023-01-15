import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("file://C:/Users/godte/Desktop/Projects/SeleniumPython/files/Test.html")

#first method to find if element exist

element_exist = driver.find_elements(By.TAG_NAME, "p")

if len(element_exist) > 0:
    print("Element exist")
else:
    print("No such element")

#second method to find if element exist

try:
    driver.find_element(By.TAG_NAME, "example")
    print("Element exist")
except NoSuchElementException:
    print("No such element")

time.sleep(3)