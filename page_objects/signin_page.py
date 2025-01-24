from time import sleep
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.utilities import ScreeShots, config_util

class SignInPage:
    #locators
    ROOT_SIGNIN_ID = 'mmb-signin-root'
    IFRAME_LOGIN_XPATH = '//iframe[@data-cy="ul-app-frame"]'
    INPUT_SIGNIN_EMAIL_XPATH = '//input[@data-cy="unified-email-input"]'
    BUTTON_EMAIL_SUBMIT_XPATH = '//button[@data-cy="unified-email-continue-button"]'

    INPUT_SIGNIN_FIRSTNAME_XPATH = '//input[@data-cy="profile-firstname"]'
    INPUT_SIGNIN_LASTNAME_XPATH = '//input[@data-cy="profile-lastname"]'
    BUTTON_PROFILE_SUBMIT_XPATH = '//button[@data-cy="profile-continue-button"]'

    OTP_PAGE_INDICATOR_XPATH = '//div[@data-cy="form-heading"]//h2[text()="Sign in with OTP"]'
    INPUT_OTP_NAME = 'otp-'
    BUTTON_OTP_SUBMIT_XPATH = '//button[@data-cy="unified-auth-otp-continue-button"]'
    ELEMENT_USER_NAME_XPATH = '//span[@data-element-name="user-name"]'
    CHECKBOX_CAPTCHA_CSS_SELECTOR = '#recaptcha-anchor'
    
    def __init__(self, driver, logger):
        # Initialize WebDriver, WebDriverWait, Screenshots, and Logger
        self.driver = driver
        self.wait = WebDriverWait(self.driver, config_util.get_timeout(), 2)
        self.SS = ScreeShots(self.driver)
        self.logger = logger
        self.browser_name = self.driver.capabilities['browserName']

    def _handle_logger(self, info):
        # Log information messages
        self.logger.info(f"Info :: {self.browser_name} :: {info}")

    def _handle_error(self, error):
        # error information messages
        self.logger.error(f"Error :: {self.browser_name} :: {error}")
        

    def verify_sign_in_page_loaded(self):
        """
        Verify that the user is on the Sign In page.
        """
        try:
            self._handle_logger("Attempting to verify if user successfully navigated to the Sign In page.")
            self.wait.until(EC.presence_of_element_located((By.XPATH, self.IFRAME_LOGIN_XPATH)))
            self._handle_logger("Sign In page loaded successfully.")
        except (NoSuchElementException, TimeoutException) as e:
            self._handle_error({e})
            raise

    def switch_to_login_iframe(self):
        """
        Switches to the login iframe.
        """
        try:
            self._handle_logger("Attempting to switch to the login iframe.")
            iframe = self.wait.until(EC.presence_of_element_located((By.XPATH, self.IFRAME_LOGIN_XPATH)))
            self.driver.switch_to.frame(iframe)
            self._handle_logger("Switched to the login iframe successfully.")
        except (NoSuchElementException, TimeoutException) as e:
            self._handle_error({e})
            raise

    def input_signin_email(self, user_email):
        """
        Enter the email address into the sign-in form.
        """
        try:
            self._handle_logger("Attempting to Enter the email address into the sign-in email input field.")
            self.wait.until(EC.presence_of_element_located((By.XPATH, self.INPUT_SIGNIN_EMAIL_XPATH))).send_keys(user_email)
            self._handle_logger("Email entered into the sign-in form successfully.")
        except (NoSuchElementException, TimeoutException) as e:
            self._handle_error({e})
            raise

    def submit_signin_form(self):
        """
        Clicks the submit button on the sign-in form.
        """
        try:
            self._handle_logger("Clicking on the sign-in submit button.")
            self.wait.until(EC.presence_of_element_located((By.XPATH, self.BUTTON_EMAIL_SUBMIT_XPATH))).click()
            self._handle_logger("Sign-in submit button clicked.")
        except (NoSuchElementException, TimeoutException) as e:
            self._handle_error(e)
            raise

    def input_profile_firstname(self, user_firstname):
        """
        Inputs the first name into the profile first name field.
        """
        try:
            self._handle_logger("Entering first name")
            self.wait.until(EC.presence_of_element_located((By.XPATH, self.INPUT_SIGNIN_FIRSTNAME_XPATH))).send_keys(user_firstname)
            self._handle_logger("First name entered successfully")
        except (NoSuchElementException, TimeoutException) as e:
            self._handle_error({e})
            self._handle_logger(f"Error occurred while entering first name: {e}")
            raise

    def input_profile_lastname(self, user_lastname):
        """
        Inputs the last name into the profile last name field.
        """
        try:
            self._handle_logger("Entering last name")
            self.wait.until(EC.presence_of_element_located((By.XPATH, self.INPUT_SIGNIN_LASTNAME_XPATH))).send_keys(user_lastname)
            self._handle_logger("Last name entered successfully")
        except (NoSuchElementException, TimeoutException) as e:
            self._handle_error({e})
            self._handle_logger(f"Error occurred while entering last name: {e}")
            raise

    def submit_profile_details(self):
        """
        Submits the profile details form.
        """
        try:
            self._handle_logger("Submitting profile details")
            self.wait.until(EC.presence_of_element_located((By.XPATH, self.BUTTON_PROFILE_SUBMIT_XPATH))).click()
            self._handle_logger("Profile details submitted successfully")
        except (NoSuchElementException, TimeoutException) as e:
            self._handle_error(e)
            self._handle_logger(f"Error occurred while submitting profile details: {e}")
            raise

    def verify_sign_in_otp_page_loaded(self):
        """
        Verify that the OTP sign-in page is loaded.
        """
        try:
            self._handle_logger("Verifying that the OTP sign-in page is loaded.")
            self.wait.until(EC.presence_of_element_located((By.XPATH, self.OTP_PAGE_INDICATOR_XPATH)))
            self._handle_logger("OTP sign-in page is successfully loaded.")
        except (NoSuchElementException, TimeoutException) as e:
            self._handle_error(e)
            raise

    def input_signin_otp(self, otp):
        """
        Enter the provided OTP (One-Time Password) into the sign-in form.
        
        Args:
            otp (str): The OTP to be entered, expected to be a 6-digit string.
        """
        try:
            self._handle_logger("Entering the OTP into the sign-in form.")
            self.switch_to_login_iframe()
            for i in range(6):
                INPUT_OTP_NAME = self.INPUT_OTP_NAME + str(i)
                self.wait.until(EC.presence_of_element_located((By.NAME, INPUT_OTP_NAME))).send_keys(otp[i])
            self._handle_logger("OTP entered successfully.")
        except (NoSuchElementException, TimeoutException) as e:
            self._handle_error(e)
            raise

    def submit_opt_in_signin_form(self):
        """
        This method handles the opt-in sign-in form submission process.
        """
        try:
            self._handle_logger("Attempting to submit the opt-in sign-in form.")
            self.wait.until(EC.presence_of_element_located((By.XPATH, self.BUTTON_OTP_SUBMIT_XPATH))).click()
        except (NoSuchElementException, TimeoutException) as e:
            self._handle_error(e)
            raise

    def verify_user_logged_in(self):
        """
        This method checks if the user is logged in by verifying the presence of the user menu.
        """
        try:
            self._handle_logger("Attempting to verify if the user is logged in.")
            user_element = self.wait.until(EC.presence_of_element_located((By.XPATH, self.ELEMENT_USER_NAME_XPATH)))
            isUserLoggedIn = user_element.is_displayed()

            assert isUserLoggedIn, "User menu not loaded correctly."
            self._handle_logger("User is logged in successfully.")
        except (NoSuchElementException, TimeoutException) as e:
            self._handle_error(e)
            raise