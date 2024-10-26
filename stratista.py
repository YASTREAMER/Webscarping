from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from time import sleep
import os
from random import randint
from uuid import uuid4

from const import *
from xpath import *


def statistaStart() -> None:

    driver = getDriver()
    newWindow(driver)

    filterLocation(driver)
    filterOperating(driver)
    filterIPO(driver)
    for xPathCompany in XPathCompanies:
        Sector = 0
        filterCompanies(driver, xPathCompany)
        randomUUID = uuid4()
        filepath = os.path.join(
            "ScrapedData/",
            f"links-{randomUUID}-{nameSector[Sector]}.txt",
        )
        scrapeStart(driver, filepath)
        Sector += 1

    sleep(1)
    driver.close()


def scrapeStart(driver, filepath) -> None:

    mult = 0
    NextpageAvailable = True

    with open(filepath, "w") as Linksfile:
        while (mult + 1) * 5000 <= Upperlimit:
            NextpageAvailable = True
            filerRevenue(driver, mult * 5000, (mult + 1) * 5000)
            i = 1
            for i in range(100):

                if not NextpageAvailable:
                    break
                NextpageAvailable = pageLimit(driver)

                links = scrapeLinks(driver)

                Linksfile.write(
                    f"The reveneue range is {mult*5000} to {(mult+1)*5000} :- \n"
                )

                for link in links:
                    Linksfile.write(link)
                    Linksfile.write("\n")
                try:
                    nextPage(driver)
                except:
                    print("End of page")
            mult += 1


def pageLimit(driver) -> bool:
    stringtext = driver.find_element(
        By.XPATH, "/html/body/div[4]/main/section[3]/div/form/div[4]/div/span"
    ).text
    # Removing the prefix
    stringtext = stringtext.removeprefix("Page: ")

    CurrentPage, LastPage = stringtext.split("/")
    CurrentPage = int(CurrentPage)
    LastPage = int(LastPage)

    if CurrentPage == LastPage:
        return False
    else:
        return True


def getDriver():

    # Initialize WebDriver
    driver = webdriver.Firefox()
    return driver


def newWindow(driver) -> None:
    # Login into Statista
    driver.get("https://www.statista.com/companies/search?queries%5B%5D=")
    sleep(8)
    # Checing the cookies
    driver.find_element(By.CSS_SELECTOR, "#onetrust-accept-btn-handler").click()
    sleep(4)


def filterIPO(driver) -> None:

    # Filter button
    WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "/html/body/div[4]/main/section[3]/div/form/div[2]/div/div/div[1]/button",
            )
        )
    )
    driver.find_element(
        By.XPATH,
        "/html/body/div[4]/main/section[3]/div/form/div[2]/div/div/div[1]/button",
    ).click()
    # IPO Filter
    WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "/html/body/div[4]/main/section[3]/div/form/div[7]/div[2]/div[2]/div[7]",
            )
        )
    )
    driver.find_element(
        By.XPATH,
        "/html/body/div[4]/main/section[3]/div/form/div[7]/div[2]/div[2]/div[7]",
    ).click()
    # Applying private companies filter
    WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "/html/body/div[4]/main/section[3]/div/form/div[7]/div[2]/div[2]/div[7]/div/fieldset/div/div/div/ul/li[1]",
            )
        )
    )
    driver.find_element(
        By.XPATH,
        "/html/body/div[4]/main/section[3]/div/form/div[7]/div[2]/div[2]/div[7]/div/fieldset/div/div/div/ul/li[1]",
    ).click()
    # Applying the overall filters
    WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "/html/body/div[4]/main/section[3]/div/form/div[7]/div[2]/div[2]/div[7]/div/fieldset/div/div/div/div[2]/button[2]",
            )
        )
    )
    driver.find_element(
        By.XPATH,
        "/html/body/div[4]/main/section[3]/div/form/div[7]/div[2]/div[2]/div[7]/div/fieldset/div/div/div/div[2]/button[2]",
    ).click()


