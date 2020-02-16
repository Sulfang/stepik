from datetime import time

from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/redirect_accept.html"

browser.get(link)

redirect_btn = browser.find_element_by_css_selector('.btn')
redirect_btn.click()

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

x_value = browser.find_element_by_css_selector('#input_value').text
input_field = browser.find_element_by_css_selector('#answer')

submit = browser.find_element_by_css_selector('.btn')


y = calc(x_value)

input_field.send_keys(y)
submit.click()

time.sleep(20)
browser.quit()