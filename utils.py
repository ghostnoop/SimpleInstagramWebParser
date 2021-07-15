import json
import platform
import time

from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pickle
from bs4 import BeautifulSoup
from selenium.common.exceptions import InvalidCookieDomainException

URL = "https://www.instagram.com/"
URL_BLOGGER = "https://www.instagram.com/{}/?__a=1"


def load_cookie(driver):
    with open('cookies.pickle', 'rb') as cookiesfile:
        cookies = pickle.load(cookiesfile)
        for cookie in cookies:
            try:
                t = cookie['domain']
                if t[0] == '.':
                    t = t[1:]
                    cookie['domain'] = t
                # print(cookie)
                driver.add_cookie(cookie)
            except InvalidCookieDomainException as e:
                print(e)


def check_platform():
    if platform.system() == "Windows":
        return False
    else:
        return True


def save_cookie(driver):
    with open('cookies.pickle', 'wb') as filehandler:
        pickle.dump(driver.get_cookies(), filehandler)


def get_driver():
    if check_platform():
        ua = UserAgent()
        options = Options()
        options.add_argument("--start-maximized")
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument(f"user-agent={ua.random}")
        driver = webdriver.Chrome(options=options)
        return driver
    else:
        return webdriver.Chrome()


def page_parse(driver: webdriver.Chrome, login: str):
    soup = BeautifulSoup(driver.page_source, 'lxml')
    text = soup.find('pre').text
    parsed_json = json.loads(text)
    try:
        _id = parsed_json['graphql']['user']['id']
        count = parsed_json['graphql']['user']['edge_followed_by']['count']
        return {
            "id": _id,
            "followers": count,
            "login": login
        }

    except Exception as e:
        return {}
