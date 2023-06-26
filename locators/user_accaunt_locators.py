from selenium.webdriver.common.by import By


class NodeRunnerAccountLocators:
    DASHBOARD_TAB = (By.CSS_SELECTOR, "a[href='/runners/dashboard")
    NODES_LIST_TAB = (By.CSS_SELECTOR, "a[href='/runners/nodes")
    REWARDS_TAB = (By.CSS_SELECTOR, "a[href='/runners/rewards")
    SYSTEM_ALERTS_TAB = (By.CSS_SELECTOR, "a[href='/runners/alerts")
    TERMS_AND_POLICIES_TAB = (By.CSS_SELECTOR, "a[href='/runners/policies")
    API_KEY_TAB = (By.CSS_SELECTOR, "a[href='/runners/api")
    USER_DETAIL = (By.CSS_SELECTOR, "p[class='subtitle2 ui-uppercase ellipsis']")

    # User Details Page
    CHANGE_PASSWORD = (By.CSS_SELECTOR, "button[id='change_password']")
    TWO_FA_TOGGLE = (By.CSS_SELECTOR, "div[class='ui-w-[29px] ui-h-[14px] ui-rounded-[16px] ui-relative ui-bg-[#B6B4B5] ui-cursor-pointer']")
    TWO_FA_TOGGLE_ON = (By.CSS_SELECTOR, "div[class='ui-w-[29px] ui-h-[14px] ui-rounded-[16px] ui-relative ui-bg-[#9439FF] ui-cursor-pointer']")

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

    # Dashboard locators

    # Nodes List locators
    ADD_NODE_BUTTON = (By.CSS_SELECTOR, "button[id='Add-Node']")
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[id='search_node']")

    FILTERING_BY_DROP_DOWN = (By.XPATH, "//h5[contains(text(),'Filtering by')]")
    RUNNING_FILTER = (By.XPATH, "//span[contains(text(),'Running')]")
    PAUSED_FILTER = (By.XPATH, "//span[contains(text(),'Paused')]")
    OFFLINE_FILTER = (By.XPATH, "//span[contains(text(),'Offline')]")

    # Rewards locators

    # System alerts locators

    # Terms and Policies locators

    # Api Key locators


class DeveloperLocators:

    MY_PROJECTS_TAB = (By.CSS_SELECTOR, "a[href='/developers/projects']")
    MANAGE_ACCOUNT_TAB = (By.CSS_SELECTOR, "a[href='/developers/account']")
    API_AND_DOCUMENTATION_TAB = (By.CSS_SELECTOR, "a[href='/developers/documentation']")
    BALANCES_TAB = (By.CSS_SELECTOR, "a[href='/developers/balances']")

    # My Project tab



    # Manage Account tab

    # API & Documentation tab

    # Balances tab

    DEPOSIT_BUTTON = (By.CSS_SELECTOR, "button[id='deposit_btn']")
    DEPOSIT_AMOUNT_INPUT = (By.CSS_SELECTOR, "input[id='daposit_Amount']")
    BALANCE_COUNT_FIELD = (By.CSS_SELECTOR, "p[class='textnumber1 ui-text-purple']")
    SORTING_COLUMN_BUTTONS = (By.CSS_SELECTOR, "button[class='ui-flex ui-w-max ui-mx-auto subtitle1']")

