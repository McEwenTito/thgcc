import datetime
import time

from actions.base_actions import BaseAction
from pages.calender_page import CalenderPage



class CalenderActions():

    def __init__(self, browser):
        self.calender_page = CalenderPage(browser)


    def drop_calender(self):
        self.calender_page.calender_dropdown.click()


    def convert_to_date(self, date_element):
        date = datetime.datetime(int(date_element.get_attribute("data-year")),
                                        int(date_element.get_attribute("data-month")) + 1, int(date_element.text))
        return str(date.date())



    def get_next_sunday(self) -> datetime.datetime:
        today = datetime.datetime.now().date()
        d = datetime.timedelta(days=14)
        print(today)
        print(today+d)
        return today+d


    def get_sundays(self) -> list:
        sunday_elements = self.calender_page.sundays.web_elements
        print(f"suday ele {sunday_elements}")
        keys = [self.convert_to_date(date) for date in sunday_elements]
        sunday_dates = dict(zip(keys, sunday_elements))
        print("sunday dicts: " + str(sunday_dates))
        return sunday_dates


    def click_sunday(self):
        sundays = self.get_sundays()
        next_sunday = self.get_next_sunday()
        print(f"sunday {list(sundays.keys())}")
        print(f"Next sunday: {next_sunday}")
        if str(next_sunday) in list(sundays.keys()):
            print(f"found: {sundays[str(next_sunday)]}")
            sundays[str(next_sunday)].click()
        else:
            self.calender_page.next.click()
            # time.sleep(1)
            self.click_sunday()



