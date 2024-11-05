from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from time import sleep
import os
from uuid import uuid4
from dotenv import load_dotenv
import boto3
from botocore.exceptions import NoCredentialsError

from const import *
import cred
from xpath import *
from cred import *


load_dotenv()


def uploadToS3(local_file, bucket_name, s3_folder, s3_file_name):
    # Get AWS credentials from environment variables
    aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
    aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")

    # Initialize S3 client with credentials
    s3 = boto3.client(
        "s3",
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
    )

    try:
        s3.upload_file(local_file, bucket_name, f"{s3_folder}/{s3_file_name}")
        print(f"Upload Successful: {s3_folder}/{s3_file_name}")
    except FileNotFoundError:
        print("The file was not found")
    except NoCredentialsError:
        print("Credentials not available")


def filterAll(driver) -> None:

    filterLocation(driver)
    sleep(1)
    filterOperating(driver)
    sleep(1)
    filterIPO(driver)


def statistaStart() -> None:

    driver = getDriver()
    newWindow(driver)
    input("There is your time to set the download location \n")

    filterAll(driver)
    removeFiles()

    for xPathCompany in XPathCompanies:
        # Sector = 0
        filterCompanies(driver, xPathCompany)
        startDownload(driver)
        # randomUUID = uuid4()
        # filepath = os.path.join(
        #     "ScrapedData/",
        #     f"links-{randomUUID}-{nameSector[Sector]}.txt",
        # )
        # scrapeStart(driver, filepath)
        # Sector += 1
        resetComapnies(driver)
        uploadStart()
        print("Finished Uploading")
        removeFiles()
        print("Deleted files locally")

    sleep(1)
    driver.close()


def removeFiles() -> None:

    for file in os.listdir("DownloadFolder"):
        tempFile = os.path.join("DownloadFolder", file)
        os.remove(tempFile)


def scrapeStart(driver, filepath) -> None:

    with open(filepath, "w") as Linksfile:
        while (mult + 1) * Increament <= Uupperlimit:
            NextpageAvailable = True
            print(mult * Increament, (mult + 1) * Increament)
            sleep(20)
            filterRevenue(driver, mult * Increament, (mult + 1) * Increament)
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


def filterRevenue(driver, lower, upper) -> None:

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
    driver.find_element(
        By.XPATH,
        "/html/body/div[4]/main/section[3]/div/form/div[7]/div[2]/div[2]/div[4]/div/fieldset/div/div/div/div[2]/input[1]",
    ).send_keys(lower)

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
    # randomDelay = randint(3, 5)
    # Loading new page
    driver.find_element(
        By.XPATH, "/html/body/div[4]/main/section[3]/div/form/div[4]/div/button[3]"
    ).click()


def startDownload(driver):
    mult = Lowerlimit / Increament
    NextpageAvailable = True
    while ((mult + 1) * Increament) <= Upperlimit:
        NextpageAvailable = True
        print((mult * Increament), ((mult + 1) * Increament))
        filterRevenue(driver, (mult * Increament), ((mult + 1) * Increament))
        i = 1
        for i in range(100):
            if not NextpageAvailable:
                break
            NextpageAvailable = pageLimit(driver)
            downloadCsv(driver)
            try:
                nextPage(driver)
            except:
                print("End of page")
        mult += 1


def downloadCsv(driver) -> None:

    WaitCss(driver)
    driver.find_element(
        By.XPATH,
        "/html/body/div[4]/main/section[3]/div/form/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/div/a",
    ).click()


def uploadStart() -> None:

    bucket_name = cred.bucket_name
    s3_folder = cred.s3_folder

    for file in os.listdir("DownloadFolder"):

        # Generating a new UUID
        randomUUID = uuid4()
        local_file = os.path.join("DownloadFolder", file)
        s3_file_name = f"file-{randomUUID}"
        uploadToS3(local_file, bucket_name, s3_folder, s3_file_name)


def scrapeLinks(driver) -> list:
    # Have to add this delay so as to let the page load
    WaitCss(driver)
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


def WaitCss(driver):
    # This is used to lead the page load
    WebDriverWait(driver, 30).until(
        EC.invisibility_of_element_located(
            (
                By.XPATH,
                "/html/body/div[4]/main/section[3]/div/form/div[3]/div[2]/div/div/div[1]/div",
            )
        )
    )


def resetComapnies(driver):

    WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "/html/body/div[4]/main/section[3]/div/form/div[2]/div/div/div[1]/button",
            )
        )
    )
    # Filter XPath
    driver.find_element(
        By.XPATH,
        "/html/body/div[4]/main/section[3]/div/form/div[2]/div/div/div[1]/button",
    ).click()

    WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "/html/body/div[4]/main/section[3]/div/form/div[7]/div[2]/div[2]/div[2]/div/div/div/button",
            )
        )
    )
    # Industries XPath
    driver.find_element(
        By.XPATH,
        "/html/body/div[4]/main/section[3]/div/form/div[7]/div[2]/div[2]/div[2]/div/div/div/button",
    ).click()

    WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "/html/body/div[4]/main/section[3]/div/form/div[7]/div[2]/div[2]/div[2]/div/div/div/div/div[3]/button[1]",
            )
        )
    )
    # Reset XPath
    driver.find_element(
        By.XPATH,
        "/html/body/div[4]/main/section[3]/div/form/div[7]/div[2]/div[2]/div[2]/div/div/div/div/div[3]/button[1]",
    ).click()

    WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "/html/body/div[4]/main/section[3]/div/form/div[7]/div[2]/div[2]/div[2]/div/div/div/div/div[3]/button",
            )
        )
    )
    # Apply Xpath
    driver.find_element(
        By.XPATH,
        "/html/body/div[4]/main/section[3]/div/form/div[7]/div[2]/div[2]/div[2]/div/div/div/div/div[3]/button",
    ).click()


def cleanLinks(link: str) -> bool:

    if link[:37] == "https://www.statista.com/companies/c/":
        print(link)
        return True
    else:
        return False
