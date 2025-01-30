from selenium import webdriver
from pages.shortener_page import ShortenerPage
import logging

def before_all(context):
    context.driver = webdriver.Chrome()
    context.page = ShortenerPage(context.driver)
    logging.basicConfig(level=logging.DEBUG)
    logging.debug("Starting BDD tests...")

def after_all(context):
    context.driver.quit()