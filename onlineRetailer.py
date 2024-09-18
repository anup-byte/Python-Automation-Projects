from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from datetime import datetime as dt



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
    driver.get("https://titan22.com/account/login?return_url=%2Faccount")
    return driver


def main():
    driver = getdriver()
    driver.find_element(by="id", value="CustomerEmail").send_keys("aikipaathshala@gmail.com")
    time.sleep(2)
    driver.find_element(by="id", value="CustomerPassword").send_keys("Anup@anup" + Keys.RETURN)
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="shopify-section-footer"]/section/div/div[1]/div[1]/div[1]/nav/ul/li[1]/a').click()
    print(driver.current_url)


print(main())    

