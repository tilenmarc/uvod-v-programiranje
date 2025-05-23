from selenium import webdriver
import time


from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("https://www.imdb.com/search/title/?title_type=feature")
time.sleep(5)
for _ in range(20):
    gumb = driver.find_element(By.CLASS_NAME, "ipc-see-more__button")

    gumb.send_keys(Keys.RETURN)
    time.sleep(2)

driver.page_source()
