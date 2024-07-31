from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from constants import YANDEX_URL_PART
from locators.locators_common import CommonLocators
from pages.base_page import BasePage


class MainToYandexPage(BasePage):

    def find_and_click_yandex_button(self):
        original_window = self.driver.current_window_handle

        self.click_on_element(CommonLocators.YANDEX_BUTTON)

        WebDriverWait(self.driver, 10).until(expected_conditions.number_of_windows_to_be(2))

        new_window = None
        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                new_window = window_handle
                break

        self.driver.switch_to.window(new_window)

    def check_yandex_page(self):
        # ожидание загрузки страницы
        WebDriverWait(self.driver, 5).until(expected_conditions.url_contains(YANDEX_URL_PART))
        # Проверка перехода в конструктор
        return YANDEX_URL_PART in self.driver.current_url
