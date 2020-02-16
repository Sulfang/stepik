import math
from datetime import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/explicit_wait2.html"

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser.get(link)

price = WebDriverWait(browser, 15).until(
    EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
)

button = browser.find_element_by_id('book')
button.click()

x_value = browser.find_element_by_css_selector('#input_value').text
input_field = browser.find_element_by_css_selector('#answer')

submit = browser.find_element_by_css_selector('#solve')


y = calc(x_value)

input_field.send_keys(y)
submit.click()

time.sleep(20)
browser.quit()