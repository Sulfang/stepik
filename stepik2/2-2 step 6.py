from datetime import time

from selenium import webdriver
import math

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/execute_script.html"

browser.get(link)

x_value = browser.find_element_by_css_selector('#input_value').text
input_field = browser.find_element_by_css_selector('#answer')
check_box = browser.find_element_by_css_selector('#robotCheckbox')
radio = browser.find_element_by_css_selector('#robotsRule')
submit = browser.find_element_by_css_selector('.btn')


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


y = calc(x_value)
browser.execute_script("window.scrollBy(0, 120);")

input_field.send_keys(y)
check_box.click()
radio.click()
submit.click()

time.sleep(20)
browser.quit()