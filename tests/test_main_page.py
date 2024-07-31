import allure
import pytest

from constants import Answers


@allure.title("Выпадающий список вопрос-ответ на главной странице")
class TestMainPage:
    @allure.description("Проверить, чтобы при клике на каждый вопрос, появлялся соответствующий ответ")
    @pytest.mark.parametrize(
        'question_number, expected_result',
        [(0, Answers.ANSWER_0),
         (1, Answers.ANSWER_1),
         (2, Answers.ANSWER_2),
         (3, Answers.ANSWER_3),
         (4, Answers.ANSWER_4),
         (5, Answers.ANSWER_5),
         (6, Answers.ANSWER_6),
         (7, Answers.ANSWER_7)]
    )
    @allure.step("Прокручиваем страницу к послденему вопросу, нажимаем на каждый вопрос по порядку, проверяем, чтобы выпал ответ")
    def test_questions(self, main_page, question_number, expected_result):
        result = main_page.scroll_to_and_click_on_question_and_get_answer_text(question_number)
        assert result == expected_result
