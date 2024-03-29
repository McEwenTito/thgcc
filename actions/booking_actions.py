import datetime
import logging
import time

from actions.base_actions import BaseAction
from pages.booking_page import BookingPage
from pages.calender_page import CalenderPage



class BookingActions():

    def __init__(self, browser):
        self.browser = browser
        self.booking_page = BookingPage(browser)


    def select_available_slot(self, slot):
        try:
            self.booking_page.select_slot
            self.booking_page.select_slot.web_elements[slot].click()
            logging.info(f"selected slot at {datetime.datetime.now()}")
            # self.booking_page.select_slot.web_elements

        except Exception as e:
            # print(e)
            logging.info(e)
            self.browser.refresh()
            self.select_available_slot(slot)

        # self.find_available_slot(slot)
        # self.booking_page.select_slot.web_elements[slot].click()
        try:
            # self.booking_page.submit_slot.find()
            self.booking_page.submit_slot.click()
        except Exception as e:
            pass
        # print(f'found a slot at {datetime.datetime.now()}')
        logging.info(f'found a slot at {datetime.datetime.now()}')


    def add_member(self, name):
        self.booking_page.add_player.web_element.click()
        self.booking_page.another_member.web_element.click()
        self.booking_page.player_input.input_text(name.split()[1][:3])
        self.booking_page.submit_player.click()
        time.sleep(2)
        player = self.browser.find_element("partial link text", name)
        player.click()
        time.sleep(2)


    def add_members(self, members):
        for member in members:
            self.add_member(member)
        logging.info(f"finished: {self.booking_page.finish.text}")
        self.booking_page.finish.click()




