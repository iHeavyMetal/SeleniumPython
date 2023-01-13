import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://demos.telerik.com/kendo-ui/dragdrop/index")

time.sleep(3)

draggable = driver.find_element(By.ID, "draggable")
droptarget = driver.find_element(By.ID, "droptarget")

webdriver.ActionChains(driver).drag_and_drop(draggable,droptarget).perform()



time.sleep(3)


