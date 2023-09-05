from selenium.webdriver.common.by import By


class MyProjectsLocators:
    ADD_PROJECT_BUTTON = (By.CSS_SELECTOR, "button[id='Add project']")
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[name='search']")
    SORTING_BY_STATUS_BUTTONS = (By.CSS_SELECTOR, "div[role='button']")
    UPDATE_PROJECT_BUTTON = (By.CSS_SELECTOR,
                             "button[class='button flex select-none items-center justify-center rounded-[8px] text-center  duration-150 ease-in-out h-auto p-[6px] m-[-6px] hover:bg-white/[.4] active:bg-white/[.8] rounded-full h-[26px]']")
    DELETE_PROJECT_BUTTON = (By.CSS_SELECTOR,
                             "button[class='button flex select-none items-center justify-center rounded-[8px] text-center  duration-150 ease-in-out h-auto p-[6px] m-[-6px] hover:bg-white/[.4] active:bg-white/[.8] rounded-full h-[26px]']")
    UPDATE_PROJECT_DATA_BUTTON = (By.CSS_SELECTOR,
                             "button[class='button flex select-none items-center justify-center rounded-[8px] text-center  duration-150 ease-in-out h-auto p-[6px] m-[-6px] hover:bg-white/[.4] active:bg-white/[.8] rounded-full h-[26px]']")
    PROJECT_ID = (By.CSS_SELECTOR, "td[class='text-left']")
    PROJECT_NAME = (By.CSS_SELECTOR, "td[class='text-center']")
    PROJECT_STATUS_FIELDS = (By.CSS_SELECTOR, "span[class='ellipsis capitalize']")
    PROJECT_REGION = (By.CSS_SELECTOR, "td[class='text-center']")
    PROJECT_DATE = (By.CSS_SELECTOR, "td[class='text-center']")
    PROJECT_DESCRIPTION = (By.CSS_SELECTOR, "td[class='w-[40%]']")
    ALERT = (By.CSS_SELECTOR, "div[role='alert']")


    # create project first Modal

    NAME_INPUT = (By.CSS_SELECTOR, "input[id='create_project_name']")
    CATEGORY_DROP = (By.CSS_SELECTOR, "div[class='shadow-input bg-input relative flex select-none items-center px-[13px] py-[10px] rounded-[10px] h-[36px]']")
    REGION_DROP = (By.CSS_SELECTOR, "div[class='shadow-input bg-input relative flex select-none items-center px-[13px] py-[10px] rounded-[10px] h-[36px]']")
    CATEGORY = (By.CSS_SELECTOR, "div[class='ui-px-[10px] ui-py-[6px] h2 ui-border-b-[1px] ui-border-grey hover:ui-bg-lightgrey']")
    ENTERTAINMENT_CATEGORY = (By.XPATH, "//*[contains(text(), 'Entertainment')]")
    GAME_CATEGORY = (By.XPATH, "//*[contains(text(), 'Game')]")
    OTHER_CATEGORY = (By.XPATH, "//*[contains(text(), 'Other')]")

    EUROPE_REGION = (By.XPATH, "//div[@class='h2 border-grey hover:bg-lightgrey border-b-[1px] px-[10px] py-[6px]'] //*[contains(text(), 'Europe')]")
    US_REGION = (By.XPATH, "//div[@class='h2 border-grey hover:bg-lightgrey border-b-[1px] px-[10px] py-[6px]'] //*[contains(text(), 'US')]")
    ASIA_REGION = (By.XPATH, "//div[@class='h2 border-grey hover:bg-lightgrey border-b-[1px] px-[10px] py-[6px]'] //*[contains(text(), 'Asia')]")

    REGION = (By.CSS_SELECTOR, "div[class='h2 border-grey hover:bg-lightgrey border-b-[1px] px-[10px] py-[6px]']")

    DESCRIPTION_TEXT_AREA = (By.CSS_SELECTOR, "textarea[id='project_description']")
    NEXT_BUTTON = (By.CSS_SELECTOR, "button[id='CreateProjectModal-Next']")
    CANCEL_BUTTON = (By.CSS_SELECTOR, "button[id='CreateProjectModal-Cancel']")

    # create project second modal

    GPU_CPU_RAM_DROP = (By.CSS_SELECTOR, "div[class='shadow-input bg-input relative flex select-none items-center px-[13px] py-[10px] rounded-[10px] h-[36px]']")

    GPU_ENTRY = (By.XPATH, "//*[contains(text(), 'Entry Level Performance')]")
    GPU_LOWER_MID = (By.XPATH, "//*[contains(text(), 'Lower Mid-range Performance')]")
    GPU_MID = (By.XPATH, "//*[contains(text(), 'Mid-range Performance')]")
    GPU_UPPER_MID = (By.XPATH, "//*[contains(text(), 'Upper Mid-range Performance')]")
    GPU_HIGH = (By.XPATH, "//*[contains(text(), 'High Performance')]")

    CPU_1_4 = (By.XPATH, "//*[contains(text(), '1-4')]")
    CPU_5_8 = (By.XPATH, "//*[contains(text(), '5-8')]")
    CPU_9_16 = (By.XPATH, "//*[contains(text(), '9-16')]")
    CPU_16 = (By.XPATH, "//*[contains(text(), '16+')]")

    RAM_8_16 = (By.XPATH, "//*[contains(text(), '8-16')]")
    RAM_17_32 = (By.XPATH, "//*[contains(text(), '17-32')]")
    RAM_33_64 = (By.XPATH, "//*[contains(text(), '33-64')]")
    RAM_64 = (By.XPATH, "//*[contains(text(), '64+')]")

    NEXT_BUTTON_SECOND = (By.CSS_SELECTOR, "button[id='SystemRequirementsForm-Next']")
    BACK_BUTTON = (By.CSS_SELECTOR, "button[id='SystemRequirementsForm-Back']")

    # create project third modal

    TOGGLE_ON_BUTTON = (By.CSS_SELECTOR, "div[class='w-[15px] h-[12px] absolute top-[1px] rounded-[16px] bg-white ease-in-out duration-300 left-[13px]']")
    TOGGLE_OFF_BUTTON = (By.CSS_SELECTOR,
                        "div[class='ui-w-[29px] ui-h-[14px] ui-rounded-[16px] ui-relative ui-bg-[#B6B4B5] ui-cursor-pointer']")
    FIXED_INPUT = (By.CSS_SELECTOR, "input[name='balance']")
    NEXT_BUTTON_THIRD = (By.CSS_SELECTOR, "button[id='SystemRequirementsForm-Next']")

    # create project fourth modal

    FILE_INPUT = (By.XPATH, "//input[@tabindex='-1']")
    UPLOAD_BUTTON = (By.CSS_SELECTOR, "button[id='CreateProjectModal-Upload']")
    FILE_NAME = (By.CSS_SELECTOR, "p[class='subtitle2 ui-text-center']")

    # Create Project Uploading menu

    PROGRESS_STATUS_BY_PERCENT = (By.CSS_SELECTOR, "p[class='subtitle3']")
    PROGRESS_STATUS_BAR = (By.CSS_SELECTOR, "div[class='border-purple relative h-1 overflow-hidden rounded-[4px] border']")


