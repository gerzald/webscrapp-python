from datetime import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from constant import *



def getDriverService(url_path, userAgent):
    ser = Service(url_path)

    firefoxOptions = Options()
    firefoxOptions.set_preference('general.useragent.override', userAgent)
    driver = webdriver.Firefox(service=ser, options=firefoxOptions)
    return driver



def getJobs():
    return ''


def getMainList():
    return ''


def scrapp_jobs():
    netflix_jobs()
    return ''

def netflix_jobs():
    driver = getDriverService(DRIVER_PATH, USER_AGENT)

    driver.get('https://jobs.netflix.com/search')
    driver.maximize_window()
    time.sleep(10)

    teams_options_section = driver.find_elements(By.CSS_SELECTOR, 'div.css-rdywoq')[0]
    locations_options_section = driver.find_elements(By.CSS_SELECTOR, 'div.css-rdywoq')[1]

    team_options = teams_options_section.find_elements(By.CSS_SELECTOR, 'li.css-1flyy90')
    
    for to in range(len(team_options)):
        team_input = team_options[to].find_element(By.TAG_NAME, 'input')
        team_name = team_input.get_attribute('name')

        team_input_2 = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"')]")))
        print(team_name)

    driver.quit()

scrapp_jobs()