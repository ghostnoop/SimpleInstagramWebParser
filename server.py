import json

import uvicorn
from fastapi import FastAPI
from selenium import webdriver

import utils

app = FastAPI()




@app.get("/instagram/{login}/")
async def inst_getter(login: str):
    driver.get(utils.URL_BLOGGER.format(login))
    return utils.page_parse(driver, login)
    # return {}


if __name__ == '__main__':
    global driver
    driver = utils.get_driver()
    driver.get(utils.URL)
    utils.load_cookie(driver)
    driver.refresh()

    uvicorn.run("server:app", host="127.0.0.1", port=5000, log_level="info")
