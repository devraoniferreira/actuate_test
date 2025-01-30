from selenium import webdriver
from pages.shortener_page import ShortenerPage

def before_all(context):
    context.driver = webdriver.Chrome()
    context.page = ShortenerPage(context.driver)

def after_all(context):
    context.driver.quit()