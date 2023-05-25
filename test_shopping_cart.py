from pages.log_reg_page import LoginPage
from pages.shopping_cart_page import ShoppingCart
from pages.links import main_page_link
from data.data_registration import DataRegistrationAndLoginUser_2
from data.data_shopping_cart import DataShoppingCart
import pytest


@pytest.mark.run(order=7)
@pytest.mark.shopping_cart_test(scope='class')
class TestShoppingCart():
    
    @pytest.mark.subscription_test
    @pytest.mark.parametrize('data', DataShoppingCart.RECIPE_NAME)
    def test_shopping_cart(self, browser, data):
        page = LoginPage(browser, main_page_link)
        page.open()
        page.login_user(DataRegistrationAndLoginUser_2.valid_data_login)
        page_shopping_cart = ShoppingCart(browser, browser.current_url)
        page_shopping_cart.add_shopping_cart(data)