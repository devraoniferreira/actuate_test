from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ShortenerPage(BasePage):
    URL = "http://localhost:8000/static/index.html" 

    SHORT_INPUT = (By.ID, "shortinput")
    SHORT_BUTTON = (By.ID, "shortbtn")
    SHORT_MSG = (By.ID, "shortmsg")

    LONG_INPUT = (By.ID, "longinput")
    LONG_BUTTON = (By.ID, "longbtn")
    LONG_MSG = (By.ID, "longmsg")

    CLICK_COUNT_MSG = (By.ID, "clickcountmsg")

    def open(self):
        self.driver.get(self.URL)

    def shorten_url(self, url):
        self.enter_text(self.SHORT_INPUT, url)
        self.click_element(self.SHORT_BUTTON)

    def get_shortened_url(self):
        return self.get_text(self.SHORT_MSG)

    def retrieve_original_url(self, short_url):
        self.enter_text(self.LONG_INPUT, short_url)
        self.click_element(self.LONG_BUTTON)

    def get_original_url(self):
        return self.get_text(self.LONG_MSG)

    def get_clickcountmsg_url(self):
        return self.get_text(self.CLICK_COUNT_MSG)

    def open_original_url(self):
        original_url = self.get_text(self.LONG_MSG)
        self.driver.get(self.LONG_MSG)