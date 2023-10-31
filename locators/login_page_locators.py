from selenium.webdriver.common.by import By


class LoginPageLocators:

    EMAIL_INPUT = (By.CSS_SELECTOR, "input[id='login_email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[id='login_password']")
    NODE_RUNNER_RADIO = (By.CSS_SELECTOR, "div[id='role_node_runner']")
    DEVELOPER_RADIO = (By.CSS_SELECTOR, "div[id='role_developer']")
    VALIDATOR_RADIO = (By.CSS_SELECTOR, "div[id='role_validator']")
    CONFIRM_BUTTON = (By.CSS_SELECTOR, "a[id='confirm-role-btn']")
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, "button[class='button flex select-none items-center justify-center rounded-[8px] text-center  duration-150 ease-in-out text-white bg-btnDef hover:bg-btnHover active:bg-btnActive disabled:bg-btnDisable h-[44px] w-full']")
    LOG_OUT_BUTTON = (By.CSS_SELECTOR, "button[id='user_logout']")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "div[class='text-red subtitle2 mt-1']")


class SignUpPageLocators:

    SIGN_UP_BUTTON = (By.CSS_SELECTOR, "a[href='/register']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[id='login_email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[id='login_password']")
    NODE_RUNNER_RADIO = (By.CSS_SELECTOR, "div[id='role_node_runner']")
    DEVELOPER_RADIO = (By.CSS_SELECTOR, "div[id='role_developer']")
    VALIDATOR_RADIO = (By.CSS_SELECTOR, "div[id='role_validator']")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "button[id='login_Sign_in']")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "div[class='text-red subtitle2 mt-1']")
    VERIFY_EMAIL = (By.CSS_SELECTOR, "h1[class='h1 mb-2 text-center']")
    CHECK_EMAIL = (By.CSS_SELECTOR, "span[class='text-purple']")


class UserPersonalPageLocators:

    USER_PERSONAL = (By.CSS_SELECTOR, "p[class='subtitle2 ellipsis']")
    CHANGE_PASSWORD_BUTTON = (By.CSS_SELECTOR, "button[id='change_password']")
    OLD_PASSWORD_INPUT = (By.CSS_SELECTOR, "input[id='change_password_password']")
    NEW_PASSWORD_INPUT = (By.CSS_SELECTOR, "input[id='change_password_newPassword']")
    CONFIRM_NEW_PASSWORD_INPUT = (By.CSS_SELECTOR, "input[id='change_password_confirmPassword']")
    CHANGE_PASSWORD_IN_MODAL_BUTTON = (By.CSS_SELECTOR, "button[id='change_password_Sign_in']")
    ALERT = (By.CSS_SELECTOR, "div[role='alert']")
    ERROR_UNDER_INPUT = (By.CSS_SELECTOR, "div[class='text-red subtitle2 mt-1']")


