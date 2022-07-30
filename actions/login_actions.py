from actions.base_actions import BaseAction
from settings import secrets
from pages.login_page import LoginPage

class LoginActions():


    def __init__(self, browser):
        super(LoginActions, self).__init__()
        self.browser = browser
        self.login_page = LoginPage(browser)


    def select_user(self, user: str) -> str:
        return secrets.users[user]


    def login(self, user):
        user = self.select_user(user)
        self.login_page.go()
        self.login_page.username_input.input_text(user["username"])
        self.login_page.password_input.input_text(user["password"])
        self.login_page.login_button.click()
