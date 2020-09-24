#Check the product count on the first page
import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()

product_count = driver.find_elements_by_xpath("//div[@class='product']")
product_count1 = len(product_count)
print(product_count1)

driver.close()