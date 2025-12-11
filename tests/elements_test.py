import time

from pages.elements_page import TextBoxPage
from pages.elements_page import CheckBoxPage

class TestElements:
    def test_text_box(self, driver):
        text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
        text_box_page.open_page()
        full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
        output_name, output_email, output_cur_address, output_per_address = text_box_page.check_field_form()
        assert full_name == output_name, 'full name does not match'
        assert email == output_email, 'email does not match'
        assert current_address == output_cur_address, 'current address does not match'
        assert permanent_address == output_per_address, 'permanent address does not match'


    def test_check_box(self, driver):
        check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
        check_box_page.open_page()
        check_box_page.open_full_list()
        check_box_page.click_random_checkbox()
        input_checkbox = check_box_page.get_checked_checkboxes()
        output_result = check_box_page.get_output_result()
        assert input_checkbox == output_result, 'checkboxes have not been selected'