def filterOperating(driver) -> None:

    # Filter button
    WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "/html/body/div[4]/main/section[3]/div/form/div[2]/div/div/div[1]/button",
            )
        )
    )
    driver.find_element(
        By.XPATH,
        "/html/body/div[4]/main/section[3]/div/form/div[2]/div/div/div[1]/button",
    ).click()
    # Operating Status
    WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "/html/body/div[4]/main/section[3]/div/form/div[7]/div[2]/div[2]/div[8]",
            )
        )
    )
    driver.find_element(
        By.XPATH,
        "/html/body/div[4]/main/section[3]/div/form/div[7]/div[2]/div[2]/div[8]",
    ).click()
    # Active companies
    WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "/html/body/div[4]/main/section[3]/div/form/div[7]/div[2]/div[2]/div[8]/div/fieldset/div/div/div/ul/li[1]",
            )
        )
    )
    driver.find_element(
        By.XPATH,
        "/html/body/div[4]/main/section[3]/div/form/div[7]/div[2]/div[2]/div[8]/div/fieldset/div/div/div/ul/li[1]",
    ).click()
    # Applying filters
    WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "/html/body/div[4]/main/section[3]/div/form/div[7]/div[2]/div[2]/div[8]/div/fieldset/div/div/div/div[2]/button[2]",
            )
        )
    )
    driver.find_element(
        By.XPATH,
        "/html/body/div[4]/main/section[3]/div/form/div[7]/div[2]/div[2]/div[8]/div/fieldset/div/div/div/div[2]/button[2]",
    ).click()


def filterLocation(driver) -> None:  # This function filters the location to USA only

    WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "/html/body/div[4]/main/section[3]/div/form/div[2]/div/div/div[1]/button",
            )
        )
    )
    # Filter button
    driver.find_element(
        By.XPATH,
        "/html/body/div[4]/main/section[3]/div/form/div[2]/div/div/div[1]/button",
    ).click()

    WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "/html/body/div[4]/main/section[3]/div/form/div[7]/div[2]/div[2]/div[1]/div/fieldset/div/div/button/div",
            )
        )
    )
    # Location Filter
    driver.find_element(
        By.XPATH,
        "/html/body/div[4]/main/section[3]/div/form/div[7]/div[2]/div[2]/div[1]/div/fieldset/div/div/button/div",
    ).click()

    WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "/html/body/div[4]/main/section[3]/div/form/div[7]/div[2]/div[2]/div[1]/div/fieldset/div/div/div/div[2]/div/input",
            )
        )
    )

    driver.find_element(
        By.XPATH,
        "/html/body/div[4]/main/section[3]/div/form/div[7]/div[2]/div[2]/div[1]/div/fieldset/div/div/div/div[2]/div/input",
    ).send_keys("United State")

    WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "/html/body/div[4]/main/section[3]/div/form/div[7]/div[2]/div[2]/div[1]/div/fieldset/div/div/div/ul/li[2]",
            )
        )
    )

    # The Check box
    driver.find_element(
        By.XPATH,
        "/html/body/div[4]/main/section[3]/div/form/div[7]/div[2]/div[2]/div[1]/div/fieldset/div/div/div/ul/li[2]",
    ).click()

    WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "/html/body/div[4]/main/section[3]/div/form/div[7]/div[2]/div[2]/div[1]/div/fieldset/div/div/div/div[3]/button[2]",
            )
        )
    )
    # Apply
    driver.find_element(
        By.XPATH,
        "/html/body/div[4]/main/section[3]/div/form/div[7]/div[2]/div[2]/div[1]/div/fieldset/div/div/div/div[3]/button[2]",
    ).click()


def filterCompanies(driver, xPathCompany) -> None:

    # Applying the agriculture filter
    WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "/html/body/div[4]/main/section[3]/div/form/div[2]/div/div/div[1]/button",
            )
        )
    )
    # Filter button
    driver.find_element(
        By.XPATH,
        "/html/body/div[4]/main/section[3]/div/form/div[2]/div/div/div[1]/button",
    ).click()

    WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "/html/body/div[4]/main/section[3]/div/form/div[7]/div[2]/div[2]/div[2]/div/div/div/button/div",
            )
        )
    )
    # Industry Filter
    driver.find_element(
        By.XPATH,
        "/html/body/div[4]/main/section[3]/div/form/div[7]/div[2]/div[2]/div[2]/div/div/div/button/div",
    ).click()

    WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, xPathCompany))
    )
    # Agriculture
    driver.find_element(
        By.XPATH,
        xPathCompany,
    ).click()

    WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "/html/body/div[4]/main/section[3]/div/form/div[7]/div[2]/div[2]/div[2]/div/div/div/div/div[3]/button[2]",
            )
        )
    )
    # Apply the filter
    driver.find_element(
        By.XPATH,
        "/html/body/div[4]/main/section[3]/div/form/div[7]/div[2]/div[2]/div[2]/div/div/div/div/div[3]/button[2]",
    ).click()


