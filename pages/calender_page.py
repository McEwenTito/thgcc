from selenium.webdriver.common.by import By

from .base_element import BaseElement
from .base_page import BasePage
from .locator import Locator
from settings import  locators
from settings import config


class CalenderPage(BasePage):


    @property
    def calender_dropdown(self):
        locator = Locator(by=By.XPATH, value=locators.calender_dropdown)
        return BaseElement(self.driver, locator)


    @property
    def sundays(self):
        locator  = Locator(by=By.XPATH, value=locators.sundays)
        return BaseElement(self.driver, locator)


    @property
    def next(self):
        locator  = Locator(by=By.XPATH, value=locators.next)
        return BaseElement(self.driver, locator)
