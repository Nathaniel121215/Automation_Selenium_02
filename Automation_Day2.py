from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/")

#task 01
header = driver.find_element(By.CLASS_NAME, 'heading')
print(header.text)

#task 02
driver.get("https://the-internet.herokuapp.com/login")

username = driver.find_element(By.NAME, 'username')
username.send_keys("username")


#task 03
driver.get("https://the-internet.herokuapp.com/")
footer = driver.find_element(By.ID, 'page-footer')
print(footer.text)

#task 04
link = driver.find_element(By.XPATH, '//body/div[2]/div/ul')
options = link.find_elements(By.XPATH, '//li')
for x in options:
    main = x.find_elements(By.TAG_NAME, 'a')
    for mains in main:
        print(mains.get_attribute("href"))

#task 05
driver.get("https://the-internet.herokuapp.com/login")

password = driver.find_element(By.NAME, 'password')
password.send_keys("password")

#task 05

button = driver.find_element(By.CLASS_NAME, 'radius')
button.click()


sleep(20)
driver.close()