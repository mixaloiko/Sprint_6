import allure


@allure.title("Переход с главной страницы на страницу Яндекс в новой вкладке")
class TestMainToYandexPage:

    @allure.step("Найти и кликнуть по кнопке Яндекс на главной странице, проверить переход на страницу Яндекс в новой вкладке браузера")
    def test_open_yandex_page(self, main_to_yandex_page):
        main_to_yandex_page.find_and_click_yandex_button()
        assert main_to_yandex_page.check_yandex_page()
