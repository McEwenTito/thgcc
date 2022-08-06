from selenium.webdriver.common.by import By

from .base_element import BaseElement
from .base_page import BasePage
from .locator import Locator
from settings import  locators
from settings import config


class BookingPage(BasePage):

    url = "https://www.thgcc.co.uk/memberbooking/?date=15-07-2022&course=28&group=1"
    #
    # @property
    # def select_slot(self):
    #     locator = Locator(by=By.XPATH, value=locators.available_slot)
    #     return BaseElement(self.driver, locator)
    #

    @property
    def select_slot(self):
        locator = Locator(by=By.LINK_TEXT, value="Select")
        return BaseElement(self.driver, locator)


    @property
    def submit_slot(self):
        locator = Locator(by=By.XPATH, value=locators.submit_slot)
        return BaseElement(self.driver, locator)


    @property
    def add_player(self):
        locator = Locator(by=By.XPATH, value=locators.add_player)
        return BaseElement(self.driver, locator)


    @property
    def another_member(self):
        locator = Locator(by=By.XPATH, value=locators.another_member)
        return BaseElement(self.driver, locator)


    @property
    def player_input(self):
        locator = Locator(by=By.XPATH, value=locators.player_input)
        return BaseElement(self.driver, locator)


    @property
    def submit_player(self):
        locator = Locator(by=By.XPATH, value=locators.submit_player)
        return BaseElement(self.driver, locator)


    @property
    def finish(self):
        locator = Locator(by=By.XPATH, value=locators.finish)
        return BaseElement(self.driver, locator)