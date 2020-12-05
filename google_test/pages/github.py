from selene import have
from selene.support.shared import browser


def githib_page_shuold_be(partial_title):
    browser.should(have.title_containing(partial_title))

