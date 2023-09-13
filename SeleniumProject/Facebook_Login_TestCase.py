import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait




# initialize the Chrome driver
# driver = webdriver.Chrome("C://Users\KUNAL\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# head to github login page
driver.get("http://www.facebook.com")
# driver.fullscreen_window()
driver.maximize_window()


# Search & Enter the Email or Phone field & Enter Password

username = driver.find_element(By.ID,"email")
username.send_keys("you@email.com")

password = driver.find_element(By.ID,"pass")
password.send_keys("yourpassword")

#click on login button
login   = driver.find_element(By.NAME,"login")
login.click()

time.sleep(12)

driver.quit()