# Pip install selenium
from selenium import webdriver

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Go to the Pornhub page
driver.get("https://www.pornhub.com/")

# Find the "Sign Up" button and click it to disable it. 
signup_btn = driver.find_element_by_id("signupButton") 
signup_btn.click()

# ---------------------------------
# Github : github.com/AnonParsa
# Twitter : twitter.com/AnonParsa
# Discord : https://discord.gg/FEBCntyA
# ---------------------------------