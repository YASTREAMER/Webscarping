from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd

import os

# import the credentials
from cred import *

def searchfunderStart() -> None:

    for credential in credentials:
        driver = getDriver()
        loginAuth(driver, credential[0], credential[1])
        links, filepath, startingpoint = fetchUrl(scrapeNum)
        dataText = scrapeUrl(driver, links, filepath, startingpoint)

        # Close WebDriver when done
        driver.quit()


def getDriver():

    # Initialize WebDriver
    driver = webdriver.Firefox()
    return driver


def loginAuth(driver, username, password) -> None:
    # Navigate to website
    driver.get("https://www.searchfunder.com/auth/login/")

    # Click on login button to open popup
    sleep(7)

    # Switch to login popup window
    main_window = driver.current_window_handle
    for handle in driver.window_handles:
        if handle != main_window:
            login_window = handle
            driver.switch_to.window(login_window)
            break

    # Enter credentials in popup window
    driver.find_element(
        By.XPATH, "/html/body/div[3]/div/div[2]/div/div/div/form/div[1]/div/input"
    ).send_keys(username)
    driver.find_element(
        By.XPATH, "/html/body/div[3]/div/div[2]/div/div/div/form/div[2]/div/input"
    ).send_keys(password)
    driver.find_element(
        By.XPATH, "/html/body/div[3]/div/div[2]/div/div/div/form/div[4]/div/button"
    ).click()

    # Switch back to main window after login
    driver.switch_to.window(main_window)
    sleep(5)


def scrapeUrl(driver, urls, filepath, startingpoint) -> None:
    # loading the dataframe
    df = pd.read_csv("transcationLink/Links.csv")
    with open(filepath, "w") as file:
        for url in urls:
            print(url)
            # Navigate to website
            driver.get(url)
            sleep(5) #Let the URL load
            data_elements = driver.find_elements(
                By.CLASS_NAME, "bvr-item"
            )  # Replace with the class name of the data you want to scrape
            file.write(f"The Url is {url}\n")
            for element in data_elements:
                file.write(element.text)
                file.write("\n")
            # Save the scaped link as scraped
            df.loc[startingpoint, "Scraped"] = "yes"
            startingpoint += 1

    file.close()
    df.to_csv("transcationLink/Links.csv")


def createFile(name) -> str:
    # Create a new dir if the dir does not exist
    if not os.path.exists("ScrapedData"):
        os.mkdir("ScrapedData/")
    # The file name if set as ScrapedData/Data-Range. The range tells the range in which the data has been extracted.
    filepath = os.path.join("ScrapedData/", f"Data{name}-{name+scrapeNum}.txt")
    with open(filepath, "w") as file:
        pass
    file.close()
    return filepath


def fetchUrl(limit) -> tuple:
    df = pd.read_csv("transcationLink/Links.csv")
    Size = df.shape
    links = []
    startingpoint = 0
    j = 0

    for i in range(Size[0]):

        if df.loc[i, "Scraped"] == "yes":
            startingpoint = i
            continue
        else:
            # Create a file for storing the data if the file does not exists
            if j == 0:
                filepath = createFile(i)
            j += 1
            links.append(df.loc[i, "Combined"])

        if j >= limit:
            print(
                f"The max number of links have been reached. The number of links that have been reach is {i+1}"
            )
            break
    return links, filepath, startingpoint
