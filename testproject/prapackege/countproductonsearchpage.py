#In this class we will write the code for counting the product number on search page
import time

from selenium import webdriver
search_name="ca"
driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.implicitly_wait(2)
driver.find_element_by_css_selector("input.search-keyword").send_keys(search_name)

product_count=driver.find_elements_by_xpath("//*[@class='product']")
product_number=len(product_count)
product_name=["Cauliflower - 1 Kg","Carrot - 1 Kg","Capsicum","Cashews - 1 Kg"]

product_name_on_search=driver.find_elements_by_xpath("//*[@class='product']/h4")

product_name_on_searchpage=[]
for product_name_onsearch in product_name_on_search:

    product_name_on_searchpage.append(product_name_onsearch.text)

driver.close()
print(product_name)
print(product_name_on_searchpage)
assert product_name_on_searchpage == product_name
print("Test result is pass")