def filerRevenue(driver, lower, upper) -> None:

    # Filter
    WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "/html/body/div[4]/main/section[3]/div/form/div[2]/div/div/div[1]/button",
            )
        )
    )
    driver.find_element(
        By.XPATH,
        "/html/body/div[4]/main/section[3]/div/form/div[2]/div/div/div[1]/button",
    ).click()

    # Revenue Filter
    WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "/html/body/div[4]/main/section[3]/div/form/div[7]/div[2]/div[2]/div[4]/div/fieldset/div/div/button",
            )
        )
    )
    driver.find_element(
        By.XPATH,
        "/html/body/div[4]/main/section[3]/div/form/div[7]/div[2]/div[2]/div[4]/div/fieldset/div/div/button",
    ).click()

    # Clearning the revenue filter
    WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "/html/body/div[4]/main/section[3]/div/form/div[7]/div[2]/div[2]/div[4]/div/fieldset/div/div/div/div[2]/input[2]",
            )
        )
    )
    driver.find_element(
        By.XPATH,
        "/html/body/div[4]/main/section[3]/div/form/div[7]/div[2]/div[2]/div[4]/div/fieldset/div/div/div/div[2]/input[2]",
    ).clear()

    # Renvenue Lower Limit
    WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "/html/body/div[4]/main/section[3]/div/form/div[7]/div[2]/div[2]/div[4]/div/fieldset/div/div/div/div[2]/input[1]",
            )
        )
    )
    driver.find_element(
        By.XPATH,
        "/html/body/div[4]/main/section[3]/div/form/div[7]/div[2]/div[2]/div[4]/div/fieldset/div/div/div/div[2]/input[1]",
    ).clear()

    # Revenue Upper limit
    WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "/html/body/div[4]/main/section[3]/div/form/div[7]/div[2]/div[2]/div[4]/div/fieldset/div/div/div/div[2]/input[2]",
            )
        )
    )
    driver.find_element(
        By.XPATH,
        "/html/body/div[4]/main/section[3]/div/form/div[7]/div[2]/div[2]/div[4]/div/fieldset/div/div/div/div[2]/input[2]",
    ).send_keys(upper)

    # Renvenue Lower Limit
    WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "/html/body/div[4]/main/section[3]/div/form/div[7]/div[2]/div[2]/div[4]/div/fieldset/div/div/div/div[2]/input[1]",
            )
        )
    )
    driver.find_element(
        By.XPATH,
        "/html/body/div[4]/main/section[3]/div/form/div[7]/div[2]/div[2]/div[4]/div/fieldset/div/div/div/div[2]/input[1]",
    ).send_keys(lower)

    # Apply revenue filter
    WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "/html/body/div[4]/main/section[3]/div/form/div[7]/div[2]/div[2]/div[4]/div/fieldset/div/div/div/div[5]/button[2]",
            )
        )
    )
    driver.find_element(
        By.XPATH,
        "/html/body/div[4]/main/section[3]/div/form/div[7]/div[2]/div[2]/div[4]/div/fieldset/div/div/div/div[5]/button[2]",
    ).click()


def nextPage(driver) -> None:
    randomDelay = randint(3, 7)
    # Loading new page
    driver.find_element(
        By.XPATH, "/html/body/div[4]/main/section[3]/div/form/div[4]/div/button[3]"
    ).click()
    sleep(randomDelay)


def scrapeLinks(driver) -> list:
    # Have to add this delay so as to let the page load
    sleep(10)
    try:
        WebDriverWait(driver, 30).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "companyResults__td"))
        )
    except:
        print("Skip")

    linksStore = []
    # Finding all the link on the page
    links = driver.find_elements(By.TAG_NAME, "a")
    for link in links:
        # print(link.get_attribute("href"))
        isLinkClean = cleanLinks(link.get_attribute("href"))
        if isLinkClean:
            linksStore.append(link.get_attribute("href"))
    return linksStore


def cleanLinks(link: str) -> bool:

    if link[:37] == "https://www.statista.com/companies/c/":
        print(link)
        return True
    else:
        return False
