from selenium.webdriver.common.by import By


class BalancePageLocators:

    BALANCE_COUNT = (By.CSS_SELECTOR, "p[class='textnumber1 ui-text-purple']")
    DEPOSIT_BUTTON = (By.CSS_SELECTOR, "button[id='deposit_btn']")
    DEPOSIT_INPUT = (By.CSS_SELECTOR, "input[id='daposit_Amount']")
    DEPOSIT_IN_MODAL_BUTTON = (By.CSS_SELECTOR, "button[id='deposit']")

    ALERT = (By.CSS_SELECTOR, "div[role='alert']")
    ERROR = (By.CSS_SELECTOR, "div[class='ui-text-red subtitle2 ui-mt-1']")
