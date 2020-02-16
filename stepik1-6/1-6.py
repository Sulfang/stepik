from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/simple_form_find_task.html")
button = browser.find_element(By.ID, "submit_button")
button.click()

browser.quit()
#close() в свою очередь закрывает только текущую вкладку, когда quit закрывает браузер полностью
