import datetime
import logging
import time

from actions.base_actions import browser
from pages.booking_page import BookingPage
from pages.calender_page import CalenderPage


booking_page = BookingPage(browser)


def select_available_slot():
    print("atleast we here")

    booking_page.go()
    booking_page.go()
    print(len(booking_page.select_slot.web_elements))
    booking_page.select_slot.web_element.click()
    booking_page.submit_slot.click()

def add_member(name):
    booking_page.add_player.web_element.click()
    booking_page.another_member.web_element.click()
    booking_page.player_input.input_text(name.split()[1][:3])
    booking_page.submit_player.click()
    # player = browser.find_element("link text", name)
    time.sleep(2)
    player = browser.find_element("partial link text", name)
    player.click()
    time.sleep(3)


def add_members(members):
    for member in members:
        add_member(member)
    # booking_page.finish.click()
    logging.info(f"finished: {booking_page.finish.text}")




