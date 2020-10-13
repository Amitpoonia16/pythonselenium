#In this class we did the complete process of checkout also we have taken the screenshot of success window
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.find_element_by_xpath("//a[@href='/angularpractice/shop']").click()
product=driver.find_elements_by_xpath("//*[@class='card h-100']")
for product1 in product:
    product_name=product1.find_element_by_xpath("div/h4").text

    if product_name == "Blackberry":
        driver.find_element_by_xpath("//div[@class='card-footer']/button").click()
    print(product_name)
driver.find_element_by_xpath("//a[@class='nav-link btn btn-primary']").click()
driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
driver.find_element_by_id("country").send_keys("indi")
wait = WebDriverWait(driver,7)
wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@class='suggestions']/ul/li/a")))

driver.find_element_by_xpath("//div[@class='suggestions']/ul/li/a").click()
driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
driver.find_element_by_xpath("//input[@class='btn btn-success btn-lg']").click()
success = driver.find_element_by_xpath("//div[@class='alert alert-success alert-dismissible']").text
print(success)
driver.get_screenshot_as_file("screenshot/Checkoutdone.png")
driver.close()