import logging, time, datetime
from selenium import webdriver


from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.consent_page import ConsentPage
from settings import config, locators, secrets
import sys, importlib, os


logging.basicConfig(filename='info.log', level=logging.INFO, filemode='w',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

class BaseAction():


    def __init__(self, browser):
        self.browser = browser


    def scroll_down_page(self, to=1000):
        print("Scolling")
        print(self.browser)
        self.browser.execute_script(f"window.scrollTo(0, {to})")
        print("Done scrolling")


    def accept_code(self):
        consent_page = ConsentPage(self.browser)
        consent_page.accept_code_button.click()

