import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) # get rid of "DeprecationWarning executable_path
                                                                            # has been deprecated please pass in a Service object"
                                                                            # Google it :)
driver.get("http://www.google.pl")


#driver.maximize_window() # or - set_window_size(1920,1080)

time.sleep(2)
driver.find_element(By.ID, "L2AGLb").click() # Method 1, click on google pop-up
#click_accept_button = driver.find_element(By.ID, "L2AGLb") # Method 2
#click_accept_button.click()

time.sleep(5)
driver.find_element(By.TAG_NAME, "img")
driver.find_element(By.CLASS_NAME, "RNNXgb")
driver.find_element(By.CSS_SELECTOR, "a")
driver.find_element(By.CSS_SELECTOR, "img")
image = driver.find_element(By.XPATH, "/html/body/div/div/div/img")
image2 = driver.find_element(By.XPATH, "//div/img")



elements_list_len = len(driver.find_elements(By.XPATH, "//div/img"))

driver.find_element(By.NAME, "q").send_keys("selenium" + Keys.ENTER)

print(image)
print(image2)
print("List length= ", elements_list_len)

time.sleep(3)

