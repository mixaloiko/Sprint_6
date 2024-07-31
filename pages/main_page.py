from locators.locators_common import CommonLocators
from locators.locators_main_page import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    def scroll_to_and_click_on_question_and_get_answer_text(self, number):
        self.click_on_element(CommonLocators.COOKIE_BUTTON)
        formatted_question_locator = self.format_locator(MainPageLocators.QUESTION_LOCATOR, number)
        formatted_answer_locator = self.format_locator(MainPageLocators.ANSWER_LOCATOR, number)
        self.scroll_to_element(formatted_question_locator)
        self.click_on_element(formatted_question_locator)
        return self.get_text_from_element(formatted_answer_locator)

