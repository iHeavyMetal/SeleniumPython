import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("file://C:/Users/godte/Desktop/Projects/SeleniumPython/files/Test.html")

driver.find_element(By.ID, "clickOnMe").click()
#time.sleep(1)
driver.switch_to.alert.accept()
time.sleep(3)
driver.find_element(By.ID, "clickOnMe").click()
#time.sleep(1)
driver.switch_to.alert.dismiss()

#driver.find_element(By.NAME, "password").send_keys(Keys.ENTER) # sent key ENTER to password field

car_select = Select(driver.find_element(By.TAG_NAME, "select"))
#car_select.select_by_visible_text("Volvo") #by text
car_select.select_by_value("saab")          #by value
#car_select.select_by_index(0)              #by index

driver.find_element(By.XPATH, "//input[@type='checkbox']").click() #checkbox
driver.find_element(By.XPATH, "//input[@value='male']").click()   #radio. can choose multiple options

time.sleep(3)