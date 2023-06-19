from selenium.webdriver.common.by import By


class AdminAccountLocators:

    # tabs
    DASHBOARD_TAB = (By.CSS_SELECTOR, "a[href='/']")
    ADMINS_TAB = (By.CSS_SELECTOR, "a[href='/admins']")
    ALERTS_TAB = (By.CSS_SELECTOR, "a[href='/alerts']")
    PROJECTS_TAB = (By.CSS_SELECTOR, "a[href='/projects']")
    XR_DEVELOPERS_LIST_TAB = (By.CSS_SELECTOR, "a[href='/developers']")

    # Dashboard tab

    # Admins Tab
    ADD_ADMIN_BUTTON = (By.CSS_SELECTOR, "button[id='add_admin_btn']")
    NEW_ADMIN_EMAIL_INPUT = (By.CSS_SELECTOR, "input[id='new_admin_email']")
    SEND_BUTTON = (By.CSS_SELECTOR, "button[id='Send_email_new_admin']")
    # Alerts tab

    # Project tab

    # Developers tab

