import time
import winsound
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import os


# to start the file from python
def beeep():
    frequency = 2500  # Set Frequency To 2500 Hertz
    duration = 5000  # Set Duration To 1000 ms == 1 second
    winsound.Beep(frequency, duration)


def exit_prog(driver):
    beeep()
    driver.quit()
    return


def site_scrape():
    options = Options()
    options.headless = True
    options.add_argument("--window-size=1920,1200")
    driver = webdriver.Firefox()
    driver.get("")
    all_links = driver.find_element(by=By.CLASS_NAME, value='promo-desc')
    last = all_links.text
    while True:
        try:
            time.sleep(10)
            all_links = driver.find_element(by=By.CLASS_NAME, value='promo-desc')
            print(all_links.text)
            if last != driver.find_element(by=By.CLASS_NAME, value='promo-desc').text:
                os.system("start task_done.mp3")
                exit_prog(driver)
                return
            driver.refresh()
        except:
            os.system("start error_voice.mp3")
            exit_prog(driver)
            return


site_scrape()
