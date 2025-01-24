# Agoda Login Automation

This project automates the login process of the Agoda website (https://www.agoda.com/en-gb/) using Selenium, Python, and Pytest. The automation includes retrieving the One-Time Password (OTP) from a mailbox to complete the login process.

## Project Structure

```
Reports/
    2025_01_24/          # Contains test execution reports
configs/
    config.properties    # Configuration file for test settings
logs/
    automation.log       # Log file for debugging and test execution details
page_objects/
    __init__.py          # Package initializer
    home_page.py         # Page Object Model for Agoda Home Page
    signin_page.py       # Page Object Model for Agoda Sign-In Page
    yopmail_page.py      # Page Object Model for Yopmail (mailbox for OTP retrieval)
test_cases/
    __init__.py          # Package initializer
    conftest.py          # Pytest configurations and fixtures
    test_login.py        # Test script for automating the login process
utilities/
    __init__.py          # Package initializer
    utilities.py         # Utility functions for reusable components
```

## Features

- Automates login to the Agoda website.
- Retrieves OTP from a mailbox (Yopmail) to complete the authentication process.
- Modular code structure using Page Object Model (POM).
- Pytest for test execution and reporting.
- Configurable settings via `config.properties`.

## Prerequisites

Ensure you have the following installed:

- Python 3.8+
- Google Chrome or any other supported browser
- Selenium
- Pytest

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/gokuldevp/Agoda_Login_Pytest_Automation-.git
   ```

2. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```
-  Note:
   Alternatively, you can install dependencies by clicking on the file run.bat

## Usage

1. Run the tests:

   ```bash
   pytest
   ```

2. View the logs in `logs/automation.log` for debugging information.

3. Check the generated HTML report in the `Reports/YYYY_MM_DD/` folder.

## Code Overview

### Key Components

- **Page Objects:**
  - `home_page.py`: Contains methods and locators for the Agoda homepage.
  - `signin_page.py`: Contains methods and locators for the Sign-In page.
  - `yopmail_page.py`: Contains methods and locators for retrieving OTP from Yopmail.

- **Test Cases:**
  - `test_login.py`: Automates the login process, including OTP retrieval.

- **Utilities:**
  - `utilities.py`: Includes helper functions for common tasks like reading configurations and logging.

- **Configurations:**
  - `config.properties`: Stores configurable parameters like url credentials and browser settings.

## Logs and Reports

- Logs: Found in `logs/automation.log`, containing detailed execution steps and errors.
- Reports: Generated in `Reports/YYYY_MM_DD/` as an HTML report after each test run.

## Contact

For any issues or questions, feel free to reach out:

- **Author:** Gokul Dev P
- **GitHub:** [https://github.com/gokuldevp](https://github.com/gokuldevp)

