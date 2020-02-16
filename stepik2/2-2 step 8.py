from selenium import webdriver
import time
import os

from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_name("email")
    input3.send_keys("tonchik014@yandex.ru")
    input_file = browser.find_element_by_css_selector("#file")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    input_file.send_keys(file_path)
    button = browser.find_element_by_css_selector('.btn')
    button.click()

finally:
    time.sleep(30)
    browser.quit()