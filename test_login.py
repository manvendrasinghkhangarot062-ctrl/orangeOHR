import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from login_page import LoginPage

class TestLogin:
    
    def setup_method(self, method):
        # Edge driver ko initialize karein
        self.driver = webdriver.Edge()
        self.driver.maximize_window()
        # OrangeHRM login page par jayein
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        # Elements load hone tak implicitly wait karein
        self.driver.implicitly_wait(10)

    def teardown_method(self, method):
        # Har test ke baad driver ko band karein
        self.driver.quit()

    def test_tc01_all_elements_visibility(self):
        login_page = LoginPage(self.driver)
        
        # Combined method ka use karke check karein ki sabhi main login elements visible hain ya nahi
        assert login_page.are_all_elements_visible(), "One or more login elements (username, password, submit button) are not visible"

    def test_tc02_all_elements_enabled(self):
        login_page = LoginPage(self.driver)
        
        # Combined method ka use karke check karein ki sabhi main login elements enabled aur clickable hain ya nahi
        assert login_page.are_all_elements_enabled(), "One or more login elements (username, password, submit button) are not enabled/clickable"

    def test_tc03_valid_login(self):
        login_page = LoginPage(self.driver)
        
        # LoginPage class se master method ka use karke
        # OrangeHRM demo ke liye Admin / admin123 default credentials hain
        login_page.login("Admin", "admin123")
        
        # URL ya Dashboard element ko check karke successful login verify karein
        WebDriverWait(self.driver, 10).until(EC.url_contains("dashboard"))
        assert "dashboard" in self.driver.current_url

    def test_tc04_branding_visibility(self):
        login_page = LoginPage(self.driver)
        
        # Image render hone me time lag sakta hai, isliye explicit wait ka use karenge
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LoginPage.BRANDING_IMAGE))
        
        # Generic method ka use karke verify karein ki login page par company branding (heading) visible hai ya nahi
        assert login_page.is_visible(LoginPage.BRANDING_IMAGE), "Company branding (heading) is not visible on the login page"

    def test_tc05_forgot_password(self):
        login_page = LoginPage(self.driver)
        
        # Generic methods ka use karke enabled aur visibility dono verify karein
        assert login_page.is_visible(LoginPage.FORGOT_PASSWORD_LINK), "Forgot password link is not visible"
        assert login_page.is_enabled(LoginPage.FORGOT_PASSWORD_LINK), "Forgot password link is not enabled"
        
        # Link par click karein
        login_page.click_forgot_password()

    def test_tc06_reset_password_button(self):
        login_page = LoginPage(self.driver)
        
        # Pehle forgot password page par jayein
        login_page.click_forgot_password()
        
        # Reset Password button load hone ke liye explicitly wait karein kyunki humne naye view par navigate kiya hai
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LoginPage.RESET_PASSWORD_BUTTON))
        
        # Generic methods ka use karke visibility aur clickability/enabled state dono verify karein
        assert login_page.is_visible(LoginPage.RESET_PASSWORD_BUTTON), "Reset password button is not visible"
        assert login_page.is_enabled(LoginPage.RESET_PASSWORD_BUTTON), "Reset password button is not enabled/clickable"

    def test_tc07_cancel_password_button(self):
        login_page = LoginPage(self.driver)
        
        # Pehle forgot password page par jayein
        login_page.click_forgot_password()
        
        # Cancel button load hone ke liye explicitly wait karein
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LoginPage.CANCEL_PASSWORD_BUTTON))
        
        # Generic methods ka use karke visibility aur clickability/enabled state dono verify karein
        assert login_page.is_visible(LoginPage.CANCEL_PASSWORD_BUTTON), "Cancel password button is not visible"
        assert login_page.is_enabled(LoginPage.CANCEL_PASSWORD_BUTTON), "Cancel password button is not enabled/clickable"

    def test_tc08_reset_password_username_input(self):
        login_page = LoginPage(self.driver)
        
        # Pehle forgot password page par jayein
        login_page.click_forgot_password()
        
        # Reset page par Username input load hone ke liye explicitly wait karein
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LoginPage.RESET_PASSWORD_USERNAME_INPUT))
        
        # Generic methods ka use karke visibility aur clickability/enabled state dono verify karein
        assert login_page.is_visible(LoginPage.RESET_PASSWORD_USERNAME_INPUT), "Username input on reset page is not visible"
        assert login_page.is_enabled(LoginPage.RESET_PASSWORD_USERNAME_INPUT), "Username input on reset page is not enabled/clickable"

    def test_tc09_reset_password_title(self):
        login_page = LoginPage(self.driver)
        
        # Pehle forgot password page par jayein
        login_page.click_forgot_password()
        
        # Reset Password title heading load hone ke liye explicitly wait karein
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LoginPage.RESET_PASSWORD_TITLE))
        
        # Generic methods ka use karke visibility aur clickability/enabled state dono verify karein
        assert login_page.is_visible(LoginPage.RESET_PASSWORD_TITLE), "Reset password title heading is not visible"
        assert login_page.is_enabled(LoginPage.RESET_PASSWORD_TITLE), "Reset password title heading is not enabled"
