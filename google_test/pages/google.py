from selene import have
from selene.support.shared import browser
from selene.support.shared.jquery_style import ss, s

def search(query: str):
    s('[name=q]').type(query).press_enter()


def result(number):
    return ss('#search .g')[number-1]


def follow_result_link(number):
    result(number).element('h3').click()