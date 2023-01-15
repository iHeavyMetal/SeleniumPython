import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("file://C:/Users/godte/Desktop/Projects/SeleniumPython/files/Test.html")

first_name = driver.find_element(By.ID, 'fname')
if first_name.is_enabled():
    first_name.send_keys("Selenium")
else:
    print("Element is disabled")

time.sleep(3)