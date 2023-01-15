import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#It1s better method than sleep
driver.implicitly_wait(10)
driver.get("file://C:/Users/godte/Desktop/Projects/SeleniumPython/files/Waits2.html")
driver.find_element(By.ID, "clickOnMe").click()     #change ID to something else to get "NoSuchElementException:
                                                    # Message: no such element: Unable to locate element"
print(driver.find_element(By.TAG_NAME, "p").text)

time.sleep(1)