from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from utilities.utilities import ScreeShots, config_util

class YopmailPage:
    #locators
    ROOT_YOPMAILPAGE_ID = 'logoacc'
    INPUT_YOPMAIL_EMAIL_ID = 'login'
    BUTTON_YOPMAIL_EMAIL_SUBMIT_XPATH = '//div[@id="refreshbut"]//button'
    TITLE_YOPMAIL_INBOX = "Inbox"
    IFRAME_YOPMAIL_INBOX_ID = 'ifinbox'
    IFRAME_YOPMAIL_INBOX_BODY_ID = 'ifmail'
    BUTTON_AGODA_OTP_EMAIL_XPATH = '//span[text()="Agoda"]/parent::div/following-sibling::div[text()="Email OTP"]/parent::button'
    TEXT_EMAIL_BODY_XPATH = '//td[contains(text(),"Agoda OTP is")]'

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
        Load the Yopmail home page.
        """
        try:
            self._handle_logger("Attempting to load the Yopmail home page.")
            self.driver.get(config_util.get_yopmail_url())
        except (NoSuchElementException, TimeoutException) as e:
            self._handle_error({e})
            raise

    def verify_home_page_loaded(self):
        """
        Verify that the Yopmail home page has loaded.
        """
        try:
            root_element = self.wait.until(EC.presence_of_element_located((By.ID, self.ROOT_YOPMAILPAGE_ID)))
            root_displayed = root_element.is_displayed()
            assert root_displayed, "Yopmail Home page not loaded correctly."
            self._handle_logger("Yopmail home page loaded successfully.")
        except (NoSuchElementException, TimeoutException) as e:
            self._handle_error({e})
            raise

    def input_yopmail_email(self, user_email):
        """
        Enter the email address into the yopmail input field.
        """
        try:
            self._handle_logger("Attempting to Enter the email address into the sign-in yopmail input field.")
            self.wait.until(EC.presence_of_element_located((By.ID, self.INPUT_YOPMAIL_EMAIL_ID))).send_keys(user_email)
            self._handle_logger("Email entered into the yopmail input field successfully.")
        except (NoSuchElementException, TimeoutException) as e:
            self._handle_error({e})
            raise

    def click_check_yopmail_inbox(self):
        """
        Clicks the submit button to check the YOPmail inbox.
        """
        try:
            self._handle_logger("Attempting to click the YOPmail inbox submit button.")
            self.wait.until(EC.presence_of_element_located((By.XPATH, self.BUTTON_YOPMAIL_EMAIL_SUBMIT_XPATH))).click()
            self._handle_logger("YOPmail inbox submit button clicked successfully.")
        except (NoSuchElementException, TimeoutException) as e:
            self._handle_error(e)
            raise

    def verify_yopmail_inbox_page_loaded(self):
        """
        Verify that the YOPmail inbox page is loaded.
        """
        try:
            self._handle_logger("Verifying that the YOPmail inbox page is loaded.")
            root_element = self.wait.until(EC.title_contains(self.TITLE_YOPMAIL_INBOX))
            assert root_element, "YOPmail inbox page not loaded correctly."
            self._handle_logger("YOPmail inbox page loaded successfully.")
        except (NoSuchElementException, TimeoutException) as e:
            self._handle_error(e)
            raise

    def click_latest_agoda_otp_email(self):
        """
        Clicks on the latest Agoda OTP email.
        """
        try:
            self._handle_logger("Clicking on the latest Agoda OTP email.")
            self.wait.until(EC.presence_of_element_located((By.XPATH, self.BUTTON_AGODA_OTP_EMAIL_XPATH))).click()
            self._handle_logger("Latest Agoda OTP email clicked.")
        except (NoSuchElementException, TimeoutException) as e:
            self._handle_error(e)
            raise

    def retrieve_agoda_otp(self):
        """
        Retrieves the Agoda OTP from the email body.
        """
        try:
            self._handle_logger("Retrieving the Agoda OTP from the email body.")
            email_text = self.wait.until(EC.presence_of_element_located((By.XPATH, self.TEXT_EMAIL_BODY_XPATH)))
            agoda_otp = email_text.text.split()[5]
            self._handle_logger("Agoda OTP retrieved successfully.")
            return agoda_otp
        except (NoSuchElementException, TimeoutException) as e:
            self._handle_error(e)
            raise

    def switch_to_yopmail_inbox_list_iframe(self):
        """
        Switches to the yopmail inbox list iframe.
        """
        try:
            self._handle_logger("Attempting to switch to the yopmail inbox list iframe.")
            iframe = self.wait.until(EC.presence_of_element_located((By.ID, self.IFRAME_YOPMAIL_INBOX_ID)))
            self.driver.switch_to.frame(iframe)
            self._handle_logger("Switched to the yopmail inbox list iframe successfully.")
        except (NoSuchElementException, TimeoutException) as e:
            self._handle_error({e})
            raise

    def switch_to_yopmail_main_content(self):
        """
        Switch back to the main content from the YOPmail iframe.
        """
        try:
            self._handle_logger("Switching back to the main content from the YOPmail iframe.")
            self.driver.switch_to.default_content()
            self._handle_logger("Switched back to the main content successfully.")
        except (NoSuchElementException, TimeoutException) as e:
            self._handle_error(e)
            raise
    
    def switch_to_yopmail_inbox_body_iframe(self):
        """
        Switch to the YOPmail inbox body iframe.
        """
        try:
            self._handle_logger("Attempting to switch to the YOPmail inbox body iframe.")
            iframe = self.wait.until(EC.presence_of_element_located((By.ID, self.IFRAME_YOPMAIL_INBOX_BODY_ID)))
            self.driver.switch_to.frame(iframe)
            self._handle_logger("Switched to the YOPmail inbox body iframe successfully.")
        except (NoSuchElementException, TimeoutException) as e:
            self._handle_error(e)
            raise