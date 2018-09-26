# Android environment
import os
import unittest
from appium import webdriver

#Import Test Case Modules
import ScreenShot
import GetStartedScreenTest
import SplashScreenTest
import SetUpUserProfile
import DeviceCalibration
import GeneralBaselineGoalSetup

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))

class ThermosTestCase(unittest.TestCase):
    testdevice = ScreenShot.device[0]
    testport = ScreenShot.Port[0]

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0.1'
        desired_caps['deviceName'] = self.testdevice
        desired_caps['udid'] = self.testdevice
        desired_caps['appPackage'] = 'com.thermos'
        desired_caps['appActivity'] = 'com.thermos.smartlid.SetupProfile.SplashScreen'
        ScreenShot.FolderCheckOnAndorid()
        self.driver = webdriver.Remote('http://127.0.0.1:'+self.testport+'/wd/hub', desired_caps)

        #On PC save screenshots
        #ScreenShot.FolderCheckOnPC()
        #self.driver.save_screenshot('screenshots/001_SplashScreen.png')

        #On Android device save screenshots
        ScreenShot.AndroidScreenshot("001_SplashScreen")


    def tearDown(self):
        self.driver.close_app()
        self.driver.quit()

    def test_StartTest(self):
        SplashScreenTest.test_SplashScreen(self)
        GetStartedScreenTest.test_GetStartedScreen(self)
        SetUpUserProfile.test_SetUpUserProfile(self)
        DeviceCalibration.test_DeviceCalibration(self)
        GeneralBaselineGoalSetup.test_GeneralBaselineGoalSetup(self)


if __name__ == '__main__':

    for i in range(0, len(ScreenShot.device)):
        ThermosTestCase.testdevice = ScreenShot.device[i]
        ThermosTestCase.testport = ScreenShot.Port[i]
        unittest.main(exit=False)
        i += 1
