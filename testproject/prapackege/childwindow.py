#In this class we learn the child window handling
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()
driver.find_element_by_xpath("//a[text()='Click Here']").click()
print(driver.title)
driver.switch_to.window(driver.window_handles[1])
print(driver.title)
driver.quit()