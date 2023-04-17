from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert

from time import sleep

driver = webdriver.Chrome()
driver.get("http://127.0.0.1:5500/ExcerciseDay3.html")

button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//body/button')))
button.click()

WebDriverWait(driver, 10).until(EC.alert_is_present())
alert = driver.switch_to.alert
print(alert.text)
alert.accept()
driver.switch_to.default_content()

button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//body/button[2]')))
button.click()

# wait for the new window to be present
WebDriverWait(driver, 10).until(EC.new_window_is_opened)

# add an implicit wait before switching to the new window
driver.implicitly_wait(30)

# print the current window handles
print("Window handles:", driver.window_handles)

# switch to the new window
driver.switch_to.window(driver.window_handles[1])

# get the title of the new window and print it to the console
new_window_title = driver.title
print(new_window_title)

# close the new window and switch back to the original window
driver.close()
driver.switch_to.window(driver.window_handles[0])


# switch to the second iframe
driver.switch_to.frame(0)

# find the button and click it
button = driver.find_element(By.XPATH, "//body/button")
button.click()

# wait for the confirm dialog to be present and dismiss it
WebDriverWait(driver, 30).until(EC.alert_is_present())
alert = driver.switch_to.alert
print(alert.text)
alert.dismiss()

sleep(20)
driver.quit()
