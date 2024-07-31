from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class MainToOrderPage(BasePage):

    def find_and_click_order_button(self, locator):
        self.scroll_to_element(locator)
        self.click_on_element(locator)

    def check_order_page(self):
        # ожидание загрузки страницы
        WebDriverWait(self.driver, 3).until(expected_conditions.url_contains('order'))
        # проверить, что произошел переход на страницу входа
        current_url = self.driver.current_url
        return 'order' in current_url
