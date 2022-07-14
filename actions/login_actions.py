from actions.base_actions import __scroll_down_page, browser
from settings import secrets
from pages.login_page import LoginPage


def select_user(user: str) -> str:
    return secrets.users[user]

def login(user):
    user = select_user(user)
    login_page = LoginPage(browser)
    login_page.go()
    __scroll_down_page()
    login_page.username_input.input_text(user["username"])
    login_page.password_input.input_text(user["password"])
    login_page.login_button.click()
