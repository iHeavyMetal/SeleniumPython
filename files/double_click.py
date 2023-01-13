import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("file://C:/Users/godte/Desktop/Projects/SeleniumPython/files/DoubleClick.html")

button = driver.find_element(By.ID, "bottom")

#webdriver.ActionChains(driver).double_click(button).perform()  #double click
webdriver.ActionChains(driver).context_click(button).perform()  #right mouse click



time.sleep(3)