from selenium.webdriver.common.by import By


class AdminLoginPageLocators:

    LOGIN_INPUT = (By.CSS_SELECTOR, "input[id='login_email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[id='login_password']")
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, "button[id='login_Sign_in']")
