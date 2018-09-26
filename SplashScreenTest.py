from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
import ScreenShot
from time import sleep

def test_SplashScreen(self):
    try:
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(
                (By.ID, "com.android.packageinstaller:id/permission_allow_button")
            )
        )
    except TimeoutException:
        print("No Permission Pop up!")
    ScreenShot.AndroidScreenshot('002_Location_Permission')

    try:
        self.driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()
    except NoSuchElementException:
        print("No Permission Pop up!")

    sleep(1)

    ScreenShot.AndroidScreenshot('003_FirstPage')