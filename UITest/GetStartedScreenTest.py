from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import ScreenShot
from time import sleep

def test_GetStartedScreen(self):

    ShopThermos = 'new UiSelector().text("Shop Thermos Connected Products").className("android.widget.TextView")'
    AboutThermos = 'new UiSelector().text("About Thermos Connected Products").className("android.widget.TextView")'
    #Shop Thermos ?Need to find a way to check WebElement!
    self.driver.find_element_by_android_uiautomator(ShopThermos).click()
    WebDriverWait(self.driver, 30).until(
        EC.presence_of_element_located(
            (By.ID, "com.thermos:id/activity_web_view_back")
        )
    )
    sleep(3)
    ScreenShot.AndroidScreenshot('004_ShopThermos')
    self.driver.find_element_by_id('com.thermos:id/activity_web_view_back').click()

    #About Thermos ?Need to find a way to check WebElement!
    self.driver.find_element_by_android_uiautomator(AboutThermos).click()
    WebDriverWait(self.driver, 30).until(
        EC.presence_of_element_located(
            (By.ID, "com.thermos:id/activity_web_view_back")
        )
    )
    sleep(3)
    ScreenShot.AndroidScreenshot('005_AboutThermos')
    self.driver.find_element_by_id('com.thermos:id/activity_web_view_back').click()

    #Get Started
    self.driver.find_element_by_id('com.thermos:id/startButton').click()
    WebDriverWait(self.driver, 30).until(
        EC.presence_of_element_located(
            (By.ID, "com.thermos:id/activity_set_up_profile_back")
        )
    )
    sleep(1)
    ScreenShot.AndroidScreenshot('006_SetUpUserProfilePage')