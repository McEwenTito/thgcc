import logging
import time
import selenium
import sys


from actions import base_actions, login_actions, home_actions, consent_actions, calender_actions, booking_actions
from settings import config


def run(user, players):
    print(selenium.__version__)
    login_actions.login(user)
    logging.info("logged in")
    home_actions.book_tee_time()
    logging.info("clicked book")
    consent_actions.accept_code()
    logging.info("consented")
    calender_actions.drop_calender()
    logging.info("calender droped")
    calender_actions.click_sunday()
    logging.info("date clicked")
    booking_actions.select_available_slot()
    time.sleep(2)
    logging.info("slot selected")
    booking_actions.add_members(players)
    logging.info("players added")



if __name__ == '__main__':
    print("We are running!")
    run(sys.argv[1], config.PLAYERS[sys.argv[2]])


