from time import sleep
from pages.BasePage import Page
from selenium.webdriver.common.by import By

URL = "https://www.surveymonkey.com/"


class CreateSurvey(Page):

    # Login
    SIGN_IN_LINK = (By.XPATH, "//a[contains(@class, 'sign-in')]")
    SIGN_IN_BUTTON = (By.XPATH, "//button[contains(text(), 'SIGN IN')] ")
    USERNAME = (By.ID, "username")
    PASSWORD=(By.ID, "password")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "div.error-message")

    # Dashboard
    USER_ACCT_TAB_MAIN_MENU = (By.ID, "userAcctTab_MainMenu")
    SIGN_OUT = (By.LINK_TEXT, "Sign Out")
    CREATE_SURVEY_BUTTON = (By.XPATH, "//a[text() = 'CREATE SURVEY']")
    START_FROM_SCRATCH = (By.XPATH, "//button[@id='scratch']/span[text()='START FROM SCRATCH']")
    # Locator for survey monkey details popup
    CREATE_SURVEY = (By.XPATH, "//button[text()='CREATE SURVEY']")
    SURVEY_NAME = (By.ID, "surveyTitle")
    SURVEY_CATEGORY = (By.CLASS_NAME, "Select-placeholder")

    # Survey create page
    SURVEY_HEADER_TITLE = (By.XPATH, "//nav[@class = 'navigationTabs']//h2")
    NEW_QUESTION_BUTTON = (By.XPATH, "//a[contains(@class,'main-add-question-cta')]")
    ENTER_YOUR_QUESTION = (By.XPATH, "//div[@data-id='editQuestionContent']"
                                     "//td[contains(@class, 'questionText')]//div[@id='editTitle']")
    ENTER_FIRST_QUESTION = (By.XPATH, "//div[@data-id='editQuestionContent']//tbody[@data-field-type='answer']"
                                      "//tr[contains(concat(' ', normalize-space(@class), ' '), ' choice ') "
                                      "and not(contains(@class,'hide'))][1]//div[starts-with(@id,'newChoice')]"
                            )
    SAVE_SURVEY = (By.XPATH, "//div[@id='editQuestion']//section[contains(@class, 't1')]"
                             "//div[contains(@class, 'buttons')]/a[contains(@class,'save')]")
    DONE_BUTTON = (By.XPATH, "//div[contains(@class,'survey-submit-actions')]"
                             "//button[contains(@class,'done-button')]")
    SURVEY_TITLE = (By.XPATH, "//span[contains(@class , 'title-text')]")


    def open_page(self):
        self.open_web_page(URL)

    def click_on_sign_in(self):
        self.click(self.SIGN_IN_LINK)
        print "Clicked on sign in link"

    def click_on_sign_button(self):
        self.click(self.SIGN_IN_BUTTON)
        print "Clicked on sign in button"

    def fill_login_details(self, username=None, password=None):
        """

        :param username:
        :param password:
        :return:
        """
        if username:
            self.fill_text_box(self.USERNAME, username)
        if password:
            self.fill_text_box(self.PASSWORD, password)

    def get_error_message_text(self):
        error_text = None
        element = self.find_element(self.ERROR_MESSAGE)
        if element:
            error_text = element.text
        if error_text:
            return error_text
        else:
            return None

    def click_on_user_acct_tab_main_menu(self):
        self.driver.execute_script("window.scrollTo(0,0);")
        # pdb.set_trace()
        sleep(3)
        self.click(self.USER_ACCT_TAB_MAIN_MENU)

    def click_on_sign_out(self):
        self.click(self.SIGN_OUT)

    def click_on_create_survey(self):
        self.click(self.CREATE_SURVEY_BUTTON)

    def is_start_from_scratch_button_present(self):
        return self.is_element_present(self.START_FROM_SCRATCH)

    def click_on_start_from_scratch_button(self):
        self.click(self.START_FROM_SCRATCH)

    def is_create_survey_button_present_on_survey_details_pop_up(self):
        return self.is_element_present(self.CREATE_SURVEY)

    def fill_survey_name(self, survey_name):
        """

        :param survey_name:
        :return:
        """
        self.fill_text_box(self.SURVEY_NAME, survey_name)

    def select_survey_category(self, text):
        pass

    def click_on_survey_button(self):
        self.click(self.CREATE_SURVEY)

    def is_survey_title(self):
        pass

    def is_summery_page(self):
        pass

    def click_on_new_questions(self):
        self.click(self.NEW_QUESTION_BUTTON)
        print "Click on new question button"

    def enter_questions_answer(self, q_text):
        self.fill_text_box(self.ENTER_YOUR_QUESTION, q_text)
        print "Enter question text"
        self.fill_text_box(self.ENTER_FIRST_QUESTION, q_text)
        print "Enter answer choice"

    def click_on_save_button(self):
        self.click(self.SAVE_SURVEY)
        print "Click on save survey button"

    def is_survey_done_button(self):
        self.is_element_present(self.DONE_BUTTON)

    def get_survey_title_text(self):
        title_text = None
        element = self.find_element(self.SURVEY_TITLE)
        if element:
            title_text = element.text
        if title_text:
            return title_text
        else:
            print "Survey question page title is not found"



