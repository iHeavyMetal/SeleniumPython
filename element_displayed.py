import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("file://C:/Users/godte/Desktop/Projects/SeleniumPython/files/Test.html")

paragraph = driver.find_element(By.TAG_NAME, 'p')

if paragraph.is_displayed():
    print("Is displayed")
    print(paragraph.text)
else:
    print("Is not displayed")
    print(paragraph.get_attribute("textContent"))

time.sleep(3)