from selenium.webdriver.common.by import By


class MainPageLocators:

    QUESTION_LOCATOR = By.ID, 'accordion__heading-{}'
    ANSWER_LOCATOR = By.CSS_SELECTOR, '#accordion__panel-{} p'

    ORDER_BUTTON_TOP = By.CLASS_NAME, 'Button_Button__ra12g'
    ORDER_BUTTON_BOTTOM = By.CLASS_NAME, 'Button_Middle__1CSJM'

