from appium import webdriver

# Desired Capabilitiesの設定
desired_caps = {
   "platformName": "Android",  # プラットフォーム
   "platformVersion": "12.0",  # OSバージョン
   "deviceName": "emulator-5554",  # デバイス名
   "app": "/path/to/your/app.apk",  # テスト対象のアプリ
   "automationName": "UiAutomator2"  # 自動化フレームワーク
}

# WebDriverの初期化
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# UI操作のサンプル
element = driver.find_element_by_accessibility_id("Login")
element.click()

# テスト終了
driver.quit()
