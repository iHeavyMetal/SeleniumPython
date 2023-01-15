import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("file://C:/Users/godte/Desktop/Projects/SeleniumPython/files/Waits.html")
driver.find_element(By.ID, "clickOnMe").click()
time.sleep(5)

print(driver.find_element(By.TAG_NAME, "p").text)

time.sleep(1)

