import logging, time, datetime
from selenium import webdriver


from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.consent_page import ConsentPage
from settings import config, locators, secrets
import sys, importlib, os


logging.basicConfig(filename='info.log', level=logging.INFO, filemode='w',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

try:
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications": 2}
    chrome_options.binary_location = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_argument("start-maximized");
    browser = webdriver.Chrome(options=chrome_options)
    browser.set_page_load_timeout(60)
except Exception as e:
    logging.exception(e)


def __scroll_down_page(to=1000):
    browser.execute_script(f"window.scrollTo(0, {to})")




def accept_code():
    consent_page = ConsentPage(browser)
    consent_page.accept_code_button.click()

