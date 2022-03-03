from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_guest_should_see_btn_basket(browser):
    browser.get(link)
    assert browser.find_elements(By.CSS_SELECTOR, '.btn-add-to-basket'), 'button basket not found'