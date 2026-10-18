# selenium

# import

```
from selenium.webdriver.common.by import By
from selenium import webdriver
```

# start browser driver

```
url = "https://www.example.com/"

driver = webdriver.Firefox()

driver.get(url)
```

# get elements

```
target_class = "class-name-here"
target_id_1 = "element-id1"
target_id_2 = "element-id2"
target_selector = "a#element"

print(i.find_element(By.ID, target_id_1).text)
print(i.find_element(By.CLASS_NAME, target_class).text)
print(i.find_element(By.CSS_SELECTOR, target_selector).get_dom_attribute("href"))
print(i.find_elements(By.CLASS_NAME, target_class))

print(i.find_element(By.ID, target_id_1).find_element(By.ID, target_id_2).text)
```
