import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Test_data import data2
import pytest
from webdriver_manager.firefox import GeckoDriverManager


class TestOrangeHRM:
    url = "https://opensource-demo.orangehrmlive.com"

    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        yield
        self.driver.close()

    # TC_Login_01
    def test_data_01(self, booting_function):
        self.driver.get(self.url)

        # Enter username
        username_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, data2.TestSelectors.input_box_username))
        )
        username_input.send_keys(data2.TestData.username)

        # CLICK ON FORGET PASSWORD:
        forget_password = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data2.TestSelectors.input_forget_password))
        )
        forget_password.click()

        # FILLING USERNAME AS DINESH:
        filling_username_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, data2.TestSelectors.input_box_username1))
        )
        filling_username_input.send_keys(data2.TestData.username_1)

        # CLICKING RESET PASSWORD BUTTON:
        reset_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data2.TestSelectors.input_reset_password))
        )
        text = reset_button.text
        print(text)
        reset_button.click()

        # TC_PIM_02:

    def test_data_02(self, booting_function):
        self.driver.get(self.url)

        # Enter username
        username_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, data2.TestSelectors.input_box_username))
        )
        username_input.send_keys(data2.TestData.username)

        # Enter password
        password_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, data2.TestSelectors.input_box_password))
        )
        password_input.send_keys(data2.TestData.password)

        # Clicking login button
        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data2.TestSelectors.login_xpath))
        )
        login_button.click()

        #  GO TO THE ADMIN PAGE:
        admin_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data2.TestSelectors.admin_xpath))
        )
        text1 = admin_button.text
        print(text1)
        admin_button.click()

        # VALIDATE THE 'TITLE' OF THE PAGE AS 'OrangeHRM'  :
        print('Title of the page:-', self.driver.title)

        # Validating options displaying on admin  page:
        # (A) VALIDATING USER MANAGEMENT:
        user_management = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data2.TestSelectors.user_management_xpath))
        )
        text1 = user_management.text
        print("Option (A):", text1)
        user_management.click()

        # (B) VALIDATING JOB:
        job = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data2.TestSelectors.job_xpath))
        )
        text1 = job.text
        print("Option (B):", text1)
        job.click()

        # (C) VALIDATING ORGANIZATION:
        organization = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data2.TestSelectors.organization_xpath))
        )
        text1 = organization.text
        print("Option (C):", text1)
        organization.click()

        # (D) VALIDATING QUALIFICATION:
        qualification = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data2.TestSelectors.qualification_xpath))
        )
        text1 = qualification.text
        print("Option (D):", text1)
        qualification.click()

        # (E) VALIDATING NATIONALITIES:
        nationalities = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data2.TestSelectors.nationalities_xpath))
        )
        text1 = nationalities.text
        print("Option (E):", text1)
        nationalities.click()

        # (F) VALIDATING CORPORATE BRANDING:
        corporate_branding = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data2.TestSelectors.corporate_branding_xpath))
        )
        text1 = corporate_branding.text
        print("Option (F):", text1)
        corporate_branding.click()

        # (G) VALIDATING  CONFIGURATION:
        configuration = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data2.TestSelectors.configuration_xpath))
        )
        text1 = configuration.text
        print("Option (G):", text1)
        configuration.click()

    # TC_PIM_03:
    def test_data_03(self, booting_function):
        self.driver.get(self.url)

        # Enter username
        username_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, data2.TestSelectors.input_box_username))
        )
        username_input.send_keys(data2.TestData.username)

        # Enter password
        password_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, data2.TestSelectors.input_box_password))
        )
        password_input.send_keys(data2.TestData.password)

        # Clicking login button
        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data2.TestSelectors.login_xpath))
        )
        login_button.click()

        #  GO TO THE ADMIN PAGE:
        admin_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data2.TestSelectors.admin_xpath))
        )
        text1 = admin_button.text
        print("Option (A):", text1)
        admin_button.click()

        # VALIDATING PIM:
        pim = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data2.TestSelectors.pim_xpath))
        )
        text1 = pim.text
        print("Option (B):", text1)
        pim.click()

        # VALIDATING LEAVE:
        leave = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data2.TestSelectors.leave_xpath))
        )
        text1 = leave.text
        print("Option (C):", text1)
        leave.click()

        # VALIDATING TIME:
        Time = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data2.TestSelectors.Time_xpath))
        )
        text1 = Time.text
        print("Option (D):", text1)
        Time.click()

        # VALIDATING RECRUITMENT:
        recruitment = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data2.TestSelectors.recruitment_xpath))
        )
        text1 = recruitment.text
        print("Option (E):", text1)
        recruitment.click()

        # VALIDATING MY INFO:
        my_info = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data2.TestSelectors.my_info_xpath))
        )
        text1 = my_info.text
        print("Option (F):", text1)
        my_info.click()

        # VALIDATING PERFORMANCE:
        performance = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data2.TestSelectors.performance_xpath))
        )
        text1 = performance.text
        print("Option (G):", text1)
        performance.click()

        # VALIDATING DASHBOARD:
        dashboard = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data2.TestSelectors.dashboard_xpath))
        )
        text1 = dashboard.text
        print("Option (H):", text1)
        dashboard.click()

        # VALIDATING DIRECTORY:
        directory = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data2.TestSelectors.directory_xpath))
        )
        text1 = directory.text
        print("Option (I):", text1)
        directory.click()

        # VALIDATING MAINTENANCE:
        maintenance = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data2.TestSelectors.maintenance_xpath))
        )
        text1 = maintenance.text
        print("Option (J):", text1)
        maintenance.click()

        # # VALIDATING CLAIM:  * Newly added *
        # claim = WebDriverWait(self.driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, data2.TestSelectors.claim_xpath))
        # )
        # text1 = claim.text
        # print("Option (K):", text1)
        # claim.click()

        # VALIDATING BUZZ:
        buzz = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, data2.TestSelectors.buzz_xpath))
        )
        text1 = buzz.text
        print("Option (K):", text1)
        buzz.click()












