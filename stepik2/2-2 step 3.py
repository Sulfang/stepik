from datetime import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/selects2.html"


browser.get(link)

num1 = browser.find_element_by_css_selector("#num1").text
num2 = browser.find_element_by_css_selector('#num2').text

sum = int(num1) + int(num2)

select = Select(browser.find_element_by_css_selector('#dropdown'))
select.select_by_visible_text(f"{sum}")

submit_btn = browser.find_element_by_css_selector('.btn').click()

time.sleep(20)
browser.quit()