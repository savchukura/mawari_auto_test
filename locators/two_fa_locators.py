from selenium.webdriver.common.by import By


class TwoFaLocators:

    USER_DETAIL = (By.CSS_SELECTOR, "p[class='subtitle2 ui-uppercase ellipsis']")
    TWO_FA_TOGGLE = (By.CSS_SELECTOR,
                     "div[class='ui-w-[29px] ui-h-[14px] ui-rounded-[16px] ui-relative ui-bg-[#B6B4B5] ui-cursor-pointer']")
    TWO_FA_TOGGLE_ON = (By.CSS_SELECTOR,
                        "div[class='ui-w-[29px] ui-h-[14px] ui-rounded-[16px] ui-relative ui-bg-[#9439FF] ui-cursor-pointer']")

    TOTP_CODE = (By.CSS_SELECTOR, "p[class='bg-input mt-4 rounded-[8px] px-3 py-2 text-center']")
    CONTINUE_FA_BUTTON = (By.CSS_SELECTOR, "button[id='continue-twofa-modal']")

    VERIFY_INPUT_ONE = (By.CSS_SELECTOR, "input[aria-label='Please enter OTP character 1']")
    VERIFY_INPUT_TWO = (By.CSS_SELECTOR, "input[aria-label='Please enter OTP character 2']")
    VERIFY_INPUT_THREE = (By.CSS_SELECTOR, "input[aria-label='Please enter OTP character 3']")
    VERIFY_INPUT_FOUR = (By.CSS_SELECTOR, "input[aria-label='Please enter OTP character 4']")
    VERIFY_INPUT_FIVE = (By.CSS_SELECTOR, "input[aria-label='Please enter OTP character 5']")
    VERIFY_INPUT_SIX = (By.CSS_SELECTOR, "input[aria-label='Please enter OTP character 6']")

    VERIFY_CODE_BUTTON = (By.CSS_SELECTOR, "button[id='continue-twofa-modal']")

    VERIFY_TWO_FA_AFTER_LOGIN = (By.CSS_SELECTOR, "button[id='Verify_totp']")

    VERIFY_TWO_FA_DELETE = (By.CSS_SELECTOR, "button[id='Verify_totp']")

    VALIDATION_ALERT = (By.CSS_SELECTOR, "div[role='alert']")