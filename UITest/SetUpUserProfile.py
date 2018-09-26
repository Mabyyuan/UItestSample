from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
import ScreenShot
from time import sleep

def test_SetUpUserProfile(self):

    #Click Use Fitbit Profile
    UseFitbitProfile = 'new UiSelector().text("Use Fitbit Profile").className("android.widget.TextView")'
    self.driver.find_element_by_android_uiautomator(UseFitbitProfile).click()
    WebDriverWait(self.driver, 30).until(
        EC.invisibility_of_element_located(
            (By.ID, "com.thermos:id/progressBar2")
        )
    )


    #2017/05/04 Add Fitbit account login
    PW = "W1234567"
    Email = "wits.poseidon@gmail.com"
    FitbitEmail = 'new UiSelector().text("電子郵件").className("android.widget.EditText")'
    self.driver.find_element_by_android_uiautomator(FitbitEmail).click()
    self.driver.find_element_by_android_uiautomator(FitbitEmail).send_keys(Email)
    FitbitPasswd = 'new UiSelector().text("密碼").className("android.widget.EditText")'
    self.driver.find_element_by_android_uiautomator(FitbitPasswd).click()
    self.driver.find_element_by_android_uiautomator(FitbitPasswd).send_keys(PW)
    sleep(1)
    ScreenShot.AndroidScreenshot('007_FitbitLogIn')
    self.driver.find_element_by_class_name("android.widget.Button").click()

    try:
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(
                (By.ID, "com.thermos:id/next")
            )
        )
    except TimeoutException:
        ScreenShot.AndroidScreenshot('008_Fitbit_Login_Fail!')
        return True

    sleep(1)
    ScreenShot.AndroidScreenshot('008_Fitbit_Enable')
    self.driver.find_element_by_id("com.thermos:id/next").click()

    #2017/05/04 Remove click Create My Own Profile
    #UseFitbitProfile = 'new UiSelector().text("Create My Own Profile").className("android.widget.TextView")'
    #self.driver.find_element_by_android_uiautomator(UseFitbitProfile).click()

    #input user name
    username = "AppiumTest"
    InputField_Username = "com.thermos:id/edit_name"
    self.driver.find_element_by_id(InputField_Username).send_keys(username)
    sleep(1)
    ScreenShot.AndroidScreenshot('009_Profile_UserName')
    self.driver.find_element_by_id("com.thermos:id/next").click()
    sleep(1)
    ScreenShot.AndroidScreenshot('010_Profile_AddAPhoto')

    #add a photo
    AddAPhoto = "com.thermos:id/edit_photo"
    self.driver.find_element_by_id(AddAPhoto).click()
    sleep(1)
    ScreenShot.AndroidScreenshot('011_Photo_permission')
    permission_Photo = "com.android.packageinstaller:id/permission_allow_button"
    try:
        self.driver.find_element_by_id(permission_Photo).click()
    except NoSuchElementException:
        print("No permission_Photo pop up!")
    sleep(1)
    ScreenShot.AndroidScreenshot('012_Pictures_permission')
    Premission_Pictures = "com.android.packageinstaller:id/permission_allow_button"
    try:
        self.driver.find_element_by_id(Premission_Pictures).click()
    except NoSuchElementException:
        print("No permission_Picutres pop up!")
    sleep(1)
    ScreenShot.AndroidScreenshot('013_Photo_Selection')
    Selection = {
        'TakeAPhoto': 'new UiSelector().text("Take a photo").className("android.widget.TextView")',
        'ChooseFromLibrary': 'new UiSelector().text("Choose from library").className("android.widget.TextView")',
        'Cancel': 'new UiSelector().text("Cancel").className("android.widget.TextView")'
        }

    #Select Take a photo
    self.driver.find_element_by_android_uiautomator(Selection['TakeAPhoto']).click()
    sleep(1)
    ScreenShot.AndroidScreenshot('014_TakeAPhoto')
    self.driver.back()
    sleep(1)

    #Need to add a check point due to Camera app behavior might be different.
    try:
        self.driver.find_element_by_id(AddAPhoto)
    except NoSuchElementException:
        self.driver.back()

    self.driver.find_element_by_id(AddAPhoto).click()
    sleep(1)

    #Select Choose From Liberary
    self.driver.find_element_by_android_uiautomator(Selection['ChooseFromLibrary']).click()
    sleep(1)
    ScreenShot.AndroidScreenshot('015_ChooseFromLibrary')
    PicturesFolder = 'new UiSelector().text("Pictures").className("android.widget.TextView")'
    self.driver.find_element_by_android_uiautomator(PicturesFolder).click()
    sleep(1)
    ScreenShot.AndroidScreenshot('016_ChooseFromLibrary_PicturesFolder')
    pic1 = '//android.widget.GridView/android.widget.FrameLayout[@index="0"]'
    self.driver.find_element_by_xpath(pic1).click()
    sleep(1)
    ScreenShot.AndroidScreenshot('017_ChooseFromLibrary_PicturesFolder_Enable')
    self.driver.find_element_by_id('com.thermos:id/toolbar_next').click()
    sleep(1)
    ScreenShot.AndroidScreenshot('018_Profile_AddAPhoto_Success')

    #Go to E-mail Registration
    self.driver.find_element_by_id('com.thermos:id/next').click()
    sleep(1)
    ScreenShot.AndroidScreenshot('019_Profile_EnterEmail')

    #2017/05/04 add Privacy Policy and Contact Us


    #Input Mail Address
    MailAddress = "AppiumTest@test.com"
    InputField_Mail = "com.thermos:id/edit_email"
    self.driver.find_element_by_id(InputField_Mail).send_keys(MailAddress)
    sleep(1)
    ScreenShot.AndroidScreenshot('019_Profile_EnterEmailInputed')
    self.driver.find_element_by_id('com.thermos:id/next').click()

    #Initial Setup
    sleep(1)
    ScreenShot.AndroidScreenshot('020_InitialSetup_WakeUpSmartLid')

    self.driver.find_element_by_id('com.thermos:id/next').click()
    sleep(0.5)
    ScreenShot.AndroidScreenshot('021_InitialSetup_Searching')

    try:
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(
                (By.ID, "com.thermos:id/textView7")
            )
        )
    except TimeoutException:
        ScreenShot.AndroidScreenshot('022_InitialSetup_NotFound')
        return True
    sleep(1)
    ScreenShot.AndroidScreenshot('022_InitialSetup_PairingComplete')
    self.driver.find_element_by_id('com.thermos:id/next').click()


