from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
import ScreenShot
import Gesture
from time import sleep

#Please Make Sure it is in the Hydration Page
def test_GeneralBaselineGoalSetup(self):
    # Hydration Page
    sleep(1)
    ScreenShot.AndroidScreenshot('028_Hydration_HydrationGoal')

    #2017/05/04 add continue with general baseline goal
    BaselineGoal = 'new UiSelector().text("Continue With General Baseline Goal").className("android.widget.TextView")'
    self.driver.find_element_by_android_uiautomator(BaselineGoal).click()
    sleep(1)
    ScreenShot.AndroidScreenshot('029_BaselineGoalSet')
    self.driver.back()

    #Hydration - Setup My Suggested Goal
    SetupMySuggestedGoal = 'new UiSelector().text("Setup My Suggested Goal").className("android.widget.TextView")'
    ##ContinueWithGeneralBaselineGoal = 'new UiSelector().text("Continue With General Baseline Goal").className("android.widget.TextView")'

    self.driver.find_element_by_android_uiautomator(SetupMySuggestedGoal).click()
    sleep(1)
    ScreenShot.AndroidScreenshot('029_Hydration_Disclaimer')
    AcceptTermsAndConditions = 'new UiSelector().text("Accept Terms And Conditions").className("android.widget.TextView")'
    self.driver.find_element_by_android_uiautomator(AcceptTermsAndConditions).click()
    sleep(1)
    ScreenShot.AndroidScreenshot('030_SetAge.png')
    self.driver.find_element_by_id('com.thermos:id/next').click()
    sleep(1)
    ScreenShot.AndroidScreenshot('031_SetSex.png')
    self.driver.find_element_by_id('com.thermos:id/next').click()
    sleep(1)
    ScreenShot.AndroidScreenshot('032_SetWeight.png')
    Gesture.SetGaolWHswipeLeft(self, 12, 1000)
    sleep(1)
    ScreenShot.AndroidScreenshot('032_SetWeightMax.png')
    Gesture.SetGaolWHswipeRight(self, 24, 1000)
    sleep(1)
    ScreenShot.AndroidScreenshot('032_SetWeightMin.png')
    self.driver.find_element_by_id('com.thermos:id/next').click()
    sleep(1)
    ScreenShot.AndroidScreenshot('033_SetHeight.png')
    Gesture.SetGaolWHswipeLeft(self, 5, 1000)
    sleep(1)
    ScreenShot.AndroidScreenshot('032_SetHightMax.png')
    Gesture.SetGaolWHswipeRight(self, 5, 1000)
    sleep(1)
    ScreenShot.AndroidScreenshot('032_SetHightMin.png')
    self.driver.find_element_by_id('com.thermos:id/next').click()
    sleep(1)
    ScreenShot.AndroidScreenshot('034_SetActivity.png')
    self.driver.find_element_by_id('com.thermos:id/next').click()
    sleep(1)
    ScreenShot.AndroidScreenshot('035_SetIntensity.png')
    self.driver.find_element_by_id('com.thermos:id/next').click()
    sleep(1)
    ScreenShot.AndroidScreenshot('036_Hydration_GoalUpdated.png')

    # Hydration Goal Updated Page
    #unuse #HydrationCalculationDisclaimer = 'new UiSelector().test("Hydration Calculation Disclaimer").className("android.widget.TextView")'
    #Add a scroll up movement here!
    Gesture.swipeUp(self, 1000)
    self.driver.find_element_by_id('com.thermos:id/skip').click()
    sleep(1)
    ScreenShot.AndroidScreenshot('037_Hydration_Disclaimer2.png')
    self.driver.back()

    StartUsingYourProduct = 'new UiSelector().text("Start Using Your Product").className("android.widget.TextView")'
    self.driver.find_element_by_android_uiautomator(StartUsingYourProduct).click()
    sleep(0.5)
    ScreenShot.AndroidScreenshot('038_Thermos_HomeScreen_Pre.png')
    #Need to add a loop to check later
    WebDriverWait(self.driver, 120).until(
        EC.presence_of_element_located(
            (By.ID, "com.thermos:id/share_icon")
        )
    )
    sleep(1)
    ScreenShot.AndroidScreenshot('039_Thermos_HomeScreen1.png')
    # Need to add a loop to check later
    WebDriverWait(self.driver, 120).until(
        EC.presence_of_element_located(
            (By.ID, "com.thermos:id/text_msg")
        )
    )
    sleep(1)
    ScreenShot.AndroidScreenshot('040_Thermos_HomeScreen2.png')
    Gesture.swipeUp(self, 1000)
    sleep(1)
    ScreenShot.AndroidScreenshot('041_Thermos_HomeScreen3.png')