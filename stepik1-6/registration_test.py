from selenium import webdriver
import time

good_link = "http://suninjuly.github.io/registration1.html"
bad_link = "http://suninjuly.github.io/registration2.html"

def one_cycle(link):
    try: 
        
        browser = webdriver.Chrome()
        browser.get(link)

        # заполняем обязательные поля
        input1 = browser.find_element_by_css_selector(".first_block>.first_class>.first")
        input1.send_keys("Pavel")
        input2 = browser.find_element_by_css_selector(".first_block>.second_class>.second")
        input2.send_keys("Kiselev")
        input3 = browser.find_element_by_css_selector(".first_block>.third_class>.third")
        input3.send_keys("kpytoxakkep@mail.ru")
        
        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text

        assert "Congratulations! You have successfully registered!" == welcome_text

    finally:
        time.sleep(5)
        browser.quit()

if __name__ == '__main__':
    one_cycle(good_link)
    one_cycle(bad_link)
