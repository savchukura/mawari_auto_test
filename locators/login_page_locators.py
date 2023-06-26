from selenium.webdriver.common.by import By


class LoginPageLocators:

    EMAIL_INPUT = (By.CSS_SELECTOR, "input[id='login_email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[id='login_password']")
    NODE_RUNNER_RADIO = (By.CSS_SELECTOR, "div[id='role_node_runner']")
    DEVELOPER_RADIO = (By.CSS_SELECTOR, "div[id='role_developer']")
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, "button[id='login_Sign_in']")
    LOG_OUT_BUTTON = (By.CSS_SELECTOR, "button[id='user_logout']")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "div[class='ui-text-red subtitle2 ui-mt-1']")


class SignUpPageLocators:

    SIGN_UP_BUTTON = (By.CSS_SELECTOR, "a[href='/register']")

