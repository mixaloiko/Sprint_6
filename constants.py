from random import randint

from locators.locators_main_page import MainPageLocators
from locators.locators_order_page import OrderPageLocators

MAIN_URL = "https://qa-scooter.praktikum-services.ru/"
ORDER_URL = "https://qa-scooter.praktikum-services.ru/order"
YANDEX_URL_PART = "dzen.ru"


class Answers:
    ANSWER_0 = "Сутки — 400 рублей. Оплата курьеру — наличными или картой."
    ANSWER_1 = "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."
    ANSWER_2 = "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."
    ANSWER_3 = "Только начиная с завтрашнего дня. Но скоро станем расторопнее."
    ANSWER_4 = "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."
    ANSWER_5 = "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."
    ANSWER_6 = "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."
    ANSWER_7 = "Да, обязательно. Всем самокатов! И Москве, и Московской области."


class OrderPageInputData:
    def __init__(self, first_name, last_name, address, phone, number, order_button_locator, color):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.phone = phone
        self.number = number
        self.order_button_locator = order_button_locator
        self.color = color


order_page_input_data_list = [
    OrderPageInputData(
        first_name="Иван",
        last_name="Иванов",
        address="Москва",
        phone=f"749{randint(11111111, 99999999)}",
        number=1,
        order_button_locator=MainPageLocators.ORDER_BUTTON_BOTTOM,
        color=OrderPageLocators.CHECKBOX_COLOR_BLACK
    ),
    OrderPageInputData(
        first_name="Петя",
        last_name="Петров",
        address="Минск",
        phone=f"749{randint(11111111, 99999999)}",
        number=2,
        order_button_locator=MainPageLocators.ORDER_BUTTON_TOP,
        color=OrderPageLocators.CHECKBOX_COLOR_GREY
    )
]
