from selenium.webdriver.common.by import By


class BalancePageLocators:

    BALANCE_COUNT = (By.CSS_SELECTOR, "p[class='textnumber1 text-purple']")
    DEPOSIT_BUTTON = (By.CSS_SELECTOR, "button[id='deposit_btn']")
    DEPOSIT_INPUT = (By.CSS_SELECTOR, "input[id='daposit_Amount']")
    DEPOSIT_IN_MODAL_BUTTON = (By.CSS_SELECTOR, "button[id='deposit']")

    ALERT = (By.CSS_SELECTOR, "div[role='alert']")
    ERROR = (By.CSS_SELECTOR, "div[class='text-red subtitle2 mt-1']")

    TRANSACTION_INFORMATION = (By.CSS_SELECTOR, "td[class='text-center']")

    # stripe
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[id='email']")

    CARD_BUTTON = (By.CSS_SELECTOR, "button[id='card_tab']")
    CASH_APP_PAY = (By.CSS_SELECTOR, "button[id='cashapp-tab']")

    CARD_NUMBER_INPUT = (By.CSS_SELECTOR, "input[id='cardNumber']")
    MM_YY = (By.CSS_SELECTOR, "input[id='cardExpiry']")
    CVC = (By.CSS_SELECTOR, "input[id='cardCvc']")

    CARD_HOLDER_NAME_INPUT = (By.CSS_SELECTOR, "input[id='billingName']")

    COUNTRY_DROP = (By.CSS_SELECTOR, "select[id='billingCountry']")

    PAY_BUTTON = (By.CSS_SELECTOR, "button[class='SubmitButton SubmitButton--complete']")
