from selenium.webdriver.common.by import By

class DashboardPage:
    # --- Locators ---
    # Dashboard side menu par search input
    SEARCH_INPUT = (By.XPATH, "//input[@placeholder='Search']")
    
    # Admin Menu Link
    ADMIN_MENU = (By.XPATH, "//span[text()='Admin']")

    # System Users Page Locators
    SYSTEM_USER_USERNAME_INPUT = (By.XPATH, "(//input[contains(@class, 'oxd-input')])[2]")
    USER_ROLE_DROPDOWN = (By.XPATH, "(//div[contains(@class, 'oxd-select-text')])[1]")
    EMPLOYEE_NAME_INPUT = (By.XPATH, "//input[@placeholder='Type for hints...']")
    STATUS_DROPDOWN = (By.XPATH, "(//div[contains(@class, 'oxd-select-text')])[2]")
    # For options (User Role, Status, Employee Name), we will use dynamic xpath in action methods:
    # "//div[@role='listbox']//span[contains(text(), '{}')]"
    
    SEARCH_BUTTON = (By.XPATH, "//button[@type='submit' and normalize-space()='Search']")
    ADD_USER_BUTTON = (By.XPATH, "//button[@type='button' and normalize-space(.)='Add']")
    
    # Job Menu Locators
    JOB_TAB = (By.XPATH, "//span[normalize-space()='Job']")
    JOB_TITLES_OPTION = (By.XPATH, "//a[normalize-space()='Job Titles']")
    PAY_GRADES_OPTION = (By.XPATH, "//a[normalize-space()='Pay Grades']")
    EMPLOYMENT_STATUS_OPTION = (By.XPATH, "//a[normalize-space()='Employment Status']")
    JOB_CATEGORIES_OPTION = (By.XPATH, "//a[normalize-space()='Job Categories']")
    WORK_SHIFTS_OPTION = (By.XPATH, "//a[normalize-space()='Work Shifts']")

    # Organization Menu Locators
    ORGANIZATION_TAB = (By.XPATH, "//span[normalize-space()='Organization']")
    ORG_GENERAL_INFORMATION_OPTION = (By.XPATH, "//a[normalize-space()='General Information']")
    ORG_LOCATIONS_OPTION = (By.XPATH, "//a[normalize-space()='Locations']")
    ORG_STRUCTURE_OPTION = (By.XPATH, "//a[normalize-space()='Structure']")

    # Qualifications Menu Locators
    QUALIFICATIONS_TAB = (By.XPATH, "//span[normalize-space()='Qualifications']")
    QUAL_SKILLS_OPTION = (By.XPATH, "//a[normalize-space()='Skills']")
    QUAL_EDUCATION_OPTION = (By.XPATH, "//a[normalize-space()='Education']")
    QUAL_LICENSES_OPTION = (By.XPATH, "//a[normalize-space()='Licenses']")
    QUAL_LANGUAGES_OPTION = (By.XPATH, "//a[normalize-space()='Languages']")
    QUAL_MEMBERSHIPS_OPTION = (By.XPATH, "//a[normalize-space()='Memberships']")

    # Nationalities Menu Locator
    NATIONALITIES_TAB = (By.XPATH, "//a[normalize-space()='Nationalities']")

    def __init__(self, driver):
        self.driver = driver

    # --- Generic Verification Methods ---
    def is_visible(self, locator):
        """Generic method check karne ke liye ki koi element uske locator ke hisaab se visible hai ya nahi."""
        return self.driver.find_element(*locator).is_displayed()

    def is_enabled(self, locator):
        """Generic method check karne ke liye ki koi element uske locator ke hisaab se enabled hai ya nahi."""
        return self.driver.find_element(*locator).is_enabled()

    # --- Action Methods ---
    def enter_search_text(self, text):
        """Search input me text daalta hai."""
        self.driver.find_element(*self.SEARCH_INPUT).send_keys(text)

    def clear_search_input(self):
        """Search input ko clear karta hai."""
        self.driver.find_element(*self.SEARCH_INPUT).clear()

    def click_element(self, locator):
        """Generic click method"""
        self.driver.find_element(*locator).click()
        
    def enter_text(self, locator, text):
        """Generic send_keys method"""
        self.driver.find_element(*locator).send_keys(text)

    def select_dropdown_option(self, option_text):
        """
        Generic method to select an option from any open listbox dropdown.
        It uses dynamic xpath to find the option with the matching text.
        """
        import time
        time.sleep(1) # Wait for listbox to render
        dynamic_locator = (By.XPATH, f"//div[@role='listbox']//span[contains(text(), '{option_text}')]")
        self.driver.find_element(*dynamic_locator).click()
