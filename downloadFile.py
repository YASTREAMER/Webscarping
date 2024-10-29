from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import os


def mainDownload() -> None:
    driver = getDriver()


def getName(driver):
    fileName = os.listdir()
    for file in fileName:
        links = cleanLink(file)
        for link in links:
            downloadXlsx(driver,link)


def cleanLink(file) -> list:
    links = []
    for line in file:
        if line[:37] == "https://www.statista.com/companies/c/":
            line = line.removesuffix("\n")
            links.append(line)

    return links


def getDriver():
    driver = webdriver.Firefox()
    driver.get("https://www.statista.com/companies/search?queries%5B%5D=")
    sleep(8)
    # Checing the cookies
    driver.find_element(By.CSS_SELECTOR, "#onetrust-accept-btn-handler").click()
    sleep(4)
    return driver


def downloadXlsx(driver, link):
    sleep(7)
    driver.get(link)
    sleep(7)
    driver.find_element(
        By.XPATH,
        "/html/body/div[4]/main/div[8]/section[1]/div/div[2]/div[1]/div/button",
    ).click()
