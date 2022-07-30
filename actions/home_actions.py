import time

from actions.base_actions import BaseAction
from pages.home_page import HomePage
from selenium import webdriver


class HomeActions(BaseAction):


    def __init__(self, browser):
        self.browser = browser
        self.home_page = HomePage(self.browser)
        # self.base_action = BaseAction()
        print(self.browser)


    def book_tee_time(self):
        self.scroll_down_page(500)
        time.sleep(5)
        book_tee = self.browser.find_element("link text","Book a tee time")
        print(book_tee)
        book_tee.click()
        self.home_page.book_tee_time_link.click()
