from selenium.webdriver.common.by import By
import time


link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_check_button(browser):
    browser.get(link)
    time.sleep(30)
    res = len(browser.find_elements(By.CLASS_NAME, 'btn-add-to-basket'))
    assert res == 1, 'Кнопка отсутствует'



