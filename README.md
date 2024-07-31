# Sprint_6
В папке **locators** находятся все необходимы для проекта локаторы.
В папке **pages** описаны необходимые методы для тестирования. Они поделены на страницы:
- base_page
- main_page
- main_to_order_page
- main_to_yandex_page
- order_page
- order_to_main_page
В папке **tests** описанты тесты:
1. test_main_page - проверяет клик по вопросу и получению соответствующего ответа
2. test_main_to_order_page - проверяет переход на страницу заказа по клику на две кнопки Заказать на главной странице
3. test_main_to_yadndex_page - проверяет, что открылась страница Яндекс в новой вкладке браузера
4. test_order_page - позитивная проверка оформления заказа с двумя наборрами данных
5. test_order_to_main_page - проверка перехода на главную страницу со страницы заказа
В файле **conftest** описаны фикстуры 
В файле **constants** находятся статические данные для тестов 

