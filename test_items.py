from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


class TestCatalogePage():
 def test_guest_should_see_login_link(self, browser):
     browser.get(link)
     time.sleep(10)
     button = browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
     assert button == browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")


