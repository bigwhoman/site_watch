import time
import winsound
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import os


# to start the file from python
def beeep():
    frequency = 2500  # Set Frequency To 2500 Hertz
    duration = 3000  # Set Duration To 1000 ms == 1 second
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
    driver.get("https://www.tiwall.com/showcase?filters=s:music")
    while True:
        try:
            time.sleep(5)
            driver.find_element(by=By.CSS_SELECTOR, value='[data-saleurn="/s/homayoun.shajarian"]')
            os.system("start task_done.mp3")
            exit_prog(driver)
            return
        except Exception as e:
            if not str(e).find("unable to locate"):
                print(e)
                exit_prog(driver)
                return
            print("there has been an exception :: ",str(e))
            driver.refresh()


site_scrape()
