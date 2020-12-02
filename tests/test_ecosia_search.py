from selene import have
from selene.support.shared import browser


def test_open_seacch():
    browser.open("https://www.ecosia.org/")
    browser.driver.maximize_window()

def test_search_links():
    browser.element('[name=q]').type('yashaka selene').press_enter()
    browser.all('.result').first.click()
    browser.all('[href="/yashaka/selene"]').should(have.size(3))

def test_close_brouser():
    browser.close()