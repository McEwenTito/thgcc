from actions.base_actions import __scroll_down_page, browser
from pages.home_page import HomePage
from selenium import webdriver


def book_tee_time():
    home_page = HomePage(browser)
    __scroll_down_page(500)
    book_tee = browser.find_element("link text","Book a tee time")
    print(book_tee)
    book_tee.click()
    # home_page.book_tee_time_link.click()
