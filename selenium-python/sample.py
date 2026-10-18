import json
import time
from selenium.webdriver.common.by import By
from selenium import webdriver

url = "https://www.example.com/"

driver = webdriver.Firefox()

driver.get(url)

target_class = "class-name-here"
target_id_1 = "element-id1"
target_id_2 = "element-id2"
target_selector = "a#element"


print(driver.find_element(By.ID, target_id_1).text)
print(driver.find_element(By.CLASS_NAME, target_class).text)
print(driver.find_element(By.CSS_SELECTOR, target_selector).get_dom_attribute("href"))
print(driver.find_elements(By.CLASS_NAME, target_class))

driver.find_element(By.ID, target_id_1).find_element(By.ID, target_id_2)


