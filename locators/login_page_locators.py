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
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[id='login_email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[id='login_password']")
    NODE_RUNNER_RADIO = (By.CSS_SELECTOR, "div[id='role_node_runner']")
    DEVELOPER_RADIO = (By.CSS_SELECTOR, "div[id='role_developer']")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "button[id='login_Sign_in']")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "div[class='ui-text-red subtitle2 ui-mt-1']")


class UserPersonalPageLocators:

    USER_PERSONAL = (By.CSS_SELECTOR, "p[class='subtitle2 ellipsis']")
    CHANGE_PASSWORD_BUTTON = (By.CSS_SELECTOR, "button[id='change_password']")
    OLD_PASSWORD_INPUT = (By.CSS_SELECTOR, "input[id='change_password_password']")
    NEW_PASSWORD_INPUT = (By.CSS_SELECTOR, "input[id='change_password_newPassword']")
    CONFIRM_NEW_PASSWORD_INPUT = (By.CSS_SELECTOR, "input[id='change_password_confirmPassword']")
    CHANGE_PASSWORD_IN_MODAL_BUTTON = (By.CSS_SELECTOR, "button[id='change_password_Sign_in']")
    ALERT = (By.CSS_SELECTOR, "div[role='alert']")
    ERROR_UNDER_INPUT = (By.CSS_SELECTOR, "div[class='ui-text-red subtitle2 ui-mt-1']")


