from selene import have
from selene.support.shared import browser
from google_test.pages.google import search
from google_test.pages.google import follow_result_link
from google_test.pages.github import githib_page_shuold_be


def test_search():
    browser.open('https://google.com/ncr')

    search('yashaka selene')
    follow_result_link(1)

    githib_page_shuold_be('yashaka/selene')