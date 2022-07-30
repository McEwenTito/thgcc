from pages.consent_page import ConsentPage



def accept_code(browser) -> None:
    consent_page = ConsentPage(browser)
    consent_page.accept_code_button.click()
