from datetime import datetime

from locators.locators_order_page import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):

    # находим и заполняем поля заказа
    def fill_order_form(self, first_name, last_name, address, phone):
        self.set_text_to_element(OrderPageLocators.FIRST_NAME_INPUT, first_name)
        self.set_text_to_element(OrderPageLocators.LAST_NAME_INPUT, last_name)
        self.set_text_to_element(OrderPageLocators.ADRESS_INPUT, address)
        self.set_text_to_element(OrderPageLocators.PHONE_INPUT, phone)

    # находим поле с выпадающим списком и кликаем на него
    def find_and_clik_dropdown(self):
        self.click_on_element(OrderPageLocators.METRO_STATION_DROPDOWN)

    # выбираем строку из выпавшего списка
    def select_row_in_dropdown(self, number):
        formatted_metro_station_name_locator = self.format_locator(OrderPageLocators.METRO_STATION_NAME, number)
        self.click_on_element(formatted_metro_station_name_locator)

    def find_and_clik_next_button(self):
        self.scroll_to_element(OrderPageLocators.NEXT_BUTTON)
        self.click_on_element(OrderPageLocators.NEXT_BUTTON)

    def find_and_clik_and_select_dropdown_fill(self, number, color_locator):
        self.click_on_element(OrderPageLocators.FILL_TERMIN)
        formatted_dropdown_termin_locator = self.format_locator(OrderPageLocators.DROPDOWN_TERMIN, number)
        self.click_on_element(formatted_dropdown_termin_locator)
        self.click_on_element(color_locator)
        # Получение сегодняшней даты
        today = datetime.today()
        # Форматирование даты в строку формата "дд.мм.гггг"
        formatted_date = today.strftime("%d.%m.%Y")
        self.set_text_to_element(OrderPageLocators.FILL_DATE, formatted_date)

    def find_and_click_order_button(self):
        self.click_on_element(OrderPageLocators.ORDER_BUTTON)

    def find_and_click_confirm_button(self):
        self.click_on_element(OrderPageLocators.CONFIRM_BUTTON)

    def check_order_successful(self):
        success_message = self.find_element_with_wait(OrderPageLocators.SUCCESS_MESSAGE)
        return success_message is not None
