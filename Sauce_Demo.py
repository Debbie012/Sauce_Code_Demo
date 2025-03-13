import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Define Variables
URL = "https://www.saucedemo.com/inventory.html"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"
WAIT_TIME = 5

# List of products to add to cart
PRODUCT = [
    "add-to-cart-sauce-labs-backpack",
    "add-to-cart-sauce-labs-bike-light",
    "add-to-cart-sauce-labs-bolt-t-shirt",
    "add-to-cart-sauce-labs-fleece-jacket",
    "add-to-cart-sauce-labs-onesie",
    "add-to-cart-test.allthethings()-t-shirt-(red)"
]

# Initialize Chrome browser instance using Selenium WebDriver
driver = webdriver.Chrome()

# Navigate to the login page of Sauce Demo
driver.get(URL)
time.sleep(5)

# Perform Login
driver.find_element(By.ID,"user-name").send_keys(USERNAME)
time.sleep(WAIT_TIME)

driver.find_element(By.ID,"password").send_keys(PASSWORD)
time.sleep(WAIT_TIME)

driver.find_element(By.ID,"login-button").click()
time.sleep(WAIT_TIME)

# Add product to cart using a loop
for product_id in PRODUCT:
    driver.find_element(By.ID, product_id).click()
time.sleep(WAIT_TIME)

# Click on the burger menu
driver.find_element(By.ID,"react-burger-menu-btn").click()
time.sleep(WAIT_TIME)

# Click on Logout
driver.find_element(By.ID,"logout_sidebar_link").click()
time.sleep(WAIT_TIME)
