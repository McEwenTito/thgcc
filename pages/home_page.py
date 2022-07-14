from selenium.webdriver.common.by import By

from .base_element import BaseElement
from .base_page import BasePage
from .locator import Locator
from settings import  locators
from settings import config


class HomePage(BasePage):


    @property
    def book_tee_time_link(self):
        locator = Locator(by=By.XPATH, value=locators.book_tee_time_link)
        return BaseElement(self.driver, locator)

