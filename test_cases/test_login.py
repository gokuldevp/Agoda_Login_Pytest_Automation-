from faker import Faker
import pytest
from page_objects.home_page import HomePage
from page_objects.signin_page import SignInPage
from page_objects.yopmail_page import YopmailPage
from utilities.utilities import generate_test_data

@pytest.mark.usefixtures("setup")
class TestLogin:
    agoda_otp = None

    @pytest.fixture(autouse=True)
    def setup_pages(self):
        self.homepage = HomePage(self.driver, self.logger)
        self.signinpage = SignInPage(self.driver, self.logger)
        self.yopmail = YopmailPage(self.driver, self.logger)

    @pytest.mark.dependency(name='test_load_and_verify_home_page')
    def test_load_and_verify_home_page(self):
        self.homepage.load_home_page()
        self.homepage.verify_home_page_loaded()

    @pytest.mark.dependency(depends=['test_load_and_verify_home_page'], name='test_navigate_to_sign_in_page')
    def test_navigate_to_sign_in_page(self):
        self.homepage.close_firefox_Sign_in_with_google_dialogue_popup()
        self.homepage.click_on_signin_link()
        self.signinpage.verify_sign_in_page_loaded()

    @pytest.mark.dependency(depends=['test_navigate_to_sign_in_page'], name='test_submit_email_and_verify_otp_page')
    def test_submit_email_and_verify_otp_page(self):
        self.signinpage.switch_to_login_iframe()
        TestLogin.first_name,TestLogin.last_name,TestLogin.email = generate_test_data()
        self.signinpage.input_signin_email(TestLogin.email)
        self.signinpage.submit_signin_form()
        self.signinpage.input_profile_firstname(TestLogin.first_name)
        self.signinpage.input_profile_lastname(TestLogin.last_name)
        self.signinpage.submit_profile_details()
        self.signinpage.verify_sign_in_otp_page_loaded()

    @pytest.mark.dependency(depends=['test_submit_email_and_verify_otp_page'], name='test_verify_otp_email_in_yopmail_inbox')
    def test_verify_otp_email_in_yopmail_inbox(self):
        self.driver.execute_script("window.open('');")
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.yopmail.load_home_page()
        self.yopmail.input_yopmail_email(TestLogin.email)
        self.yopmail.click_check_yopmail_inbox()
        self.yopmail.verify_yopmail_inbox_page_loaded()
        self.yopmail.switch_to_yopmail_inbox_list_iframe()
        self.yopmail.click_latest_agoda_otp_email()
        self.yopmail.switch_to_yopmail_main_content()
        self.yopmail.switch_to_yopmail_inbox_body_iframe()
        TestLogin.agoda_otp = self.yopmail.retrieve_agoda_otp()

    @pytest.mark.dependency(depends=['test_verify_otp_email_in_yopmail_inbox'], name='test_verify_submitting_otp_in_signin_with_otp')
    def test_verify_submitting_otp_in_signin_with_otp(self):
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.signinpage.input_signin_otp(TestLogin.agoda_otp)
        self.signinpage.submit_opt_in_signin_form()
        self.homepage.verify_home_page_loaded()
        self.homepage.verify_sign_in_link_not_available()