# Working code for login
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

#import the credentials
from cred import *

def main() -> None:
    driver = getDriver()
    loginAuth(driver)
    dataText=scrapeUrl(driver,"https://www.searchfunder.com/bvr/ajaxdealmodalcontent/14-1")

    # Close WebDriver when done
    driver.quit()

def getDriver():

    # Initialize WebDriver
    driver = webdriver.Firefox()
    return driver

def loginAuth(driver) -> None:
    # Navigate to website
    driver.get("https://www.searchfunder.com/auth/login/")

    # Click on login button to open popup
    # driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div/div/div/form/div[4]/div/button').click()
    sleep(10)

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

def scrapeUrl(driver, url) -> list:
    # Navigate to website
    driver.get(url)
    data_elements = driver.find_elements(
        By.CLASS_NAME, "bvr-item"
    )  # Replace with the actual XPath of the data you want to scrape
    for element in data_elements:
        print(element.text)  # Print or process the scraped data as needed

    return data_elements

if __name__ == "__main__":
    main()
