from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from login_page import LoginPage
from dashboard_page import DashboardPage

class TestDashboard:
    
    def setup_method(self, method):
        # Edge driver ko initialize karein
        self.driver = webdriver.Edge()
        self.driver.maximize_window()
        # OrangeHRM login page par jayein
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        # Elements load hone tak implicitly wait karein
        self.driver.implicitly_wait(10)
        
        # Pre-condition: Dashboard access karne ke liye login karein
        login_page = LoginPage(self.driver)
        login_page.login("Admin", "admin123")
        
        # Test run karne se pehle dashboard poori tarah load hone ka wait karein
        WebDriverWait(self.driver, 10).until(EC.url_contains("dashboard"))

    def teardown_method(self, method):
        # Har test ke baad driver ko band karein
        self.driver.quit()

    def test_tc10_search_input(self):
        dashboard_page = DashboardPage(self.driver)
        
        # Search input ki visibility aur clickability/enabled state dono verify karein
        assert dashboard_page.is_visible(DashboardPage.SEARCH_INPUT), "Dashboard Search input is not visible"
        assert dashboard_page.is_enabled(DashboardPage.SEARCH_INPUT), "Dashboard Search input is not enabled/clickable"

    def test_tc11_search_action(self):
        dashboard_page = DashboardPage(self.driver)
        
        # Search input me 'admin' enter karein
        dashboard_page.enter_search_text("admin")
        
        import time
        time.sleep(2) # Thodi der wait karte hain taaki UI changes dekh sakein (optional)
        
        # Fir search input ko clear karein
        dashboard_page.clear_search_input()
        time.sleep(2) # Clear hone ke baad wait (optional)

    def test_tc12_admin_search_flow(self):
        dashboard_page = DashboardPage(self.driver)
        import time
        
        # Step 0: Click on Admin Menu to navigate to System Users page
        assert dashboard_page.is_visible(DashboardPage.ADMIN_MENU), "Admin Menu is not visible"
        assert dashboard_page.is_enabled(DashboardPage.ADMIN_MENU), "Admin Menu is not enabled"
        dashboard_page.click_element(DashboardPage.ADMIN_MENU)
        
        # Elements load hone ke liye thoda wait (Ideally WebDriverWait use karna better hai, par time.sleep(2) works for demo)
        time.sleep(2)
        
        # Step 1: Verify and interact with Username input
        assert dashboard_page.is_visible(DashboardPage.SYSTEM_USER_USERNAME_INPUT), "Username input not visible"
        assert dashboard_page.is_enabled(DashboardPage.SYSTEM_USER_USERNAME_INPUT), "Username input not enabled"
        dashboard_page.click_element(DashboardPage.SYSTEM_USER_USERNAME_INPUT)
        dashboard_page.enter_text(DashboardPage.SYSTEM_USER_USERNAME_INPUT, "Admin")
        
        # Step 2: Verify and click User Role dropdown
        assert dashboard_page.is_visible(DashboardPage.USER_ROLE_DROPDOWN), "User Role dropdown not visible"
        assert dashboard_page.is_enabled(DashboardPage.USER_ROLE_DROPDOWN), "User Role dropdown not enabled"
        dashboard_page.click_element(DashboardPage.USER_ROLE_DROPDOWN)
        time.sleep(1) # Dropdown options khulne ka wait
        
        # Step 3: Verify and select 'Admin' from dropdown
        assert dashboard_page.is_visible(DashboardPage.USER_ROLE_OPTION_ADMIN), "Admin option in User Role not visible"
        assert dashboard_page.is_enabled(DashboardPage.USER_ROLE_OPTION_ADMIN), "Admin option in User Role not enabled"
        dashboard_page.click_element(DashboardPage.USER_ROLE_OPTION_ADMIN)
        
        # Step 4: Verify and interact with Employee Name input
        assert dashboard_page.is_visible(DashboardPage.EMPLOYEE_NAME_INPUT), "Employee Name input not visible"
        assert dashboard_page.is_enabled(DashboardPage.EMPLOYEE_NAME_INPUT), "Employee Name input not enabled"
        dashboard_page.click_element(DashboardPage.EMPLOYEE_NAME_INPUT)
        dashboard_page.enter_text(DashboardPage.EMPLOYEE_NAME_INPUT, "Demo Open Source")
        time.sleep(2) # Autocomplete options aane ka wait
        
        # Verify and select the autocomplete option
        assert dashboard_page.is_visible(DashboardPage.EMPLOYEE_NAME_OPTION), "Employee Name autocomplete option not visible"
        assert dashboard_page.is_enabled(DashboardPage.EMPLOYEE_NAME_OPTION), "Employee Name autocomplete option not enabled"
        dashboard_page.click_element(DashboardPage.EMPLOYEE_NAME_OPTION)
        time.sleep(1)
        
        # Step 5: Verify and click Status dropdown
        assert dashboard_page.is_visible(DashboardPage.STATUS_DROPDOWN), "Status dropdown not visible"
        assert dashboard_page.is_enabled(DashboardPage.STATUS_DROPDOWN), "Status dropdown not enabled"
        dashboard_page.click_element(DashboardPage.STATUS_DROPDOWN)
        time.sleep(1) # Dropdown options khulne ka wait
        
        # Step 6: Verify and select 'Enabled' from dropdown
        assert dashboard_page.is_visible(DashboardPage.STATUS_OPTION_ENABLED), "Enabled option in Status not visible"
        assert dashboard_page.is_enabled(DashboardPage.STATUS_OPTION_ENABLED), "Enabled option in Status not enabled"
        dashboard_page.click_element(DashboardPage.STATUS_OPTION_ENABLED)
        
        # Step 7: Verify and click Search button
        assert dashboard_page.is_visible(DashboardPage.SEARCH_BUTTON), "Search button not visible"
        assert dashboard_page.is_enabled(DashboardPage.SEARCH_BUTTON), "Search button not enabled"
        dashboard_page.click_element(DashboardPage.SEARCH_BUTTON)
        time.sleep(3) # Search results dekhne ke liye wait
        
        # Step 8: Verify and click Add button
        assert dashboard_page.is_visible(DashboardPage.ADD_USER_BUTTON), "Add button not visible"
        assert dashboard_page.is_enabled(DashboardPage.ADD_USER_BUTTON), "Add button not enabled"
        dashboard_page.click_element(DashboardPage.ADD_USER_BUTTON)
        time.sleep(2) # Add user page load hone ka wait

    def test_tc13_job_menu_options(self):
        dashboard_page = DashboardPage(self.driver)
        import time
        
        # Pehle Admin menu par click karna zaroori hai taaki 'Job' tab dikhayi de
        assert dashboard_page.is_visible(DashboardPage.ADMIN_MENU), "Admin Menu is not visible"
        assert dashboard_page.is_enabled(DashboardPage.ADMIN_MENU), "Admin Menu is not enabled"
        dashboard_page.click_element(DashboardPage.ADMIN_MENU)
        time.sleep(2) # Admin page load hone ka wait
        
        job_options = [
            ("Job Titles", DashboardPage.JOB_TITLES_OPTION),
            ("Pay Grades", DashboardPage.PAY_GRADES_OPTION),
            ("Employment Status", DashboardPage.EMPLOYMENT_STATUS_OPTION),
            ("Job Categories", DashboardPage.JOB_CATEGORIES_OPTION),
            ("Work Shifts", DashboardPage.WORK_SHIFTS_OPTION)
        ]
        
        for option_name, option_locator in job_options:
            # Har option select karne se pehle 'Job' tab par click karna padega kyunki page refresh ho jata hai
            assert dashboard_page.is_visible(DashboardPage.JOB_TAB), "Job tab is not visible"
            assert dashboard_page.is_enabled(DashboardPage.JOB_TAB), "Job tab is not enabled"
            dashboard_page.click_element(DashboardPage.JOB_TAB)
            time.sleep(1) # Dropdown open hone ka wait
            
            # Ab specific option ki visibility aur enabled state verify karke click karein
            assert dashboard_page.is_visible(option_locator), f"{option_name} option is not visible"
            assert dashboard_page.is_enabled(option_locator), f"{option_name} option is not enabled"
            dashboard_page.click_element(option_locator)
            
            # Naya page load hone ke liye thoda wait (Demonstration ke liye)
            time.sleep(2)

    def test_tc14_organization_menu_options(self):
        dashboard_page = DashboardPage(self.driver)
        import time
        
        # Admin menu par click karna zaroori hai
        assert dashboard_page.is_visible(DashboardPage.ADMIN_MENU), "Admin Menu is not visible"
        assert dashboard_page.is_enabled(DashboardPage.ADMIN_MENU), "Admin Menu is not enabled"
        dashboard_page.click_element(DashboardPage.ADMIN_MENU)
        time.sleep(2) # Admin page load hone ka wait

        # Organization Options
        org_options = [
            ("General Information", DashboardPage.ORG_GENERAL_INFORMATION_OPTION),
            ("Locations", DashboardPage.ORG_LOCATIONS_OPTION),
            ("Structure", DashboardPage.ORG_STRUCTURE_OPTION)
        ]
        for option_name, option_locator in org_options:
            assert dashboard_page.is_visible(DashboardPage.ORGANIZATION_TAB), "Organization tab is not visible"
            assert dashboard_page.is_enabled(DashboardPage.ORGANIZATION_TAB), "Organization tab is not enabled"
            dashboard_page.click_element(DashboardPage.ORGANIZATION_TAB)
            time.sleep(1)
            
            assert dashboard_page.is_visible(option_locator), f"{option_name} option is not visible"
            assert dashboard_page.is_enabled(option_locator), f"{option_name} option is not enabled"
            dashboard_page.click_element(option_locator)
            time.sleep(2)

    def test_tc15_qualifications_menu_options(self):
        dashboard_page = DashboardPage(self.driver)
        import time
        
        # Admin menu par click karna zaroori hai
        assert dashboard_page.is_visible(DashboardPage.ADMIN_MENU), "Admin Menu is not visible"
        assert dashboard_page.is_enabled(DashboardPage.ADMIN_MENU), "Admin Menu is not enabled"
        dashboard_page.click_element(DashboardPage.ADMIN_MENU)
        time.sleep(2) # Admin page load hone ka wait

        # Qualifications Options
        qual_options = [
            ("Skills", DashboardPage.QUAL_SKILLS_OPTION),
            ("Education", DashboardPage.QUAL_EDUCATION_OPTION),
            ("Licenses", DashboardPage.QUAL_LICENSES_OPTION),
            ("Languages", DashboardPage.QUAL_LANGUAGES_OPTION),
            ("Memberships", DashboardPage.QUAL_MEMBERSHIPS_OPTION)
        ]
        for option_name, option_locator in qual_options:
            assert dashboard_page.is_visible(DashboardPage.QUALIFICATIONS_TAB), "Qualifications tab is not visible"
            assert dashboard_page.is_enabled(DashboardPage.QUALIFICATIONS_TAB), "Qualifications tab is not enabled"
            dashboard_page.click_element(DashboardPage.QUALIFICATIONS_TAB)
            time.sleep(1)
            
            assert dashboard_page.is_visible(option_locator), f"{option_name} option is not visible"
            assert dashboard_page.is_enabled(option_locator), f"{option_name} option is not enabled"
            dashboard_page.click_element(option_locator)
            time.sleep(2)

    def test_tc16_nationalities_menu(self):
        dashboard_page = DashboardPage(self.driver)
        import time
        
        # Admin menu par click karna zaroori hai
        assert dashboard_page.is_visible(DashboardPage.ADMIN_MENU), "Admin Menu is not visible"
        assert dashboard_page.is_enabled(DashboardPage.ADMIN_MENU), "Admin Menu is not enabled"
        dashboard_page.click_element(DashboardPage.ADMIN_MENU)
        time.sleep(2) # Admin page load hone ka wait

        # Nationalities
        assert dashboard_page.is_visible(DashboardPage.NATIONALITIES_TAB), "Nationalities tab is not visible"
        assert dashboard_page.is_enabled(DashboardPage.NATIONALITIES_TAB), "Nationalities tab is not enabled"
        dashboard_page.click_element(DashboardPage.NATIONALITIES_TAB)
        time.sleep(2)
