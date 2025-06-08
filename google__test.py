from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com")

search_box = driver.find_element("name", "q")
search_box.send_keys("Selenium")
search_box.send_keys(Keys.RETURN)

time.sleep(3)
driver.quit()
