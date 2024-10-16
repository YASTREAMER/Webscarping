from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

import os

# import the credentials


def getDriver():

    # Initialize WebDriver
    driver = webdriver.Firefox()
    return driver


def loginAuth(driver, username, password) -> None:
    # Navigate to website
    driver.get(
        "https://login.statista.com/u/login?state=hKFo2SBna0M3anV3R1JJWS1DbzlORXhBaDZDcEdvdXdnOThON6Fur3VuaXZlcnNhbC1sb2dpbqN0aWTZIGRxTzRoTGZNME4tdG5xb3Q3b29takpQdWhMZUZOMll2o2NpZNkgeGpWRjBGRldGUE9jRzdYSk84QzBYbGVlUlBsbFVGZkk"
    )

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
    driver.find_element(By.NAME, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.XPATH, "/html/body/main/section/div/div/div/form/div[4]/button").click()

    # Switch back to main window after login
    driver.switch_to.window(main_window)
    sleep(5)
