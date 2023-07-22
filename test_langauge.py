from selenium.webdriver.common.by import By
import time


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_basket_button(browser):
    browser.get(link)
    time.sleep(30)
  #  browser.find_element_by_css_selector('[class=btn btn-lg btn-primary btn-add-to-basket]')
    browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
    assert True
