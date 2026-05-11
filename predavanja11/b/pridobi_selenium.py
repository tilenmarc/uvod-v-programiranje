from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()

driver.get("https://www.imdb.com/search/title/?title_type=feature")

time.sleep(10)
for _ in range(10):
    gumb = driver.find_element(By.CLASS_NAME, "ipc-see-more__button")
    gumb.send_keys(Keys.RETURN)

    time.sleep(5)

print(driver.page_source)
