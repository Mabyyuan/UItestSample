from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
import ScreenShot
from time import sleep

def test_InitialPairSuccess(self):

    # Initial Setup
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
    #Calibration Page
    sleep(1)
    ScreenShot.AndroidScreenshot('023_Calibration_RemoveLid')
    self.driver.find_element_by_id('com.thermos:id/next').click()
    sleep(1)
    ScreenShot.AndroidScreenshot('024_Calibration_DryTube')
    self.driver.find_element_by_id('com.thermos:id/next').click()
    sleep(1)
    ScreenShot.AndroidScreenshot('025_Calibration_Calibrate')
    self.driver.find_element_by_id('com.thermos:id/start_calibrate_button').click()
    sleep(0.5)
    ScreenShot.AndroidScreenshot('026_Calibration_Calibrating')
    WebDriverWait(self.driver, 30).until(
        EC.presence_of_element_located(
            (By.ID, "com.thermos:id/next")
        )
    )
    sleep(1)
    ScreenShot.AndroidScreenshot('027_Calibration_CalibrationComplete')
    self.driver.find_element_by_id('com.thermos:id/next').click()

    #Hydration Page
    sleep(1)
    ScreenShot.AndroidScreenshot('028_Hydration_HydrationGoal')

