
# Appium-UI-Testing
# Overview

This repository demonstrates how to perform UI testing for mobile applications using Appium. It includes a sample test script for automating the login process of a mobile app.

このリポジトリでは、Appiumを使用してモバイルアプリケーションのUIテストを実行する方法を紹介します。サンプルテストスクリプトには、モバイルアプリのログインプロセスの自動化が含まれています。

---

# Prerequisites
- Install [Appium](https://appium.io/) and [Python](https://www.python.org/downloads/).
- Install the necessary drivers for your target mobile platform (Android/iOS).
- Install the required Python packages by running the following command:
  
  
  ```pip install Appium-Python-Client```

	•	Make sure you have access to an Android emulator or a physical device for testing.

# Setup
**1**.	Clone the repository:

```git clone https://github.com/yourusername/Appium-UI-Testing.git```
```cd Appium-UI-Testing```


**2**.	Start the Appium server (Make sure Appium is installed and running):

```appium```


**3**.	Configure your desired capabilities in the appium_test.py file for your device and app.

---

# Usage

**Step 1**: Configure Desired Capabilities
Edit the desired_caps dictionary in appium_test.py to match your device and application details:

desired_caps = {
   "platformName": "Android",  # Platform name (e.g., Android or iOS)
   "platformVersion": "12.0",  # OS version
   "deviceName": "emulator-5554",  # Emulator or device name
   "app": "/path/to/your/app.apk",  # Path to the application
   "automationName": "UiAutomator2"  # Automation framework for Android
}

**Step 2**: Run the test
Run the test script with the following command:

python appium_test.py

---

# Technologies
- *Python*
- *Appium*
- *Android Emulator*
- *UIAutomator2*
- *JSON*

---
