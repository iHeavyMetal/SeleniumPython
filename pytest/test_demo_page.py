import pytest
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


@pytest.fixture()
def test_setup():
    global driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("file://C:/Users/godte/Desktop/Projects/SeleniumPython/files/Test.html")
    yield
    driver.quit()
def test_method(test_setup):
    assert driver.title =="Strona testowa", "Assertion failed. Expected: Strona testowa"
    time.sleep(5)

def test_method2(test_setup):
    assert driver.title =="Strona testowa", "Assertion failed. Expected: Strona testowa"
    time.sleep(1)





