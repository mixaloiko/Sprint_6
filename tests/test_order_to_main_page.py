import allure

from locators.locators_common import CommonLocators


@allure.title("Переход со страницы заказа на главную страницу по клику на кнопку Самокат")
class TestOrderToMainPage:

    @allure.step("Находим и кликаем на кнопку Самокат на странице заказа, проверяем, что произошел переход на главную страницу")
    def test_open_main_page(self, order_to_main_page):
        order_to_main_page.click_on_element(CommonLocators.SCOOTER_BUTTON)
        assert order_to_main_page.check_main_page()

