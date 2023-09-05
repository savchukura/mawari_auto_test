from selenium.webdriver.common.by import By


class AdminAccountPageLocators:

    # side tabs
    DASHBOARD_TAB = (By.CSS_SELECTOR, "a[href='/']")
    ADMINS_TAB = (By.CSS_SELECTOR, "a[href='/admins']")
    ALERTS_TAB = (By.CSS_SELECTOR, "a[href='/alerts']")
    PROJECTS_TAB = (By.CSS_SELECTOR, "a[href='/projects']")
    XR_DEVELOPERS_LIST_TAB = (By.CSS_SELECTOR, "a[href='/developers']")

    # Dashboard locators

    # ADMINS TAB Locators
    ADD_ADMIN_BUTTON = (By.CSS_SELECTOR, "button[if='add_admin_btn']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[id='new_admin_email']")
    SEND_BUTTON = ()
    DELETE_BUTTON = (By.CSS_SELECTOR, "button[class='ui-max-w-[97px] button ui-flex ui-text-center ui-items-center ui-justify-center ui-ease-in-out ui-duration-150  ui-rounded-[8px] ui-select-none ui-text-black hover:ui-text-white ui-border-btnDef ui-bg-transparent hover:ui-bg-btnHover active:ui-bg-btnActive disabled:ui-border-btnDisable ui-h-[26px] ui-border-[2px] ui-w-full']")
    USER_NUMBER_AND_EMAIL = (By.CSS_SELECTOR, "span[class='ellipsis']")  # [0] is number [1] is email
    # Alerts Tab Locators

    # Projects Tab locators
    FIRST_APPROVE_BUTTON = (By.CSS_SELECTOR, "button[class='button flex select-none items-center justify-center rounded-[8px] text-center  duration-150 ease-in-out text-white bg-btnDef hover:bg-btnHover active:bg-btnActive disabled:bg-btnDisable h-[26px] w-full']")
    FIRST_DECLINE_BUTTON = (By.CSS_SELECTOR, "button[class='button flex select-none items-center justify-center rounded-[8px] text-center  duration-150 ease-in-out text-black hover:text-white border-btnDef bg-transparent hover:bg-btnHover active:bg-btnActive disabled:border-btnDisable h-[26px] w-full border-[2px]']")
    CONFIRM_DOWNLOAD_BUTTON = (By.CSS_SELECTOR, "button[class='button flex select-none items-center justify-center rounded-[8px] text-center  duration-150 ease-in-out h-auto p-[6px] m-[-6px] hover:bg-white/[.4] active:bg-white/[.8] rounded-full h-[44px]']")
    DOWNLOAD_BUTTON = (By.XPATH, "//a[@download]")
    # XR developers tab locators

