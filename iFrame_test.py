from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("file://C:/Users/godte/Desktop/Projects/SeleniumPython/files/iFrameTest.html")

print(driver.find_element(By.TAG_NAME, "h1").text)
driver.switch_to.frame(driver.find_element(By.TAG_NAME, "iframe")) #switch to iframe
print(driver.find_element(By.TAG_NAME, "h1").text)
driver.switch_to.default_content()          #switch to default site
print(driver.find_element(By.TAG_NAME, "h1").text)