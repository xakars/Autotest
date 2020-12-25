from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def add_to_basket(self):
        add_element = self.browser.find_element(*ProductPageLocators.ADD_BASK)
        add_element.click()
    
    def should_be_product_page(self):
        self.should_be_message_adding()
        self.price_check()
#        self.should_not_be_success_message()
#        self.should_be_disappeared_success_message()
    
    def should_be_message_adding(self):
        assert self.is_element_present(*ProductPageLocators.NAME_PRODUCT), "Product name is not presented"
        assert self.is_element_present(*ProductPageLocators.MESSAGE_ABOUT_ADD), "Message about adding is not presented"
        text_product = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text
        text_message = self.browser.find_element(*ProductPageLocators.MESSAGE_ABOUT_ADD).text
        assert text_product == text_message, f"Product name not found in the message"
    
    def price_check(self):
        assert self.is_element_present(*ProductPageLocators.PRICE_PRODUCT), "Product price is not presented"
        assert self.is_element_present(*ProductPageLocators.MESSAGE_ABOUT_TOTAL_PRICE), "Message about price is not presented"
        price_product = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
        total_price = self.browser.find_element(*ProductPageLocators.MESSAGE_ABOUT_TOTAL_PRICE).text
        assert price_product == total_price, "Price product not equal total price"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_ABOUT_ADD), "Success message is presented, but should not be"

    def should_be_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_ABOUT_ADD), "Success message is not disappeared, but should be"

