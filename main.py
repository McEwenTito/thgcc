import logging

from actions import base_actions, login_actions, home_actions, consent_actions, calender_actions, booking_actions
from settings import config


def run():
    login_actions.login("conor")
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
    logging.info("slot selected")
    booking_actions.add_members(config.PLAYERS1)
    logging.info("players added")



if __name__ == '__main__':
    print("We are running!")
    run()


