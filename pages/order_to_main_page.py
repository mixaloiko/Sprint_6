from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from constants import MAIN_URL
from locators.locators_common import CommonLocators
from pages.base_page import BasePage


class OrderToMainPage(BasePage):

    def find_and_click_scooter_button(self):
        self.click_on_element(CommonLocators.SCOOTER_BUTTON)

    def check_main_page(self):
        # ожидание загрузки страницы
        WebDriverWait(self.driver, 3).until(expected_conditions.url_matches(MAIN_URL))
        # Проверка перехода в конструктор
        return self.driver.current_url == MAIN_URL
