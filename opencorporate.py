# from bs4 import BeautifulSoup
# import os
# import time
# from playwright.sync_api import sync_playwright

# Set your credentials as environment variables
# import os
# os.environ['USERNAME'] = 'masoob0085@gmail.com'
# os.environ['PASSWORD'] = 'Masoob#123'

# def login_auth(page):
#     # Navigate to the login page
#     page.goto("https://opencorporates.com/users/sign_in")
    
#     # Fetch credentials from environment variables
#     username = os.getenv("USERNAME")
#     password = os.getenv("PASSWORD")

#     # Wait for the email input field and fill in the login details
#     page.fill("#user_email", username)
#     page.fill("#user_password", password)

#     # Click the "Sign in" button
#     page.click('button[name="submit"]')

#     # Wait for some time to ensure login completes (can adjust this time)
#     time.sleep(5)

# def get_company_details(page, url):
#     # Navigate to the company page
#     page.goto(url)
    
#     # Wait for the page to fully load
#     time.sleep(5)

#     # Get the page content and parse it
#     html = page.content()
#     soup = BeautifulSoup(html, 'html.parser')

#     try:
#         # Extract company details
#         company_name = soup.select_one('h1[class="wrapping_heading fn org"]').get_text(strip=True) if soup.select_one('h1[class="wrapping_heading fn org"]') else "N/A"
#         company_number = soup.select_one('dd[class="company_number"]').get_text(strip=True) if soup.select_one('dd[class="company_number"]') else "N/A"
#         status = soup.select_one('dd[class="status"]').get_text(strip=True) if soup.select_one('dd[class="status"]') else "N/A"
#         incorporation_date = soup.select_one('dd[class="incorporation_date"]').get_text(strip=True) if soup.select_one('dd[class="incorporation_date"]') else "N/A"
#         company_type = soup.select_one('dd[class="company_type"]').get_text(strip=True) if soup.select_one('dd[class="company_type"]') else "N/A"
#         jurisdiction = soup.select_one('dd[class="jurisdiction"]').get_text(strip=True) if soup.select_one('dd[class="jurisdiction"]') else "N/A"
#         agent_name = soup.select_one('dd[class="agent_name"]').get_text(strip=True) if soup.select_one('dd[class="agent_name"]') else "N/A"
#         agent_address = soup.select_one('dd[class="agent_address"]').get_text(strip=True) if soup.select_one('dd[class="agent_address"]') else "N/A"

#         # Extract address and phone details
#         address_div = soup.find('div', {'id': 'company_addresses'})
#         if address_div:
#             addresses = address_div.select('p.description')
#             head_office_address = addresses[0].get_text(strip=True) if len(addresses) > 0 else "N/A"
#             mailing_address = addresses[1].get_text(strip=True) if len(addresses) > 1 else "N/A"
#             second_head_office_address = addresses[2].get_text(strip=True) if len(addresses) > 2 else "N/A"
#         else:
#             head_office_address = mailing_address = second_head_office_address = "N/A"

#         phone_div = soup.find('div', {'id': 'telephone_numbers'})
#         if phone_div:
#             phone_numbers = phone_div.select('p.description')
#             phone_number = phone_numbers[0].get_text(strip=True) if len(phone_numbers) > 0 else "N/A"
#         else:
#             phone_number = "N/A"

#         # Print all company details
#         print(f"Company Name: {company_name}")
#         print(f"Company Number: {company_number}")
#         print(f"Status: {status}")
#         print(f"Incorporation Date: {incorporation_date}")
#         print(f"Company Type: {company_type}")
#         print(f"Jurisdiction: {jurisdiction}")
#         print(f"Agent Name: {agent_name}")
#         print(f"Agent Address: {agent_address}")
#         print(f"Head Office Address: {head_office_address}")
#         print(f"Mailing Address: {mailing_address}")
#         print(f"Second Head Office Address: {second_head_office_address}")
#         print(f"Phone Number: {phone_number}")

#     except Exception as e:
#         print(f"Error retrieving company details: {e}")

# def main():
#     # Start Playwright
#     with sync_playwright() as p:
#         # Use the Chromium browser in headless mode
#         browser = p.chromium.launch(headless=True)
#         page = browser.new_page()
        
#         try:
#             # Log in to the site
#             login_auth(page)
            
#             # URL of the company page to scrape
#             company_url = "https://opencorporates.com/companies/us_fl/L20000102453"
            
#             # Get company details
#             get_company_details(page, company_url)
        
#         finally:
#             # Close the browser
#             browser.close()

# # Run the main function
# main()

