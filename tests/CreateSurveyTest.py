import requests,json
import os

from pages.CreateSurveyPage import CreateSurvey
from time import sleep
from uuid import uuid4


##
## 1) Generate python stub source code:
##    java -jar graphwalker-3.4.0-SNAPSHOT.jar source -i model.graphml python.template > model.py
##
## 2) Start graphwalker:
##    java -jar graphwalker-3.4.0-SNAPSHOT.jar online --service RESTFUL -m model.graphml "random(edge_coverage(100))"
##
## 3) Run the per program:
##    python model.py
##

CREATE_SURVEY_OBJ = None
DEMO_TITLE = "TestSurvey_" + str(uuid4())[:6]
RESULT_DUMP = False
USERNAME = ""
PASS = ""


class CreateSurveyTest(CreateSurvey):

    def __init__(self):
        super(CreateSurveyTest, self).__init__()


def setup():
    """

    :return:
    """
    global CREATE_SURVEY_OBJ
    CREATE_SURVEY_OBJ = CreateSurveyTest()
    print "Object created", CREATE_SURVEY_OBJ
    return


def teardown():
    """
    :return:
    """
    CREATE_SURVEY_OBJ.quit()

def e_ClickNewQuestion() :
    CREATE_SURVEY_OBJ.click_on_new_questions()
    sleep(3)
    print( "e_ClickNewQuestion" )
    return


def e_EnteringQueAndAns() :
    question_text = "Test"
    CREATE_SURVEY_OBJ.enter_questions_answer(q_text = question_text)
    CREATE_SURVEY_OBJ.click_on_save_button()
    print( "e_EnteringQueAndAns" )
    return


def e_LoginFailed() :
    fake_data = "test"
    CREATE_SURVEY_OBJ.click_on_sign_in()
    CREATE_SURVEY_OBJ.fill_login_details(username=fake_data, password=fake_data)
    CREATE_SURVEY_OBJ.click_on_sign_button()
    print( "e_LoginFailed" )
    return


def e_LoginSuccedAfterFailure() :
    # CREATE_SURVEY_OBJ.page_reload()
    CREATE_SURVEY_OBJ.fill_login_details(username=USERNAME,password=PASS)
    CREATE_SURVEY_OBJ.click_on_sign_button()
    print( "e_LoginSuccedAfterFailure" )
    return


def e_Logout() :
    CREATE_SURVEY_OBJ.click_on_user_acct_tab_main_menu()
    CREATE_SURVEY_OBJ.click_on_sign_out()
    print( "e_Logout" )
    return


def e_StartBrowser() :
    global CREATE_SURVEY_OBJ
    CREATE_SURVEY_OBJ = CreateSurveyTest()
    print "Object created", CREATE_SURVEY_OBJ
    print( "e_StartBrowser" )
    return


def e_SurveyDetails() :
    survey_name = DEMO_TITLE
    CREATE_SURVEY_OBJ.fill_survey_name(survey_name=survey_name)
    CREATE_SURVEY_OBJ.click_on_survey_button()
    print( "e_SurveyDetails" )
    return survey_name

def e_createSurvey() :
    CREATE_SURVEY_OBJ.click_on_create_survey()
    print( "e_createSurvey" )
    return


def e_createSurveyFromScratch() :
    CREATE_SURVEY_OBJ.click_on_start_from_scratch_button()
    print( "e_createSurveyFromScratch" )
    return


def v_AccountOverviewPage() :
    print( "v_AccountOverviewPage" )
    return


def v_CreateSurvey() :
    result = CREATE_SURVEY_OBJ.is_create_survey_button_present_on_survey_details_pop_up()
    if result:
        assert result
    else:
        print "Create survey button is not present on survey details pop up"
    print( "v_CreateSurvey" )
    return


def v_DoneButton() :
    CREATE_SURVEY_OBJ.is_survey_done_button()
    print( "v_DoneButton" )
    return


def v_ErrorPage() :
    error_message = "The username or password you entered is incorrect. " \
                    "Please try again--and remember that passwords are case sensitive."
    actual_error_text = CREATE_SURVEY_OBJ.get_error_message_text()
    if actual_error_text:
        result = error_message == actual_error_text
        if result:
            print "Passed"
            assert result
    else:
        print "No Error text found"
    print( "v_ErrorPage" )
    return


def v_HomePage() :
    CREATE_SURVEY_OBJ.open_page()
    actual_title = CREATE_SURVEY_OBJ.get_page_title()
    expected_title = "SurveyMonkey: Free online survey software & questionnaire tool"
    result = expected_title == actual_title
    if result:
        assert result
    else:
        print "Home page is not open"
    # print( "v_HomePage" )
    return


def v_StartFromScratch() :
    result = CREATE_SURVEY_OBJ.is_start_from_scratch_button_present()
    if result:
        assert result
    else:
        print "Start from scratch button is not present"
    print( "v_StartFromScratch" )
    return


def v_SummaryPage() :
    sleep(5)
    print( "v_SummaryPage" )
    return


def v_TitleVerification() :
    expected_title = DEMO_TITLE
    actual_title_text = CREATE_SURVEY_OBJ.get_survey_title_text()
    if actual_title_text:
        result = expected_title == actual_title_text
        if result:
            assert result
        else:
            print "Failed"
    print( "v_TitleVerification" )
    return


gw_url = 'http://localhost:8887/graphwalker'

try:
    while requests.get(gw_url+'/hasNext').json()['hasNext'] == 'true' :
        RESULT_DUMP = True
        # Get next step from GraphWalker
        step = requests.get(gw_url+'/getNext').json()['currentElementName']
        if step != '' :
            eval( step + "()" )
finally:
    result = requests.get(gw_url+'/getStatistics').json()
    file_path = os.path.join(os.getcwd(), "result") + "/result.json"
    with open(file_path, 'w') as obj:
        json.dump(result, obj)
    if RESULT_DUMP:
        print result
    del CREATE_SURVEY_OBJ
    # if hasattr(CREATE_SURVEY_OBJ,"teardown"):
    #     CREATE_SURVEY_OBJ.teardown()

