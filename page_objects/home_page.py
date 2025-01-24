from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from utilities.utilities import ScreeShots, config_util

class HomePage:
    #locators
    IDENTIFY_HOMEPAGE_TITLE = 'Agoda Official Site | Free Cancellation & Booking Deals | Over 2 Million Hotels'
    LINK_SIGNIN_XPATH = '//button[@data-element-name="sign-in-button"]'
    IFRAME_GOOGLE_POPUP_XPATH = '//iframe[@title="Sign in with Google Dialogue"]'
    BUTTON_CLOSE_IFRAME_GOOGLE_POPUP_ID = 'close'

    
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

    # Actions
    def load_home_page(self):
        """
        Load the Agoda home page.
        """
        try:
            self._handle_logger("Attempting to load the Agoda home page.")
            self.driver.get(config_util.get_agoda_url())
        except (NoSuchElementException, TimeoutException) as e:
            self._handle_error({e})
            raise

    def verify_home_page_loaded(self):
        """
        Verify that the home page has loaded.
        """
        try:
            root_element = self.wait.until(EC.title_contains(self.IDENTIFY_HOMEPAGE_TITLE))
            self._handle_logger("Agoda home page loaded successfully.")
        except (NoSuchElementException, TimeoutException) as e:
            self._handle_error({e})
            raise

    def close_firefox_Sign_in_with_google_dialogue_popup(self):
        """
        Closes the Sign In with Google dialogue popup on Firefox.
        """
        try:
            self._handle_logger("Attempting to close the 'Sign In with Google' dialogue popup.")
            if self.browser_name == "firefox":
                iframe = self.wait.until(EC.presence_of_element_located((By.XPATH, self.IFRAME_GOOGLE_POPUP_XPATH)))
                self.driver.switch_to.frame(iframe)
                self.driver.find_element(By.ID, self.BUTTON_CLOSE_IFRAME_GOOGLE_POPUP_ID).click()
                self.driver.switch_to.default_content()
            self._handle_logger("Successfully closed the 'Sign In with Google' dialogue popup if available.")
        except (NoSuchElementException, TimeoutException) as e:
            pass

    def click_on_signin_link(self):
        """
        Clicks on the Sign In link.
        """
        try:
            self._handle_logger("Attempting to click on the Sign In link.")
            signin_link = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.LINK_SIGNIN_XPATH)))
            signin_link.click()
            self._handle_logger("Sign In link clicked successfully.")
        except (NoSuchElementException, TimeoutException) as e:
            self._handle_error({e})
            raise

    def verify_sign_in_link_not_available(self):
        """
        Verify that the Sign In link is not available.
        """
        try:
            self._handle_logger("Checking if the Sign In link is not available.")
            self.wait.until(EC.invisibility_of_element_located((By.XPATH, self.LINK_SIGNIN_XPATH)))
            self._handle_logger("Confirmed: Sign In link is not available.")
        except (NoSuchElementException, TimeoutException) as e:
            self._handle_error({e})
            raise