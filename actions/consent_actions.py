from actions.base_actions import browser
from pages.consent_page import ConsentPage



def accept_code() -> None:
    consent_page = ConsentPage(browser)
    consent_page.accept_code_button.click()
