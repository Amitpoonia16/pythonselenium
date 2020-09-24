#Search for the product and count the product count on search page
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()

driver.find_element_by_css_selector("[class='search-keyword']").send_keys("cu")
driver.implicitly_wait(5)

product_count = driver.find_elements_by_xpath("//div[@class='product']")
product_count1 = len(product_count)
print(product_count1)

driver.close()