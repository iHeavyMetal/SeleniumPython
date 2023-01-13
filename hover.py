import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.w3schools.com")
driver.find_element(By.ID, "accept-choices").click()


tutorial_element = driver.find_element(By.ID, "navbtn_references")

webdriver.ActionChains(driver).move_to_element(tutorial_element).click(tutorial_element).perform()

time.sleep(3)