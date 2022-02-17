import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_basket_button(browser):
    browser.get(link)
    browser.implicitly_wait(10)
    button = browser.find_element_by_css_selector('#add_to_basket_form > button')
    time.sleep(5)
    assert button.text is not None
