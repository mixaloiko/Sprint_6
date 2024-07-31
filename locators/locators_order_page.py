from selenium.webdriver.common.by import By


class OrderPageLocators:
    # первый шаг
    FIRST_NAME_INPUT = (By.XPATH, "//*[@placeholder='* Имя']")
    LAST_NAME_INPUT = (By.XPATH, "//*[@placeholder='* Фамилия']")
    ADRESS_INPUT = (By.XPATH, "//*[@placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION_DROPDOWN = (By.XPATH, "//*[@placeholder='* Станция метро']")
    PHONE_INPUT = (By.XPATH, "//*[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.CSS_SELECTOR, ".Order_NextButton__1_rCA button.Button_Button__ra12g")
    METRO_STATION_NAME = (By.CSS_SELECTOR, "li.select-search__row:nth-child({})")
    # второй шаг
    FILL_DATE = (By.XPATH, "//*[@placeholder='* Когда привезти самокат']")
    FILL_TERMIN = (By.CLASS_NAME, "Dropdown-control")
    CHECKBOX_COLOR_BLACK = (By.ID, "black")
    CHECKBOX_COLOR_GREY = (By.ID, "grey")
    ORDER_BUTTON = (By.CSS_SELECTOR, ".Order_Buttons__1xGrp button:nth-child(2)")
    CONFIRM_BUTTON = (By.CSS_SELECTOR, ".Order_Modal__YZ-d3 .Order_Buttons__1xGrp button:nth-child(2)")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "Order_Form__17u6u")
    DROPDOWN_TERMIN = (By.CSS_SELECTOR, "div.Dropdown-option:nth-child({})")







