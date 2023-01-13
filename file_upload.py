import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import os
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("file:///C:/Users/godte/Desktop/Projects/SeleniumPython/files/FileUpload.html")

upload_input = driver.find_element(By.ID, "myFile")
path = os.path.abspath("uploadMe.txt")

driver.save_screenshot("screenshot/screen1.png")
upload_input.send_keys(path)
driver.save_screenshot("screenshot/screen2.png")

time.sleep(3)