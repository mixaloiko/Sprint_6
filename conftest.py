import pytest
from selenium.webdriver import Firefox

from constants import MAIN_URL, ORDER_URL
from pages.main_page import MainPage
from pages.main_to_order_page import MainToOrderPage
from pages.main_to_yandex_page import MainToYandexPage
from pages.order_page import OrderPage
from pages.order_to_main_page import OrderToMainPage


@pytest.fixture()
def driver():
    driver = Firefox()
    yield driver
    driver.quit()


@pytest.fixture()
def main_page(driver):
    page = MainPage(driver)
    page.get_url(MAIN_URL)
    return page


@pytest.fixture()
def order_page(driver):
    page = OrderPage(driver)
    page.get_url(ORDER_URL)
    return page


@pytest.fixture()
def main_to_order_page(driver):
    page = MainToOrderPage(driver)
    page.get_url(MAIN_URL)
    return page


@pytest.fixture
def order_to_main_page(driver):
    page = OrderToMainPage(driver)
    page.get_url(ORDER_URL)
    return page


@pytest.fixture()
def main_to_yandex_page(driver):
    page = MainToYandexPage(driver)
    page.get_url(MAIN_URL)
    return page