import os
import time
import csv
import pandas as pd
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
os.environ['USERNAME'] = 'masoob0085@gmail.com'
os.environ['PASSWORD'] = 'Masoob#123'
def login_auth(browser):
    # Navigate to the login page
    page = browser.new_page()
    page.goto("https://opencorporates.com/users/sign_in")
    
    # Fetch credentials from environment variables
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")

    # Wait until the email input field is present
    page.fill("#user_email", username)
    page.fill("#user_password", password)

    # Click the "Sign in" button
    page.click("button[name='submit']")

    # Wait for login to complete
    page.wait_for_timeout(10000)  # Wait for 10 seconds

    return page

def get_company_details(page, url):
    # Navigate to the company page
    page.goto(url)

    # Wait for the page to fully load
    page.wait_for_timeout(10000)  # Wait for 10 seconds

    # Get the page source and parse it
    html = page.content()
    soup = BeautifulSoup(html, 'html.parser')

    # Extract company details with safe access
    company_name = soup.select_one('h1.wrapping_heading.fn.org').get_text(strip=True) if soup.select_one('h1.wrapping_heading.fn.org') else "N/A"
    company_number = soup.select_one('dd.company_number').get_text(strip=True) if soup.select_one('dd.company_number') else "N/A"
    status = soup.select_one('dd.status').get_text(strip=True) if soup.select_one('dd.status') else "N/A"
    incorporation_date = soup.select_one('dd.incorporation_date').get_text(strip=True) if soup.select_one('dd.incorporation_date') else "N/A"
    company_type = soup.select_one('dd.company_type').get_text(strip=True) if soup.select_one('dd.company_type') else "N/A"
    jurisdiction = soup.select_one('dd.jurisdiction').get_text(strip=True) if soup.select_one('dd.jurisdiction') else "N/A"
    agent_name = soup.select_one('dd.agent_name').get_text(strip=True) if soup.select_one('dd.agent_name') else "N/A"
    agent_address = soup.select_one('dd.agent_address').get_text(strip=True) if soup.select_one('dd.agent_address') else "N/A"

    # Extract address and phone number details with safe access
    address_div = soup.find('div', {'id': 'company_addresses'})
    if address_div:
        addresses = address_div.select('p.description')
        head_office_address = addresses[0].get_text(strip=True) if len(addresses) > 0 else "N/A"
        mailing_address = addresses[1].get_text(strip=True) if len(addresses) > 1 else "N/A"
        second_head_office_address = addresses[2].get_text(strip=True) if len(addresses) > 2 else "N/A"
    else:
        head_office_address = mailing_address = second_head_office_address = "N/A"

    phone_div = soup.find('div', {'id': 'telephone_numbers'})
    if phone_div:
        phone_numbers = phone_div.select('p.description')
        phone_number = phone_numbers[0].get_text(strip=True) if len(phone_numbers) > 0 else "N/A"
    else:
        phone_number = "N/A"
    
    # Return all company details as a dictionary
    return {
        "Company Name": company_name,
        "Company Number": company_number,
        "Status": status,
        "Incorporation Date": incorporation_date,
        "Company Type": company_type,
        "Jurisdiction": jurisdiction,
        "Agent Name": agent_name,
        "Agent Address": agent_address,
        "Head Office Address": head_office_address,
        "Mailing Address": mailing_address,
        "Second Head Office Address": second_head_office_address,
        "Phone Number": phone_number,
        "Company URL": url
    }

def main():
    with sync_playwright() as p:
        # Launch a browser
        browser = p.chromium.launch(headless=True)  # Use headless mode for Colab
        page = login_auth(browser)
        
        # Read Excel file containing company URLs
        df = pd.read_excel('opencorporates.xlsx')
        
        # Create a list to store all company details
        all_company_details = []
        
        # Iterate over each URL in the Excel file
        for index, row in df.iterrows():
            company_url = row['company_search_result href']
            print(f"Fetching details for: {company_url}")
            
            # Fetch the company details and add to the list
            try:
                company_details = get_company_details(page, company_url)
                all_company_details.append(company_details)
            except Exception as e:
                print(f"Error retrieving details for {company_url}: {e}")
        
        # Write the results to a CSV file
        keys = all_company_details[0].keys()
        with open('company_details.csv', 'w', newline='', encoding='utf-8') as output_file:
            dict_writer = csv.DictWriter(output_file, fieldnames=keys)
            dict_writer.writeheader()
            dict_writer.writerows(all_company_details)

        print("Data written to company_details_2.csv successfully.")
        
        # Close the browser
        browser.close()

# Run the main function
main()
