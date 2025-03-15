import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Define Variables
URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"
WAIT_TIME = 5

# Initialize Chrome browser instance using Selenium WebDriver
driver = webdriver.Chrome()

# Navigate to the login page of Sauce Demo
driver.get(URL)
time.sleep(WAIT_TIME) # Wait for page to load

# Maximize window
driver.maximize_window()

# Define Elements as Variables
Username = driver.find_element(By.ID,"user-name")
Password = driver.find_element(By.ID,"password")
Login = driver.find_element(By.ID,"login-button")

# Perform Login
Username.send_keys(USERNAME)
time.sleep(WAIT_TIME)

Password.send_keys(PASSWORD)
time.sleep(WAIT_TIME)

Login.click()
time.sleep(WAIT_TIME)

# Define Menu and Logout buttons
menu = driver.find_element(By.ID,"react-burger-menu-btn")
Logout = driver.find_element(By.ID,"logout_sidebar_link")

# List of products to add to cart
PRODUCT = [
    "add-to-cart-sauce-labs-backpack",
    "add-to-cart-sauce-labs-bike-light",
    "add-to-cart-sauce-labs-bolt-t-shirt",
    "add-to-cart-sauce-labs-fleece-jacket",
    "add-to-cart-sauce-labs-onesie",
    "add-to-cart-test.allthethings()-t-shirt-(red)"
]

# Add product to cart using a loop
for product_id in PRODUCT:
    driver.find_element(By.ID, product_id).click()
time.sleep(WAIT_TIME)

# Click on the burger menu
menu.click()
time.sleep(WAIT_TIME)

# Click on Logout
Logout.click()
time.sleep(WAIT_TIME)

# Quit browser
driver.quit()
