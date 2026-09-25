from selenium.webdriver.common.by import By

class LoginPage:
    # --- Locators ---
    # Username input field
    USERNAME_INPUT = (By.XPATH, "//input[@name='username' and @placeholder='Username']")
    
    # Password input field
    PASSWORD_INPUT = (By.XPATH, "//input[@name='password' and @placeholder='Password']")
    
    # Login submit button
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit' and contains(@class, 'orangehrm-login-button')]")
    
    # Company branding image (heading)
    BRANDING_IMAGE = (By.XPATH, "//div[contains(@class, 'orangehrm-login-branding')]/img[@alt='company-branding']")
    
    # Forgot password link
    FORGOT_PASSWORD_LINK = (By.XPATH, "//p[contains(@class, 'orangehrm-login-forgot-header')]")
    
    # Reset Password button
    RESET_PASSWORD_BUTTON = (By.XPATH, "//button[@type='submit' and contains(@class, 'orangehrm-forgot-password-button--reset')]")
    
    # Cancel Reset Password button
    CANCEL_PASSWORD_BUTTON = (By.XPATH, "//button[@type='button' and contains(@class, 'orangehrm-forgot-password-button--cancel')]")
    
    # Username input on the Reset Password page
    RESET_PASSWORD_USERNAME_INPUT = (By.XPATH, "//input[@name='username' and @placeholder='Username']")
    
    # Reset Password title heading
    RESET_PASSWORD_TITLE = (By.XPATH, "//h6[contains(@class, 'orangehrm-forgot-password-title')]")

    def __init__(self, driver):
        self.driver = driver

    # --- Generic Verification Methods ---
    def is_visible(self, locator):
        """Generic method check karne ke liye ki koi element uske locator ke hisaab se visible hai ya nahi."""
        return self.driver.find_element(*locator).is_displayed()

    def is_enabled(self, locator):
        """Generic method check karne ke liye ki koi element uske locator ke hisaab se enabled hai ya nahi."""
        return self.driver.find_element(*locator).is_enabled()

    # --- Combined Verification Methods ---
    def are_all_elements_visible(self):
        """Check karta hai ki username, password, aur login button page par visible hain ya nahi."""
        return (self.is_visible(self.USERNAME_INPUT) and 
                self.is_visible(self.PASSWORD_INPUT) and 
                self.is_visible(self.LOGIN_BUTTON))

    def are_all_elements_enabled(self):
        """Check karta hai ki username, password, aur login button enable/interactable hain ya nahi."""
        return (self.is_enabled(self.USERNAME_INPUT) and 
                self.is_enabled(self.PASSWORD_INPUT) and 
                self.is_enabled(self.LOGIN_BUTTON))

    # --- Action Methods ---
    def click_forgot_password(self):
        """Forgot password link par click karta hai."""
        self.driver.find_element(*self.FORGOT_PASSWORD_LINK).click()

    def login(self, username, password):
        """
        Master method jo poore login flow ko handle karta hai.
        Username, password enter karta hai, aur login button par click karta hai.
        """
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()
