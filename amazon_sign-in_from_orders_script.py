from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=/Users/Daniel/Documents/Automation/python-selenium-automation/chromedriver)
driver.get('https://www.amazon.com/')

driver.find_element(by.ID, 'nav-orders').click()

assert driver.find_element(By.XPath, "//h1[text()= 'Sign-In']") and driver.find_element(By.ID, 'ap_email'),
    f'Error! Cannot find Sign In header and/or email input field'

print('Test case passed')

driver.quit()
