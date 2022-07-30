import logging

from selenium import webdriver

logging.basicConfig(filename='info.log', level=logging.INFO, filemode='w',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

class Browser():

    def __init__(self):
        try:
            chrome_options = webdriver.ChromeOptions()
            prefs = {"profile.default_content_setting_values.notifications": 2}
            chrome_options.binary_location = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            chrome_options.add_experimental_option("prefs", prefs)
            chrome_options.add_argument("start-maximized");
            self.browser = webdriver.Chrome(options=chrome_options)
            self.browser.set_page_load_timeout(60)
            print(self.browser)

        except Exception as e:
            logging.exception(e)

