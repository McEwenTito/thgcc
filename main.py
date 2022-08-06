import logging
import time
import selenium
import sys
import threading


from actions import consent_actions
from selenium import webdriver

from actions.booking_actions import BookingActions
from actions.browser import Browser
from actions.calender_actions import CalenderActions
from actions.login_actions import LoginActions
from actions.home_actions import HomeActions
from settings import config


browser = Browser().browser
browser2 = Browser().browser


def run(user, players, browser, slot):

    print(selenium.__version__)
    login_actions = LoginActions(browser)
    login_actions.login(user)
    logging.info("logged in")
    home_actions = HomeActions(browser)
    try:
        home_actions.book_tee_time()
    except Exception as e:
        logging.exception(e)
        pass
    logging.info("clicked book")
    consent_actions.accept_code(browser)
    logging.info("consented")
    calender_actions = CalenderActions(browser)
    calender_actions.drop_calender()
    logging.info("calender droped")
    calender_actions.click_sunday()

    logging.info("date clicked")
    booking_actions = BookingActions(browser)
    booking_actions.select_available_slot(slot)
    time.sleep(1)
    # logging.info("slot selected")
    booking_actions.add_members(players)
    logging.info("players added")



if __name__ == '__main__':
    # print("We are running!")
    t1 = threading.Thread(target=run, args=["joe", config.PLAYERS["set1"], browser, 0])
    t2 = threading.Thread(target=run, args=["conor", config.PLAYERS["set2"], browser2, 1])

    t1.start()
    # time.sleep(6)
    t2.start()

    t1.join()
    t2.join()
    # run(sys.argv[1], config.PLAYERS[sys.argv[2]])


