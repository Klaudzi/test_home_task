from selenium import webdriver
import pytest
import time

def test_add_product(browser):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)
    time.sleep(30)
    element = browser.find_element_by_xpath('//*[@id="add_to_basket_form"]/button').text
    # print("\nЗначение", element)
    assert element != "" , "No correct!!!"