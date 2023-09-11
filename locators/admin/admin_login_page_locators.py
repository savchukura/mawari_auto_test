from selenium.webdriver.common.by import By


class AdminLoginPageLocators:

    LOGIN_INPUT = (By.CSS_SELECTOR, "input[id='login_email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[id='login_password']")
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, "button[class='button flex select-none items-center justify-center rounded-[8px] text-center  duration-150 ease-in-out text-white bg-btnDef hover:bg-btnHover active:bg-btnActive disabled:bg-btnDisable h-[44px] w-full']")
    ERROR = (By.CSS_SELECTOR, "div[class='text-red subtitle2 mt-1']")

