from selenium.webdriver.common.by import By


class RewardsPageLocators:

    BALANCE_FIELD = (By.CSS_SELECTOR, "p[class='textnumber1 text-purple']")
    TOTAL_TIME_STREAMING_AND_TOTAL_INCOME_FIELDS = (By.CSS_SELECTOR, "p[class='textnumber1 text-purple']")
    WITHDRAW_BUTTON = (By.CSS_SELECTOR, "button[id='withdraw_btn']")
    AMOUNT_INPUT = (By.CSS_SELECTOR, "input[id='daposit_Amount']")
    WITHDRAW_IN_MODAL_BUTTON = (By.CSS_SELECTOR, "button[id='deposit']")
    DISABLE_WITHDRAW_IN_MODAL_BUTTON = (By.CSS_SELECTOR, "button[disabled]")
    ALERT = (By.CSS_SELECTOR, "div[role='alert']")
    AMOUNT_INPUT_ERROR = (By.CSS_SELECTOR, "div[class='text-red subtitle2 mt-1']")

