


ID - (By.ID, "example")
CSS_SELECTOR - (By.CSS_SELECTOR, '[name="q"]')
CSS_SELECTOR - driver.find_element((By.CSS_SELECTOR, "th:first-child").text) #table(th). print table content
NAME - (By.NAME, 'q')
LINK_TEXT - (By.LINK_TEXT, "example") #in <a href> tag
PARTIAL_LINK_TEXT - (By.PARTIAL_LINK_TEXT, "example")
CLASS_NAME - (By.CLASS_NAME, "example") #class="example1 example2" - can search by example1 or example2
TAG_NAME - (By.TAG_NAME, "example") # "a", "p", "img", "div", "label"

CSS_SELECTOR:
    a
    .red
     #fname
     div.row
    [aria-hidden="true"]
    li a
    li+a
    li,a
    p:first-child
    p:last-child
    p:nth-child(2)


XPATH:
/html/body/table/tr/th #path to specific tag
//table/tr/th #relative path start search from tag table
//th[text()='example'] #good practice. search in html with specific text
//input[@name='example']

XPATCH - (By.XPATH, "example")
(By.XPATH, "//button[@id='Click On Me']")



