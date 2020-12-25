from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOG_FORM = (By.CSS_SELECTOR, "#login_form")
    REG_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_BASK = (By.CSS_SELECTOR, "#add_to_basket_form")
    NAME_PRODUCT = (By.CSS_SELECTOR, ".product_main h1")
    PRICE_PRODUCT = (By.CSS_SELECTOR, ".product_main .price_color")
    MESSAGE_ABOUT_ADD = (By.CSS_SELECTOR, ".alert:nth-child(1) strong")
    MESSAGE_ABOUT_TOTAL_PRICE = (By.CSS_SELECTOR, ".alert:nth-child(3) strong")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR,".btn-group a")

class BasketPageLocators():
    BASKET_ITEM = (By.CSS_SELECTOR, "#basket_formset")
    MESSAGE_ABOUT_CLEAR_BASKET = (By.CSS_SELECTOR, "#content_inner")
