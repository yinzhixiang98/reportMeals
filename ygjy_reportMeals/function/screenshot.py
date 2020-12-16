from time import sleep
import os
from selenium import webdriver     #从selenium库导入webdirver

def screenshot(save_path):
    global driver
    chrome_path = "D:/YG Soft/YGAUTOAPPIUM/chromedriver.exe"
    os.environ['webdriver.chrome.driver'] = chrome_path
    driver = webdriver.Chrome(chrome_path)
    sleep(1)
    driver.get("file:///E:\SummaryReport.html")
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.save_screenshot(save_path)
    driver.close()

if __name__ == "__main__":
    screenshot("E:\screenshot.png")