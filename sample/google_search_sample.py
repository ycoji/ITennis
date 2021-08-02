from selenium import webdriver
import chromedriver_binary
import time

driver = webdriver.Chrome()
driver.get('https://www.google.com/')

search_box = driver.find_element_by_name("q")
search_box.send_keys('横浜市予約システム')
search_box.submit()

time.sleep(3)

driver.quit()

