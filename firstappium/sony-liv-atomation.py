import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

desired_cap = {
    "platformName": "Android",
    "deviceName": "28949403",
    "appPackage":"com.sonyliv",
    "appActivity":"com.sonyliv.ui.splash.SplashActivity",
    "app": "C:\\Users\\Satyajit\\Desktop\\sony.apk",
    "newCommandTimeout": 300,
}

driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_cap)
driver.implicitly_wait(60)

for i in range(1):
    driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
    time.sleep(2)

touch = TouchAction(driver)
touch.tap(x=184, y=71).perform()
time.sleep(5)
touch.press(x=353, y=924).move_to(x=365, y=10).release().perform()
time.sleep(5)
touch.tap(x=618, y=1061).perform()
time.sleep(60)
touch.tap(x=630, y=200).perform()
time.sleep(2)
touch.tap(x=655, y=80).perform()

