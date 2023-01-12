import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("http://www.google.pl")
#driver.maximize_window() #set_window_size(1920,1080)

time.sleep(5)

#driver.find_element(By.CLASS_NAME, "RNNXgb")
driver.find_element(By.NAME, "q").send_keys("selenium" + Keys.ENTER)


time.sleep(3)

