from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
checkboxes = driver.find_elements_by_css_selector("input[type='checkbox']")

print(len(checkboxes))


for checkbox in checkboxes:
    print(checkbox.is_selected())
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()


for checkbox in checkboxes:

    print(checkbox.is_selected())
driver.close()
