from selenium.webdriver.common.by import By
from behave import given, when, then


SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
SEARCH_BTN = (By.ID, 'nav-search-submit-button')


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Search for {search_word}')
def search_amazon(context, search_word):
    context.driver.find_element(*SEARCH_INPUT).send_keys(search_word)
    context.driver.find_element(*SEARCH_BTN).click()


@when("Click on cart icon")
def step_impl(context):
    context.driver.find_element(By.ID, "nav-cart-count-container").click()
    """
    :type context: behave.runner.Context
    """
    #raise NotImplementedError(u'STEP: When Click on cart icon')


@then("Verify cart is empty")
def step_impl(context):
    actual_result = context.driver.find_element(By.XPATH, "//h2").text
    expected_result = "Your Amazon Cart is empty"
    assert actual_result == expected_result, f'Actual result {actual_result} does not match the expected result {expected_result}'