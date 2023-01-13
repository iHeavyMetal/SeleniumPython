import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("file://C:/Users/godte/Desktop/Projects/SeleniumPython/files/Test.html")

driver.find_element(By.ID, "newPage").click()
print(driver.title)     #check what page is in focus
current_window_name = driver.current_window_handle #check current window active
window_names = driver.window_handles #get all windows

for window in window_names:
    if window != current_window_name:
        driver.switch_to.window(window)
time.sleep(3)

print(driver.title)
driver.switch_to.window(current_window_name)  #switch again to first window
print(driver.title)
time.sleep(5)