import allure
import pytest

from locators.locators_common import CommonLocators
from locators.locators_main_page import MainPageLocators


@allure.title("Переход на страницу заказа по кнопке Заказать")
class TestMainToOrderPage:

    @allure.description("Проверить переход на страницу заказа по клику на две кнопки Заказать на главной странице")
    @pytest.mark.parametrize(
        'locator',
        [MainPageLocators.ORDER_BUTTON_TOP, MainPageLocators.ORDER_BUTTON_BOTTOM]
    )
    @allure.step("Находим и кликаем по кнопке Куки, затем находим и кликаем по кнопке Заказать, проверяем перехолд на страницу заказа")
    def test_open_order_page(self, main_to_order_page, locator):
        main_to_order_page.click_on_element(CommonLocators.COOKIE_BUTTON)
        main_to_order_page.find_and_click_order_button(locator)
        assert main_to_order_page.check_order_page()
