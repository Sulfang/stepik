from selenium import webdriver
import time
import math

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/math.html"
browser.get(link)


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


x_element = browser.find_element_by_css_selector("#input_value")
text_field = browser.find_element_by_css_selector("#answer")

x = x_element.text
y = calc(x)

text_field.send_keys(y)

checkbox = browser.find_element_by_css_selector("#robotCheckbox")
checkbox.click()

radiobutton = browser.find_element_by_css_selector("#robotsRule")
radiobutton.click()

submit_btn = browser.find_element_by_css_selector(".btn")
submit_btn.click()

time.sleep(20)
browser.quit()

