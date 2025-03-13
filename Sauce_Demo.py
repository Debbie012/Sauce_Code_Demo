import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize Chrome browser instance using Selenium WebDriver
driver = webdriver.Chrome()

# Navigate to the login page of Sauce Demo
driver.get("https://www.saucedemo.com/inventory.html")
time.sleep(5)

# Login with a valid username
driver.find_element(By.ID,"user-name").send_keys("standard_user")
time.sleep(5)

# Enter Password
driver.find_element(By.ID,"password").send_keys("secret_sauce")
time.sleep(5)

# Click Login
driver.find_element(By.ID,"login-button").click()
time.sleep(5)

# Add a backpack to cart
driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack").click()
time.sleep(5)

# Add bike light to cart
driver.find_element(By.ID,"add-to-cart-sauce-labs-bike-light").click()
time.sleep(5)

# Add T-Shirt to cart
driver.find_element(By.ID,"add-to-cart-sauce-labs-bolt-t-shirt").click()
time.sleep(5)

# Add Jacket to cart
driver.find_element(By.ID,"add-to-cart-sauce-labs-fleece-jacket").click()
time.sleep(5)

# Add Onesie to cart
driver.find_element(By.ID,"add-to-cart-sauce-labs-onesie").click()
time.sleep(5)

# Add Red T-Shirt to cart
driver.find_element(By.ID,"add-to-cart-test.allthethings()-t-shirt-(red)").click()
time.sleep(5)

# Click on the burger menu
driver.find_element(By.ID,"react-burger-menu-btn").click()
time.sleep(5)

# Click on Logout
driver.find_element(By.ID,"logout_sidebar_link").click()
time.sleep(5)
