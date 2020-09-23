import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()

driver.find_element_by_css_selector("input.search-keyword").send_keys("br")
time.sleep(4)
product_count = driver.find_elements_by_xpath("//div[@class='products']/div")

addbutton = driver.find_elements_by_xpath("//button[text()='ADD TO CART']")
print(len(product_count))

for addbutton1 in addbutton:
    addbutton1.click()

