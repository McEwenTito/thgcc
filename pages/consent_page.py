from selenium.webdriver.common.by import By

from .base_element import BaseElement
from .base_page import BasePage
from .locator import Locator
from settings import  locators
from settings import config


class ConsentPage(BasePage):


    @property
    def accept_code_button(self):
        locator = Locator(by=By.XPATH, value=locators.accept_code_button)
        return BaseElement(self.driver, locator)

