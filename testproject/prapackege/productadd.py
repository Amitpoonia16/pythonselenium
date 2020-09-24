#Add the product into cart
from selenium import webdriver
driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.find_element_by_xpath("//button[text()='ADD TO CART']").click()
driver.close()