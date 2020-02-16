from datetime import time

from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"

browser.get(link)

confirm_btn = browser.find_element_by_css_selector('.btn')
confirm_btn.click()
confirm = browser.switch_to.alert
confirm.accept()

x_value = browser.find_element_by_css_selector('#input_value').text
input_field = browser.find_element_by_css_selector('#answer')

submit = browser.find_element_by_css_selector('.btn')


y = calc(x_value)

input_field.send_keys(y)
submit.click()

time.sleep(20)
browser.quit()