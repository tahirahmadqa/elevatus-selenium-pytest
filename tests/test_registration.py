import pytest
import softest
from pages.navbar import Navbar
from pages.cookieDrawer import CookieDrawer
from pages.registrationPage import RegistrationPage
from pages.loginPage import LoginPage
from pages.jobListingPage import JobListingPage
from pages.jobDetailPage import JobDetailPage
from pages.submitYouCvPage import SubmitYourCvPage
from utilities.utils import Utils
from faker import Faker
import datetime
import random
import string
import imaplib
import email
import requests
from bs4 import BeautifulSoup

@pytest.mark.usefixtures("setup")
class TestLogin(softest.TestCase):
    log = Utils.custom_logger()
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.onNavbar = Navbar(self.driver)
        self.onCookieDrawer = CookieDrawer(self.driver)
        self.onRegistrationPage = RegistrationPage(self.driver)
        self.onLoginPage = LoginPage(self.driver)
        self.onJobListingPage = JobListingPage(self.driver)
        self.onJobDetailPage = JobDetailPage(self.driver)
        self.onSubmitYourCvPage = SubmitYourCvPage(self.driver)
        self.ut = Utils()
        self.fake = Faker()
        self.first_name = self.fake.first_name()
        self.last_name = self.fake.last_name()
        self.response = requests.post('https://www.mailinator.com/api/v2/domains/mailinator.com/inboxes', json={})
        self.inbox = self.response.json()['inbox']
        self.email_address = f"{self.inbox}@mailinator.com"
        print(f"Random email address: {self.email_address}")
        password_characters = string.ascii_letters + string.digits + "!@#$%^&*()"
        self.password = ''.join(random.choice(password_characters) for i in range(10))
        while not (any(c.islower() for c in self.password) and
                any(c.isupper() for c in self.password) and
                any(c.isdigit() for c in self.password) and
                any(c in string.punctuation for c in self.password)):
            self.password = ''.join(random.choice(password_characters) for i in range(10))
        # starting phone number from 3 as I've set up to work with Pakistani number
        self.phone_number = "322" + self.fake.phone_number()[3:]
        start_date = datetime.date.today() - datetime.timedelta(days=365*80)
        end_date = datetime.date.today() - datetime.timedelta(days=365*18)
        random_date = self.fake.date_between(start_date=start_date, end_date=end_date)
        self.dateOfBirth = random_date.strftime('%Y-%m-%d')
    
    def test_user_registers_and_then_applies_for_job(self):
        #handle cookie drawer
        if self.onCookieDrawer.accept_cookies_btn_is_displayed:
            self.onCookieDrawer.click_accept_cookies_button()
        #register
        self.onNavbar.click_register_button()
        self.onRegistrationPage.verify_signup_button_is_disabled()
        self.onRegistrationPage.enter_in_firstname_field(self.first_name)
        self.onRegistrationPage.enter_in_lastname_field(self.last_name)
        self.onRegistrationPage.enter_in_email_field(self.email_address)
        self.onRegistrationPage.enter_in_password_field(self.password)
        self.onRegistrationPage.enter_in_confirm_password_field(self.password)
        self.onRegistrationPage.enter_in_phone_number_field(self.phone_number)
        self.onRegistrationPage.check_privacy_policy_checkbox()
        self.onRegistrationPage.verify_signup_button_is_enabled()
        self.onRegistrationPage.click_signup_button()
        self.onRegistrationPage.verify_registration_is_successful()
        #email account connect connect
        # Connect to your Gmail account
        imap_host = 'imap.mailinator.com'
        imap_user = self.email_address
        imap_pass = ''
        imap = imaplib.IMAP4_SSL(imap_host)
        imap.login(imap_user, imap_pass)
        imap.select('INBOX')
        # Search for the verification email by subject
        result, data = imap.search(None, 'SUBJECT "Elevatus - Registration Successful"')
        # Get the latest email from the search results
        latest_email_id = data[0].split()[-1]
        result, data = imap.fetch(latest_email_id, '(RFC822)')
        raw_email = data[0][1]
        # Parse the raw email using the email library
        email_message = email.message_from_bytes(raw_email)
        email_subject = email_message['Subject']
        email_from = email_message['From']
        email_body = ''
        # Get the email body as HTML
        if email_message.is_multipart():
            for part in email_message.get_payload():
                if part.get_content_type() == 'text/html':
                    email_body += part.get_payload()
        else:
            email_body = email_message.get_payload()
        # Parse the HTML of the email using BeautifulSoup
        soup = BeautifulSoup(email_body, 'html.parser')
        verification_link = soup.find_all('a')[0].get('href')
        # Print the verification link
        print(verification_link)
        # use the verification link above to verify registration
        # Logout of the Gmail account
        imap.close()
        imap.logout()
        #apply job
        self.onLoginPage.click_fill_manually_button()
        self.onSubmitYourCvPage.enter_in_date_of_birth_field(self.dateOfBirth)
        self.onSubmitYourCvPage.select_first_gender()
        self.onSubmitYourCvPage.select_first_nationality()
        self.onSubmitYourCvPage.upload_cv()
        self.onSubmitYourCvPage.click_submit_button()

    def test_user_registers_and_then_applies_for_job(self):
        #handle cookie drawer
        if self.onCookieDrawer.accept_cookies_btn_is_displayed:
            self.onCookieDrawer.click_accept_cookies_button()
        #login
        self.driver.get("https://automations.elevatus.io/login")
        self.onLoginPage.enter_in_email_field("email.tahirahmad2+sb1@gmail.com")
        self.onLoginPage.enter_in_password_field("Doitnow911@")
        self.onLoginPage.click_signin_button()
        #apply job
        self.onLoginPage.click_fill_manually_button()
        self.onSubmitYourCvPage.enter_in_date_of_birth_field(self.dateOfBirth)
        self.onSubmitYourCvPage.select_first_gender()
        self.onSubmitYourCvPage.select_first_nationality()
        self.onSubmitYourCvPage.upload_cv()
        self.onSubmitYourCvPage.click_submit_button() 