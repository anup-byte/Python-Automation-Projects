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
    driver.get("http://automated.pythonanywhere.com")
    return driver

def cleanText(text):
    """Extract only the temperature from text"""
    output = float(text.split(": ")[1])
    return output


def writeFile(text):
    """Write input text into a text file"""
    filename = f"{dt.now().strftime('%Y-%m-%d.%H-%M-%S')}.txt"
    with open(filename, 'w') as file:
        file.write(text)



def main():
    driver = getdriver()
    while True:
        time.sleep(2)
        element = driver.find_element(By.XPATH, '/html/body/div[1]/div/h1[2]')
        text = str(cleanText(element.text))
        writeFile(text)
    
main()