from requests.sessions import Session, session
# import selenium
from bs4 import BeautifulSoup
import requests

#importing the credentials
from cred import *

def main()-> None:
    login(username,password,https://www.searchfunder.com/bvr/ajaxdealmodalcontent/14-1)
    

def login(username, password, login_url)-> Session:
    session = requests.Session()
    login_data = {
        'username': username,
        'password': password
    }
    response = session.post(login_url, data=login_data)
    if response.ok:
        return session
    else:
        raise Exception("Login failed")

def scrape_page(session, url):
    response = session.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    # Extract data from the page
    # Example: data = soup.find_all('div', class_='data-class')
    return data

if __name__=="__main__":
    main()
