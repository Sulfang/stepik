from selenium import webdriver
import time
import math

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/get_attribute.html"

browser.get(link)


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


x_element = browser.find_element_by_css_selector("#treasure")
x_value = x_element.get_attribute("valuex")
y = calc(x_value)

text_field = browser.find_element_by_css_selector("#answer")
text_field.send_keys(y)

checkbox = browser.find_element_by_css_selector("#robotCheckbox")
checkbox.click()

radiobutton = browser.find_element_by_css_selector("#robotsRule")
radiobutton.click()

submit_btn = browser.find_element_by_css_selector(".btn")
submit_btn.click()

time.sleep(20)
browser.quit()
