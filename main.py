from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Specify the path to ChromeDriver
service = Service("/usr/local/bin/chromedriver")

def getdriver():
    # Set options to make browsing easier
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    
    # Exclude the automation control info
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")
    
    # Initialize the driver with the service and options
    driver = webdriver.Chrome(service=service, options=options)
    
    # Navigate to the webpage
    driver.get("http://automated.pythonanywhere.com")
    
    return driver

def main():
    driver = getdriver()
    element = driver.find_element(By.XPATH, "/html/body/div[1]/div/h1[1]")
    text = element.text
    driver.quit()  # Close the browser after use
    return text

print(main())
