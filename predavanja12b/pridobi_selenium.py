from selenium import webdriver

from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()


driver.get("https://www.imdb.com/search/title/?title_type=feature")
sleep(5)

for _ in range(10):
    button = driver.find_element(
        By.CLASS_NAME,
        "ipc-see-more__button",
    )
    button.send_keys(Keys.RETURN)
    # button.click()
    sleep(2)

print(driver.page_source)
