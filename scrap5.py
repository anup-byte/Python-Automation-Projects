from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

# Specify the path to ChromeDriver
service = Service("/usr/local/bin/chromedriver")

def cleanText(text):
    """Extract only the temperature from text"""
    output = float(text.split(": ")[1])
    return output

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
    driver.get("http://automated.pythonanywhere.com/login/")
    return driver

def cleanText(text):
    """Extract only the temperature from text"""
    output = float(text.split(": ")[1])
    return output

def main():
    driver = getdriver()
    driver.find_element(by="id", value="id_username").send_keys("automated")
    time.sleep(2)
    driver.find_element(by="id", value="id_password").send_keys("automatedautomated" + Keys.RETURN)
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/nav/div/a").click()
    time.sleep(2)

    # Scrape the temperature value
    text = driver.find_element(By.XPATH, '/html/body/div[1]/div/h1[2]').text
    return cleanText(text)


print(main())
