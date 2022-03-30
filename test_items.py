from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

class TestCatalogePage():
    def test_item_has_add_to_cart_button(self, browser):
        browser.get(link)
        time.sleep(10)
        button = browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
        assert button,"корзина не найдена"

