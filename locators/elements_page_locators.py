from selenium.webdriver.common.by import By



class TextBoxPageLocators:

    FULL_NAME = (By.CSS_SELECTOR, 'input[id="userName"]')
    EMAIL = (By.CSS_SELECTOR, 'input[id="userEmail"]')
    CURRENT_ADDRESS = (By.CSS_SELECTOR, 'textarea[id="currentAddress"]')
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, 'textarea[id="permanentAddress"]')
    SUBMIT = (By.CSS_SELECTOR, 'button[id="submit"]')


    RESULT_NAME = (By.CSS_SELECTOR, 'p[id="name"]')
    RESULT_EMAIL = (By.CSS_SELECTOR, 'p[id="email"]')
    RESULT_CUR_ADDRESS = (By.CSS_SELECTOR, 'p[id="currentAddress"]')
    RESULT_PER_ADDRESS = (By.CSS_SELECTOR, 'p[id="permanentAddress"]')

class CheckBoxPageLocators:

    EXPAND_ALL_BUTTON = (By.CSS_SELECTOR, 'button[title="Expand all"]')
    ITEM_LIST = (By.CSS_SELECTOR, 'span[class="rct-title"]')
    CHECKED_ITEMS = (By.CSS_SELECTOR, 'svg[class="rct-icon rct-icon-check"]')
    TITLE_ITEM = (By.XPATH, './/ancestor::span[@class="rct-text"]')
    ITEM_RESULT_LIST = (By.CSS_SELECTOR, 'span[class="text-success"]')