#In this class we have search the "ca" and added all the product into cart after that we will go to the cart page and will make sure that all product is added successfully.
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
product_size = len(product_name)
list = []
list2 = []
for productname in product_name:


    list.append(productname.text)
for addtocart in add_to_cart:
    addtocart.click()

driver.find_element_by_css_selector("a.cart-icon").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
product_name_cart_page= driver.find_elements_by_xpath("//*[@id='productCartTables']/tbody/tr/td[2]/p")
for product_name_cartpage in product_name_cart_page:
    list2.append(product_name_cartpage.text)

print(list)
print("List 2 item")
print(list2)

assert list == list2
print("Test cases pass")
driver.close()



