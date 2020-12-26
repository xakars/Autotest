from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import RegistrationPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, "login not found in link"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOG_FORM), "Login formis not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        email_in = self.browser.find_element(*RegistrationPageLocators.EMAIL_AREA)
        email_in.send_keys(email)
        password_in = self.browser.find_element(*RegistrationPageLocators.PASSWORD_AREA)
        password_in.send_keys(password)
        confirm_password = self.browser.find_element(*RegistrationPageLocators.PASSWORD_AREA_Confirm)
        confirm_password.send_keys(password)
        register_button = self.browser.find_element(*RegistrationPageLocators.REGISTER_BUTTON)
        register_button.click()
