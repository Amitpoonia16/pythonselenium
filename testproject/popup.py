from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

message="Amit"
driver.find_element_by_id("name").send_keys(message)
driver.find_element_by_id("alertbtn").click()
alert = driver.switch_to.alert
ac_message = alert.text
alert.accept()
assert message in ac_message
driver.close()


