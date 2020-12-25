from .locators import BasketPageLocators
from .base_page import BasePage


class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.should_be_clear_basket()
        self.should_be_message_about_clear_basket()
    def should_be_clear_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM), "Busket is't clear"
    def should_be_message_about_clear_basket(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_ABOUT_CLEAR_BASKET), "no message about empty basket"
