import time

from utils import get_driver, save_cookie


def load_and_save_cookie():
    URL = "https://www.instagram.com/"
    #
    dr = get_driver()
    dr.get(URL)
    # you need to paste your data after that save cookie
    time.sleep(5)
    save_cookie(dr)
    # dr.get(URL)


if __name__ == '__main__':
    load_and_save_cookie()
