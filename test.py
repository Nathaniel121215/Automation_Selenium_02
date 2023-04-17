from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Edge()
driver.get("http://flex.wesupportinc.com:8069/web/login")
elem1 = driver.find_element(By.NAME, "login")
elem1.send_keys("npenaranda@wesupportinc.com")
# elem1.send_keys(Keys.RETURN)

elem2 = driver.find_element(By.NAME, "password")
elem2.send_keys("gagaga")

# elem2.send_keys(Keys.RETURN)
# login_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
login_button = driver.find_element(By.CSS_SELECTOR,'.btn.btn-primary')
login_button.click()

# menuclick = driver.find_element(By.CLASS_NAME, 'nav-link nav-toggle')
# menuclick.click()



sleep(20)
driver.close()
