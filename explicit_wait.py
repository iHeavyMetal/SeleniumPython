import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#It`s better method than sleep and implicit_wait


wait = WebDriverWait(driver, 10, 0.5)
driver.get("file://C:/Users/godte/Desktop/Projects/SeleniumPython/files/Waits2.html")
driver.find_element(By.ID, "clickOnMe").click()
wait.until(expected_conditions.visibility_of_element_located((By.TAG_NAME, "p")))
print(driver.find_element(By.TAG_NAME, "p").text)

time.sleep(1)