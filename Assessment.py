from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert

from time import sleep

driver = webdriver.Chrome()

# Launch a browser of your choice and navigate to "https://www.saucedemo.com/".

driver.get("https://www.saucedemo.com/")

# Write a Java method that accepts a locator type (ID, Name, ClassName, TagName, CSS, XPath) and a locator value as parameters, and returns a WebElement.

def find_element(locator_type, locator_value):
    # Find the element based on the provided locator type and value
    if locator_type == 'id':
        element = WebDriverWait(driver, 50).until(
            EC.presence_of_element_located((By.ID, locator_value))
        )
    elif locator_type == 'name':
        element = WebDriverWait(driver, 50).until(
            EC.presence_of_element_located((By.NAME, locator_value))
        )
    elif locator_type == 'class':
        element = WebDriverWait(driver, 50).until(
            EC.presence_of_element_located((By.CLASS_NAME, locator_value))
        )
    elif locator_type == 'tag':
        element = WebDriverWait(driver, 50).until(
            EC.presence_of_element_located((By.TAG_NAME, locator_value))
        )
    elif locator_type == 'css':
        element = WebDriverWait(driver, 50).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, locator_value))
        )
    elif locator_type == 'xpath':
        element = WebDriverWait(driver, 50).until(
            EC.presence_of_element_located((By.XPATH, locator_value))
        )
    else:
        raise ValueError('Invalid locator type')

    return element

# The logo with the class name "login_logo".
logo = find_element('class', 'login_logo')
print(logo)
print(logo.text)

# The username with the class name "login_logo".
username = find_element('id', 'user-name')
print(username)
print(username.text)

# The password with the class name "login_logo".
password = find_element('id', 'password')
print(password)
print(password.text)

# The button with the class name "login_logo".
print("======================================================================")
button = find_element('id', 'login-button')
print(button)
print(button.get_attribute("value"))

# Enter the text "standard_user" in the username input field.
username = find_element('id', 'user-name')
username.send_keys("standard_user")

# Enter the text "secret_sauce" in the password input field.
username = find_element('id', 'password')
username.send_keys("secret_sauce")

# The login button with the ID "login-button".

button = find_element('id', 'login-button')
button.click()

# Verify that the user has successfully logged in by checking if an element with the class name "inventory_list" is present.
print("======================================================================")
link = find_element('class', 'inventory_list')
options = link.find_elements(By.CLASS_NAME, 'inventory_item')
for x in options:
    main = x.find_elements(By.CLASS_NAME, 'inventory_item_name')
    for mains in main:
        print(mains.text)

# Implement an implicit wait of 10 seconds.
driver.implicitly_wait(10)

# Write a method that accepts a WebDriverWait instance and a By instance as parameters, and returns a WebElement after waiting for it to be visible. Use this method to locate an element with the class name "inventory_list" and print its text.
print("======================================================================")
inventorylst = WebDriverWait(driver, 30).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, 'inventory_list')))
for element in inventorylst:
    print(element.text)


# Locate title link
inventory_item = driver.find_element(By.ID, "item_4_title_link")
inventory_item.click()

# Print details name
print("======================================================================")
inventory_details_name = driver.find_element(By.CLASS_NAME, "inventory_details_name")
print(inventory_details_name.text)

# Click add to cart button
btn_primary = driver.find_element(By.CLASS_NAME, "btn_primary")
btn_primary.click()

# Click cart button
shopping_cart_link = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
shopping_cart_link.click()

# Print Cart List
print("======================================================================")
link = find_element('class', 'cart_list')
options = link.find_elements(By.CLASS_NAME, 'cart_item')
for x in options:
    main = x.find_elements(By.CLASS_NAME, 'inventory_item_name')
    for mains in main:
        print("Cart Item: " + mains.text)




sleep(20)
driver.close()