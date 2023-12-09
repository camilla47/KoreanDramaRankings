from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException

import time
import pandas as pd

# THIS CODE WILL LOOP THROUGH ALL 20 TITLE ELEMENTS AND GRAB THE GENRES AND PUT THEM INTO A LIST!!!!!

def scrape_page2(titles, genres, watchers, network, url):
    ## create the driver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.set_page_load_timeout(10)
    
    ## get the url
    try:
        driver.get(url)
    except TimeoutException as error:
        print("timeout error- getting url")   
    #print('Starting Driver')

    ## find all the show titles
    title_elements = driver.find_elements(by=By.CSS_SELECTOR, value='h6.title a')

    # iterate through shows to scrape info
    for index in range(0, len(title_elements), 2):
        ## re-find the element in each iteration
        title_elements = driver.find_elements(By.CSS_SELECTOR, 'h6.title a')
        element = title_elements[index]   
        print(element.text)
        titles.append(element.text)

        ## scroll to the title, then click
        #print("Clicking on the title...")
        try:
            driver.execute_script("arguments[0].scrollIntoView();", element)
            driver.execute_script("window.scrollBy(0, arguments[0]);", -100)
            time.sleep(1)
            element.click()
        except TimeoutException as error:
            print("Timeout error- clicking title ")   
        
        # scrape the genre
        #print("Searching for genre...")
        try:
            genres_section = driver.find_element(By.CLASS_NAME, 'show-genres')
            #print(genres_section.text)        
            genres.append(genres_section.text)
        except:
            print("Genre not found")
            genres.append('na')

        ## scrape the network
        #print("Searching for network...")
        try:
            network_elements = driver.find_elements(By.CLASS_NAME, "p-a-0")
            if network_elements:
                # Loop through all elements with class "p-a-0"
                for element in network_elements:
                    # Check if the element contains text related to the original network
                    if "original network" in element.text.lower():
                        #print(element.text)
                        network.append(element.text)
                        break  # Exit loop after finding the first occurrence
                else:
                    print("No elements with 'original network' text found")
                    network.append('na')
            else:
                print("No elements with class 'p-a-0' found")
        except NoSuchElementException:
            print("Network elements not found")

        ## scrape the watchers
        #print("Searching for watchers...")
        try:
            genres_elements = driver.find_elements(By.CLASS_NAME, "hfs")
            watcher_int = int(genres_elements[1].text.split(' ')[-1].replace(',', ''))
            #print(watcher_int)
            watchers.append(watcher_int)
        except NoSuchElementException:
            print("Watchers not found")
            watchers.append('0')


        # go back to title list
        #print("going back to main...")
        try:
            driver.execute_script("window.history.go(-1)")
        except TimeoutException as error:
            print("timeout error - going back")