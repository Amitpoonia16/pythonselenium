#in this class we will add the product and we will check the sum of the product price is right or not

import time

from selenium import webdriver
search_name="ca"
driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.implicitly_wait(2)
driver.find_element_by_css_selector("input.search-keyword").send_keys(search_name)
time.sleep(2)
product_name = driver.find_elements_by_css_selector("h4.product-name")
add_to_cart=driver.find_elements_by_xpath("//button[text()='ADD TO CART']")
for addtocart in add_to_cart:
    addtocart.click()

driver.find_element_by_css_selector("a.cart-icon").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
amounts= driver.find_elements_by_xpath("//*[@class='cartTable']//tr//td[5]//p")
sum =0
for amount in amounts:
    sum = sum +int(amount.text)
total_amount=driver.find_element_by_class_name("totAmt").text
assert sum == int(total_amount)
print("Test cases pass")
driver.close()