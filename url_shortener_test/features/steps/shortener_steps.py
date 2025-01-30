from behave import given, when, then
from selenium import webdriver
from pages.shortener_page import ShortenerPage

@given('the user is on the URL shortener page')
def step_open_page(context):
    context.driver = webdriver.Chrome()
    context.page = ShortenerPage(context.driver)
    context.page.open()

@when('the user enters a URL "{url}"')
def step_enter_url(context, url):
    context.page.shorten_url(url)

@when('clicks the "Make it short" button')
def step_click_shorten(context):
    context.page.click_element(ShortenerPage.SHORT_BUTTON)

@then('a shortened URL should be displayed')
def step_verify_shortened_url(context):
    assert context.page.get_shortened_url() == "c984d0"

@when('the user enters a shortened URL "{short_url}"')
def step_enter_short_url(context, short_url):
    context.page.retrieve_original_url(short_url)

@when('clicks the "Get original" button')
def step_click_get_original(context):
    context.page.click_element(ShortenerPage.LONG_BUTTON)

@then('the original URL should be displayed')
def step_verify_original_url(context):
    assert context.page.get_original_url() == "https://example.com"

@then('the click count for should be displayed as "2"')
def STEP_get_clickcountmsg_url(context):
    assert context.page.get_original_url() == "2"

@When('the original URL should be displayed')
def step_verify_original_url(context):
    assert context.page.get_original_url() == "https://example.com"


@then('the user should be redirected to the original URL "{expected_url}"')
def step_verify_original_url(context, expected_url):
    context.page.open_original_url()
    

@then('error message "invalid url" should be displayed')
def step_verify_original_url(context):
    assert context.page.get_original_url() == "invalid url"

@then('error message "invalid short url" should be displayed')
def step_verify_original_url(context):
    assert context.page.get_original_url() == "invalid short url"

@then('close the browser')
def step_close_browser(context):
    context.driver.quit()