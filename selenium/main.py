#!/usr/bin/env python3

import json
import html
import time

from pprint import pprint

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait 

def save_json(data):
    pprint(data)
    with open('output.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def get_vacancies(url, next_page_limit):
    print('Opening the page ' + url)
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(url)

    cookie_button = WebDriverWait(driver, 5).until(lambda x: x.find_element(by=By.ID, value='CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll'))
    cookie_button.click()

    time.sleep(1) 

    for i in range(next_page_limit):
        print(f'Clicking next page no. {i}')
        next_button_div = WebDriverWait(driver, 20).until(lambda x: x.find_element(by=By.CLASS_NAME, value='jobCardList_btn'))
        next_button = next_button_div.find_element(by=By.CLASS_NAME, value='fwp-load-more')
        ActionChains(driver).move_to_element(next_button).perform()
        time.sleep(1) 
        next_button.click()

    time.sleep(5) # wait to load more jobs

    jobs = []

    try:
        job_cards = driver.find_elements(by=By.CLASS_NAME, value='jobCard')
        for card in job_cards:
            job_title = card.find_element(by=By.CLASS_NAME, value='jobCard_title').text
            job_link = card.find_element(by=By.CLASS_NAME, value='jobCard_link').get_attribute('href')
            jobs.append({"Title": html.unescape(job_title), "Link": job_link})
    except Exception as e:
        print(f"Error fetching job details: {e}")

    time.sleep(1)
    print(f'Got {len(jobs)} jobs')
    driver.quit()
    return jobs

if __name__ == '__main__':
    url = 'https://www.lejobadequat.com/emplois'
    max_next_pages = 1

    vacancies = get_vacancies(url, max_next_pages)
    save_json(vacancies)

