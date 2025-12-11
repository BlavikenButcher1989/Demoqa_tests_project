import time

from pages.base_page import BasePage
from locators.elements_page_locators import TextBoxPageLocators
from locators.elements_page_locators import CheckBoxPageLocators
from generator.generator import generator_person

import random


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        full_name = next(generator_person()).full_name
        email = next(generator_person()).email
        current_address = next(generator_person()).current_address
        permanent_address = next(generator_person()).permanent_address

        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        self.element_is_visible(self.locators.SUBMIT).click()

        return full_name, email, current_address, permanent_address

    def get_text(self, locator):
        return self.element_is_visible(locator).text.split(':')[1]

    def check_field_form(self):
        full_name = self.get_text(self.locators.RESULT_NAME)
        email = self.get_text(self.locators.RESULT_EMAIL)
        current_address = self.get_text(self.locators.RESULT_CUR_ADDRESS)
        permanent_address = self.get_text(self.locators.RESULT_PER_ADDRESS)

        return full_name, email, current_address, permanent_address


class CheckBoxPage(BasePage):
    locators = CheckBoxPageLocators()

    def open_full_list(self):
        self.element_is_visible(self.locators.EXPAND_ALL_BUTTON).click()

    def click_random_checkbox(self):
        item_list = self.elements_are_visible(self.locators.ITEM_LIST)

        for item in random.sample(item_list, random.randint(1, len(item_list))):
            self.go_to_element(item)
            item.click()

    def get_checked_checkboxes(self):
        checked_list = self.elements_are_visible(self.locators.CHECKED_ITEMS)
        data = [box.find_element(*self.locators.TITLE_ITEM).text.lower().replace(' ', '').replace('.doc', '') for box in
                checked_list]

        return data

    def get_output_result(self):
        result_text = self.elements_are_visible(self.locators.ITEM_RESULT_LIST)
        result_list = [i.text.lower().replace(' ', '') for i in result_text]

        return result_list
