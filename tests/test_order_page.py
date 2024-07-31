import allure
import pytest

from constants import order_page_input_data_list
from locators.locators_common import CommonLocators


@allure.title("Проверка успешного оформления заказа")
class TestOrderPage:
    @allure.description("Проверяем позитивный сценарий с двумя наборами данных")
    @pytest.mark.parametrize(
        'input_data',
        order_page_input_data_list
    )
    @allure.step("1 - кликаем на кнопку Куки"
                 "2 - вводим данные в поля Имя, Фамилия, Адрес, Телефон"
                 "3 - кликаем на выпадающий список в строке Станция метро и выбираем значение"
                 "4 - нажимаем на кнопку Далее"
                 "5 - заполняем поля с датой доставки, сроком арены и цветом самоката"
                 "6 - нажимаем кнопку Заказать"
                 "7 - нажимаем кнопку подтверждения заказа"
                 "8 - проверяем, что появилось сообщение об успешно оформленном заказе и номер заказа")
    def test_fill_order(self, order_page, input_data):
        order_page.click_on_element(CommonLocators.COOKIE_BUTTON)
        order_page.fill_order_form(input_data.first_name, input_data.last_name, input_data.address, input_data.phone)
        order_page.find_and_clik_dropdown()
        order_page.select_row_in_dropdown(input_data.number)
        order_page.find_and_clik_next_button()
        order_page.find_and_clik_and_select_dropdown_fill(input_data.number, input_data.color)
        order_page.find_and_click_order_button()
        order_page.find_and_click_confirm_button()
        assert order_page.check_order_successful()
